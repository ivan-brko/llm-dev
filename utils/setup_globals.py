from utils import file_ops


def setup_globals(repo_root):
    print("Setting up globals...")
    file_ops.REPO_PATH_PREFIX = repo_root
