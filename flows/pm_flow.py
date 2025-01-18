from agents.pm.pm import run_pm
from agents.pm_lead.pm_lead import run_pm_lead


def run_pm_flow(repo_root: str, config_root: str):
    print("Running PM flow...")

    epics = run_pm_lead(repo_root, config_root)
    print(f"Epics: {epics}")

    detailed_epic = run_pm(repo_root, config_root, epics)

    return detailed_epic
