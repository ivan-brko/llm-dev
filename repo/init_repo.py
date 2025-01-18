from git import Repo
from pathlib import Path


def initialize_git_repo(path: str) -> Repo:
    """
    Initializes a new Git repository at the specified path.
    If the path does not exist, it will be created.

    Args:
        path (str): The path where the Git repository should be initialized.

    Returns:
        Repo: The initialized Git repository object.

    Raises:
        Exception: If the repository initialization fails.
    """
    repo_path = Path(path)

    # Ensure the directory exists
    try:
        repo_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise Exception(f"Failed to create the directory '{path}': {e}")

    try:
        # Initialize the repository
        repo = Repo.init(repo_path)
        print(f"Initialized a new Git repository at: {repo_path}")
        return repo
    except Exception as e:
        raise Exception(f"Failed to initialize Git repository: {e}")
