from utils.file_ops import read_file_in_repo, write_file_in_repo


def read_done_epics():
    return read_file_in_repo("epics/done_epics.json")


def read_todo_epics():
    return read_file_in_repo("epics/todo_epics.json")


def write_done_epics(contents: str):
    write_file_in_repo("epics/done_epics.json", contents)


def write_todo_epics(contents: str):
    write_file_in_repo("/epics/todo_epics.json", contents)
