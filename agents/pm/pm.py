from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from agents.pm.prompts.pm_prompt import PM_PROMPT
from utils.file_ops import read_file_to_string
from agents.pm_lead.prompts.pm_lead_prompt import ProjectEpics
from utils.handle_epics_files import read_todo_epics, read_done_epics
from utils.llm_resolver import get_developer_llm


def run_pm(repo_root: str, config_root: str, epics: ProjectEpics) -> str:
    print(f"Running PM for repo {repo_root} for epic {epics.epics[0].name}...")

    application_idea = read_file_to_string(f"{config_root}/application_idea")

    todo_epics: str = read_todo_epics()
    done_epics: str = read_done_epics()

    prompt = PromptTemplate(
        input_variables=["application_idea", "done_epics", "todo_epics"],
        template=PM_PROMPT,
    )

    llm = get_developer_llm()

    chain = prompt | llm | StrOutputParser()

    # noinspection PyTypeChecker
    result = chain.invoke(
        {
            "application_idea": application_idea,
            "done_epics": done_epics,
            "todo_epics": todo_epics,
        }
    )

    return result
