from langchain_core.prompts import PromptTemplate

from utils.file_ops import read_file_to_string
from agents.pm_lead.prompts.pm_lead_prompt import PM_LEAD_PROMPT, ProjectEpics
from utils.handle_epics_files import read_todo_epics, read_done_epics, write_todo_epics
from utils.llm_resolver import get_developer_llm


def run_pm_lead(repo_root: str, config_root: str) -> ProjectEpics:
    print(f"Running PM lead for repo {repo_root}...")

    application_idea = read_file_to_string(f"{config_root}/application_idea")

    todo_epics: str = read_todo_epics()
    done_epics: str = read_done_epics()

    prompt = PromptTemplate(
        input_variables=["application_idea", "done_epics", "todo_epics"],
        template=PM_LEAD_PROMPT,
    )

    llm = get_developer_llm().with_structured_output(ProjectEpics)

    chain = prompt | llm

    # noinspection PyTypeChecker
    result: ProjectEpics = chain.invoke(
        {
            "application_idea": application_idea,
            "done_epics": done_epics,
            "todo_epics": todo_epics,
        }
    )

    write_todo_epics(result.model_dump_json())

    return result


if __name__ == "__main__":
    print("Testing PM lead")
    repo_root = "/Users/ivan/Projects/temp/fakerepo"
    config_root = "/Users/ivan/Projects/llm/fake-dev"

    from langchain.globals import set_llm_cache
    from langchain_community.cache import SQLiteCache

    set_llm_cache(SQLiteCache(database_path=f"{config_root}/.langchain.db"))

    import dotenv

    dotenv.load_dotenv(f"{config_root}/.env")
    results = run_pm_lead(repo_root, config_root)
    print(results.model_dump_json())
