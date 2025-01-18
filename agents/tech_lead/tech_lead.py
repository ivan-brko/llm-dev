from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

from agents.data_formatter.data_formatter import run_data_formatter
from agents.tech_lead.prompts.tech_lead_prompt import TECH_LEAD_PROMPT, TicketList
from tools.repository_contents_retriever import read_repo_file
from utils.file_ops import read_file_to_string
from utils.handle_epics_files import read_todo_epics, read_done_epics
from utils.list_repo_contents import list_files_recursively
from utils.llm_resolver import get_developer_llm


def prepare_prompt(
    application_idea: str,
    repo_contents: str,
    todo_epics: str,
    done_epics: str,
    epic: str,
):
    prompt = PromptTemplate(
        input_variables=[
            "application_idea",
            "done_epics",
            "todo_epics",
            "repo_contents",
            "epic",
        ],
        template=TECH_LEAD_PROMPT,
    )

    return prompt.format_prompt(
        application_idea=application_idea,
        repo_contents=repo_contents,
        todo_epics=todo_epics,
        done_epics=done_epics,
        epic=epic,
    )


def prepare_agent():
    llm = get_developer_llm()
    react_prompt = hub.pull("hwchase17/react")
    tools = [read_repo_file]
    agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
    agent_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
    )
    return agent_executor


def run_tech_lead(repo_root: str, config_root: str, epic: str) -> TicketList:
    print(f"Running Tech Lead for repo {repo_root}...")

    application_idea = read_file_to_string(f"{config_root}/application_idea")

    todo_epics: str = read_todo_epics()
    done_epics: str = read_done_epics()

    repo_contents = list_files_recursively(repo_root)

    prompt = prepare_prompt(
        application_idea, repo_contents, todo_epics, done_epics, epic
    )

    agent_executor = prepare_agent()

    tickets_str = agent_executor.invoke(input={"input": prompt})["output"]

    tickets: TicketList = run_data_formatter(tickets_str, TicketList)

    return tickets
