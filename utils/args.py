import argparse


def parse_args():
    print("Parsing arguments...")
    parser = argparse.ArgumentParser(description="Fake Dev CLI")
    parser.add_argument(
        "--git_push", type=bool, default=True, help="Run Git Push after changes"
    )
    parser.add_argument(
        "--cache_responses", type=bool, default=True, help="Cache LLM responses"
    )
    parser.add_argument("--repo_path", type=str, help="Path to the repository")
    parser.add_argument("--config_root", type=str, help="Path to the config root")
    args = parser.parse_args()
    return args
