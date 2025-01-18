import os

REPO_PATH_PREFIX = ""


def read_file_to_string(file_path: str) -> str:
    """
    Reads the contents of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def read_file_to_string_opt(file_path: str) -> str | None:
    """
    Reads the contents of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str | None: The contents of the file as a string, or None if the file does not exist.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return None


def read_file_in_repo(file: str) -> str:
    # Get the full file path by combining the repository root and the relative path
    repo_root = os.path.abspath(REPO_PATH_PREFIX)  # Resolve to an absolute path
    full_path = os.path.abspath(os.path.join(repo_root, file))  # Resolve the file path

    # Ensure the resolved path is within the repository root
    if not full_path.startswith(repo_root):
        return "Access denied: Attempt to access files outside the repository."

    # Ensure the file exists and read its contents
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(
            f"The file '{file}' does not exist in the repository. Full Path: {full_path}"
        )
        return f"The file '{file}' does not exist in the repository."
    except Exception as e:
        return f"An error occurred while reading '{file}': {e}"


def write_file_in_repo(file: str, content: str) -> str:
    """
    Writes content to a file within the repository.

    Args:
        file (str): The relative path to the file within the repository.
        content (str): The content to write to the file.

    Returns:
        str: A success message or an error message.
    """
    # Get the full file path by combining the repository root and the relative path
    repo_root = os.path.abspath(REPO_PATH_PREFIX)  # Resolve to an absolute path
    full_path = os.path.abspath(os.path.join(repo_root, file))  # Resolve the file path

    # Ensure the resolved path is within the repository root
    if not full_path.startswith(repo_root):
        return "Access denied: Attempt to write files outside the repository."

    # Ensure the directory for the file exists
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Write content to the file
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Content successfully written to '{full_path}'."
    except Exception as e:
        return f"An error occurred while writing to '{file}': {e}"
