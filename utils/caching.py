from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache


def configure_caching(config_root: str, cache_responses: bool):
    if cache_responses:
        path = f"{config_root}/.langchain.db"
        print(f"Cache responses enabled, using {path} for caching...")
        set_llm_cache(SQLiteCache(database_path=path))
