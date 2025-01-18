from agents.tech_lead.tech_lead import run_tech_lead


def run_pm_to_tech_flows(repo_root: str, config_root: str, epic: str):
    print("Running PM to Tech flow...")

    tickets_for_epic = run_tech_lead(repo_root, config_root, epic)

    print(tickets_for_epic.model_dump_json())
    return tickets_for_epic
