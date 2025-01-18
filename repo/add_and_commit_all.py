from git import Repo


def add_and_commit_all(repo_path: str, commit_message: str) -> None:
    """
    Adds all modified files to the staging area and commits them.

    Args:
        repo_path (str): Path to the Git repository.
        commit_message (str): Commit message to use.

    Raises:
        Exception: If there is an issue adding or committing files.
    """
    try:
        # Load the repository
        repo = Repo(repo_path)

        # Ensure the repository is not in a detached HEAD state
        if repo.head.is_detached:
            raise Exception("Repository is in a detached HEAD state. Cannot commit.")

        # Add all changes to the staging area
        repo.git.add(A=True)  # Equivalent to `git add --all`

        # Commit the changes
        repo.index.commit(commit_message)
        print(f"Committed changes with message: '{commit_message}'")

    except Exception as e:
        print(f"An error occurred: {e}")
