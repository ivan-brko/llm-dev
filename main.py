from flows.pm_flow import run_pm_flow
from flows.pm_to_tech_flow import run_pm_to_tech_flows
from repo.prepare_repo import setup_project_directory
from utils.args import parse_args
from utils.caching import configure_caching
from dotenv import load_dotenv

from utils.setup_globals import setup_globals


def main():
    print("Fake dev starting...")
    load_dotenv()

    args = parse_args()

    setup_globals(args.repo_path)

    configure_caching(args.config_root, args.cache_responses)

    setup_project_directory(
        args.repo_path, "git@github.com:ivan-brko/remix-public-template.git"
    )

    pm_flow_output = run_pm_flow(args.repo_path, args.config_root)

    run_pm_to_tech_flows(args.repo_path, args.config_root, pm_flow_output)


main()
