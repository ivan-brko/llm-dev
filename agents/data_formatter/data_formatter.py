import typing
from typing import Union

from langchain_core.prompts import PromptTemplate

from agents.data_formatter.data_formatter_prompt import DATA_FORMATTER_PROMPT
from utils.llm_resolver import get_long_context_llm, get_general_purpose_llm


def run_data_formatter(
    data: str,
    schema: Union[typing.Dict, type],
    additional_instructions: str | None = None,
):
    print(f"Running data formatter...")

    prompt = PromptTemplate(
        input_variables=["data", "additional_instructions"],
        template=DATA_FORMATTER_PROMPT,
    )

    llm = get_general_purpose_llm().with_structured_output(schema)

    chain = prompt | llm

    result = chain.invoke(
        {
            "data": data,
            "additional_instructions": additional_instructions or "",
        }
    )

    return result
