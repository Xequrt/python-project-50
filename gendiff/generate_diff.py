from gendiff.data import extensions_data
from gendiff.parser import parse


def generate_diff(file1_path, file2_path, output_format):
    data1, extension1 = extensions_data(file1_path)
    data2, extension2 = extensions_data(file2_path)

    parsed_data1 = parse(data1, extension1)
    parsed_data2 = parse(data2, extension2)
    diff = {}
    for key in sorted(set(parsed_data1.keys()) | set(parsed_data2.keys())):
        if key in parsed_data1 and key in parsed_data2:
            if parsed_data1[key] == parsed_data2[key]:
                diff[f"  {key}"] = parsed_data1[key]
            elif parsed_data1[key] != parsed_data2[key]:
                diff[f"- {key}"] = parsed_data1[key]
                diff[f"+ {key}"] = parsed_data2[key]
        elif key in parsed_data1:
            diff[f"- {key}"] = parsed_data1[key]
        else:
            diff[f"+ {key}"] = parsed_data2[key]
    return diff