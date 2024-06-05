import pytest
from gendiff import generate_diff

@pytest.mark.parametrize('file1, file2, result_file', [
    ('./tests/fixtures/file1.json',
     './tests/fixtures/file2.json',
     './tests/fixtures/correct_result_json.txt'),
    ('./tests/fixtures/file1.yml',
     './tests/fixtures/file2.yml',
     './tests/fixtures/correct_result_yml.txt'),
    ('./tests/fixtures/file1.yaml',
     './tests/fixtures/file2.yaml',
     './tests/fixtures/correct_result_yaml.txt')
])
def test_generate_diff(file1, file2, result_file):
    diff = generate_diff(file1, file2, output_format=format)
    with open(result_file) as result_file:
        result = result_file.read()
        assert result == diff