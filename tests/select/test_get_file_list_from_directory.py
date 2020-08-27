from pytest import raises
from ..fixtures import cwd_in_tests_root


def test_all_files(cwd_in_tests_root):
    from fil_io.select import get_file_list_from_directory

    path = "./test_files"
    response = get_file_list_from_directory(path)
    assert {
               './test_files/pattern_3.json',
               './test_files/non_fit_pattern_1.json',
               './test_files/pattern_2.json',
               './test_files/pattern_1.json',
               './test_files/pattern_2.csv',
               './test_files/pattern_1.csv'
           } == set(response)


def test_only_json_files(cwd_in_tests_root):
    from fil_io.select import get_file_list_from_directory
    path = "./test_files"
    response = get_file_list_from_directory(path, file_ending=".json")
    assert {
               './test_files/pattern_3.json',
               './test_files/non_fit_pattern_1.json',
               './test_files/pattern_2.json',
               './test_files/pattern_1.json',
            } == set(response)


def test_pattern_files(cwd_in_tests_root):
    from fil_io.select import get_file_list_from_directory
    path = "./test_files"
    response = get_file_list_from_directory(path, pattern="pattern*")
    assert {
               './test_files/pattern_3.json',
               './test_files/pattern_2.json',
               './test_files/pattern_1.json',
               './test_files/pattern_2.csv',
               './test_files/pattern_1.csv'
           } == set(response)


def test_pattern_and_json_files(cwd_in_tests_root):
    from fil_io.select import get_file_list_from_directory
    path = "./test_files"
    response = get_file_list_from_directory(path, file_ending=".json", pattern="pattern*")
    assert {
               './test_files/pattern_3.json',
               './test_files/pattern_2.json',
               './test_files/pattern_1.json',
           } == set(response)


def test_single_file_as_input(cwd_in_tests_root):
    from fil_io.select import get_file_list_from_directory
    path = "./test_files/pattern_1.json"

    with raises(ValueError):
        get_file_list_from_directory(path)


def test_regex(cwd_in_tests_root):
    from fil_io.select import get_file_list_from_directory
    path = "./test_files"

    response = get_file_list_from_directory(path, regex="^pattern_[0-2].json$")
    assert {
               './test_files/pattern_1.json',
               './test_files/pattern_2.json'
           } == set(response)

    response = get_file_list_from_directory(path, file_ending="json", regex="^pattern_[0-2]$")
    assert {
               './test_files/pattern_1.json',
               './test_files/pattern_2.json'
           } == set(response)