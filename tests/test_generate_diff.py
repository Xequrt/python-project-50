import os
import pytest
from gendiff import generate_diff


def get_absolute_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


@pytest.mark.parametrize('file1, file2, format, result_file', [
    ('file1_tree.json',
     'file2_tree.json',
     'stylish',
     'correct_result_tree_json_yaml_yml.txt'),
    ('file1_tree.yml',
     'file2_tree.yml',
     'stylish',
     'correct_result_tree_json_yaml_yml.txt'),
    ('file1_tree.yaml',
     'file2_tree.yaml',
     'stylish',
     'correct_result_tree_json_yaml_yml.txt'),
    ('file1_tree.json',
     'file2_tree.json',
     'plain',
     'correct_result_plain.txt'),
    ('file1_tree.json',
     'file2_tree.json',
     'json',
     'correct_result_json_format.txt')
])
def test_generate_diff(file1, file2, format, result_file):
    file1_path = get_absolute_path(file1)
    file2_path = get_absolute_path(file2)
    result_file_path = get_absolute_path(result_file)
    diff = generate_diff(file1_path, file2_path, output_format=format)
    with open(result_file_path) as result_file:
        result = result_file.read()
        assert result == diff
