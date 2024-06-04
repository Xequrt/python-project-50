import pytest
from gendiff import generate_diff

@pytest.mark.parametrize('file1, file2, result_file', [
    ('./tests/fixtures/file1.json',
     './tests/fixtures/file2.json',
     './tests/fixtures/correct_result_json.txt')
])
def test_generate_diff(file1, file2, result_file):
    diff = generate_diff(file1, file2, output_format=format)
    with open(result_file) as result_file:
        result = result_file.read()
        assert result == diff