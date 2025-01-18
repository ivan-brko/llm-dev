import os
import shutil
from git import Repo

from repo.add_and_commit_all import add_and_commit_all
from repo.init_repo import initialize_git_repo


def setup_project_directory(target_directory: str, repo_url: str):
    """
    Set up a project directory by cloning a Git repository into it,
    removing the `.git` folder, and placing all files in the specified directory.

    :param target_directory: The path where the project should be set up.
    :param repo_url: The URL of the Git repository to clone.
    """
    print("Preparing repo...")

    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)
    print(f"Directory ensured: {target_directory}")

    # Temporary directory for cloning
    temp_clone_dir = os.path.join(target_directory, "temp_clone")

    try:
        # Clone the repository into a temporary directory
        print(f"Cloning repository from {repo_url} into temporary directory...")
        Repo.clone_from(repo_url, temp_clone_dir)
        print(f"Repository cloned into {temp_clone_dir}")

        # Move all files from the temporary directory to the target directory
        for item in os.listdir(temp_clone_dir):
            source_path = os.path.join(temp_clone_dir, item)
            target_path = os.path.join(target_directory, item)

            # Move files or directories to the target directory
            if os.path.isdir(source_path):
                if os.path.exists(target_path):
                    shutil.rmtree(target_path)
                shutil.move(source_path, target_path)
            else:
                shutil.move(source_path, target_path)

        # Remove the temporary clone directory
        shutil.rmtree(temp_clone_dir)
        print(f"Temporary clone directory {temp_clone_dir} removed")

        # Remove the `.git` folder in the target directory
        git_dir = os.path.join(target_directory, ".git")
        if os.path.exists(git_dir):
            shutil.rmtree(git_dir)
            print(f".git directory removed from {target_directory}")

        print(f"Project setup successfully in {target_directory}")

        initialize_git_repo(target_directory)
        add_and_commit_all(target_directory, "Initial application setup")

    except Exception as e:
        # Clean up the temporary directory in case of failure
        if os.path.exists(temp_clone_dir):
            shutil.rmtree(temp_clone_dir)
        print(f"Error during project setup: {e}")


if __name__ == "__main__":
    # Define the target directory and repository URL
    target_dir = "/Users/ivan/Projects/temp/fakerepo2"
    repo_url = "git@github.com:ivan-brko/remix-public-template.git"

    setup_project_directory(target_dir, repo_url)
