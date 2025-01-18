import re


def clean_llm_response(response: str, debug: bool = False) -> str:
    """
    Cleans up a string received from an LLM to make it ready for further processing.

    """
    if not isinstance(response, str):
        raise ValueError("Input must be a string.")

    # Strip leading and trailing whitespace
    cleaned_response = response.strip()

    # Replace multiple spaces, tabs, or newlines with a single space
    cleaned_response = re.sub(r"\\s+", " ", cleaned_response)

    # Normalize quotes and other characters
    cleaned_response = (
        cleaned_response.replace("“", '"')
        .replace("”", '"')
        .replace("‘", "'")
        .replace("’", "'")
    )

    # Normalize to UTF-8 (optional, depending on use case)
    cleaned_response = cleaned_response.encode("utf-8", errors="ignore").decode("utf-8")

    if debug:
        print(f"Initial LLM tool call argument: >>>{response}<<<")
        print(f"Cleaned LLM tool call argument: >>>{cleaned_response}<<<")

    return cleaned_response
