import os
from datetime import datetime, timedelta
from git import Repo, exc


def clone_or_open_repo(url, path):
    if os.path.isdir(path):
        return Repo(path)
    return Repo.clone_from(url, path)


def get_commit_for_date(repo, ref, date):
    try:
        commit_sha = repo.git.rev_list('-1', '--before', date.isoformat(), ref)
        if commit_sha:
            return repo.commit(commit_sha)
    except exc.GitCommandError:
        pass
    return None


def count_lines_in_commit(commit, file_path):
    try:
        blob = commit.tree / file_path
        return blob.data_stream.read().decode('utf-8', errors='ignore').count('\n')
    except KeyError:
        return None


def main(repo_url, file_path, branch='main'):
    repo = clone_or_open_repo(repo_url, 'repo')
    results = []
    start = datetime(2023, 1, 1)
    end = datetime(2025, 12, 31)
    while start <= end:
        commit = get_commit_for_date(repo, branch, start)
        if commit:
            count = count_lines_in_commit(commit, file_path)
            if count is not None:
                results.append((start.strftime('%Y-%m-%d'), count))
        start += timedelta(weeks=1)
    for date_str, count in results:
        print(f"{date_str}: {count}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Weekly line counts for a file in a GitHub repo')
    parser.add_argument('repo_url', help='URL of the GitHub repository')
    parser.add_argument('file_path', help='Path to the file within the repository')
    parser.add_argument('--branch', default='main', help='Branch to inspect (default: main)')
    args = parser.parse_args()

    main(args.repo_url, args.file_path, branch=args.branch)
