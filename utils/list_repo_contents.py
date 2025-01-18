import os


def list_files_recursively(directory: str) -> str:
    """
    Recursively lists all files in a directory and returns the result as a string.

    Args:
        directory (str): The path to the directory to list files from.

    Returns:
        str: A string representation of the directory structure.
    """
    contents = []
    for root, dirs, files in os.walk(directory):
        # Compute relative path
        relative_root = os.path.relpath(root, directory)

        # Add directories and files
        contents.extend([os.path.join(relative_root, d) for d in dirs])
        contents.extend([os.path.join(relative_root, f) for f in files])

    paths = [
        c
        for c in contents
        if ".git/" not in c and "node_modules/" not in c
        if ".idea/" not in c
        if ".vscode/" not in c
    ]
    return "\n".join(paths)
