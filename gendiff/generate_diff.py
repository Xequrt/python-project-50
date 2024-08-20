from gendiff.data import extensions_data
from gendiff.parser import parse
from gendiff.build_diff import make_diff, build_diff
from formatters.stylish import stylish
from formatters.plain import get_plain
from formatters.json_format import get_json


def generate_diff(file1_path, file2_path, output_format='stylish'):
    data1, extension1 = extensions_data(file1_path)
    data2, extension2 = extensions_data(file2_path)

    parsed_data1 = parse(data1, extension1)
    parsed_data2 = parse(data2, extension2)

    if output_format == "stylish":
        return stylish(build_diff(parsed_data1, parsed_data2))
    elif output_format == "plain":
        return get_plain(make_diff(parsed_data1, parsed_data2))
    elif output_format == 'json':
        return get_json(make_diff(parsed_data1, parsed_data2))

    raise ValueError(f"Unrecognized output format: {output_format}")
