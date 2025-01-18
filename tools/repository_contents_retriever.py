from langchain_core.tools import tool

from utils.file_ops import read_file_in_repo
from tools.utils import clean_llm_response


@tool
def read_repo_file(repo_file: str) -> str:
    """
    Reads the contents of a file in the repository based on a relative path.

    Args:
        repo_file (str): The relative path to the file within the repository. Don't put the repository root in the path.

    Returns:
        str: The contents of the file as a string.
    """

    repo_file_clean = clean_llm_response(repo_file)
    return read_file_in_repo(repo_file_clean)
