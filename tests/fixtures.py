from pytest import fixture
from os import getcwd, chdir


@fixture
def cwd_in_tests_root():
    cwd = getcwd()
    cwd_list = cwd.split("/")
    while cwd_list[-1] != "tests":
        cwd_list = cwd_list[:-1]
    chdir("/".join(cwd_list))
    yield
    chdir(cwd)

