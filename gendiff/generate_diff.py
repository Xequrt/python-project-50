from gendiff.data import extensions_data
from gendiff.parser import parse
from gendiff.stylish import output_stylish


# def format_line(key, value, prefix):
#     return f'{prefix} {key}: {str(value).lower()}\n'


# def compare_and_append(diff, key, parsed_data1, parsed_data2):
#     if parsed_data1[key] == parsed_data2[key]:
#         diff.append(format_line(key, parsed_data1[key], ' '))
#     else:
#         if key in parsed_data1:
#             diff.append(format_line(key, parsed_data1[key], '-'))
#         if key in parsed_data2:
#             diff.append(format_line(key, parsed_data2[key], '+'))
#
#
# def generate_diff(file1_path, file2_path, output_format):
#     data1, extension1 = extensions_data(file1_path)
#     data2, extension2 = extensions_data(file2_path)
#
#     parsed_data1 = parse(data1, extension1)
#     parsed_data2 = parse(data2, extension2)
#     diff = []
#
#     for key in sorted(set(parsed_data1.keys()) | set(parsed_data2.keys())):
#         if key in parsed_data1 and key in parsed_data2:
#             compare_and_append(diff, key, parsed_data1, parsed_data2)
#         elif key in parsed_data1:
#             diff.append(format_line(key, parsed_data1[key], '-'))
#         else:
#             diff.append(format_line(key, parsed_data2[key], '+'))

# return "{\n  " + "  ".join(diff) + "}"


def make_diff(parsed_data1, parsed_data2):
    diff = []
    for key in sorted(set(parsed_data1.keys()) | set(parsed_data2.keys())):
        if key not in parsed_data2:
            diff.append({
                "key": key,
                "value": "removed",
                "new": parsed_data1[key]
            })
        elif key not in parsed_data1:
            diff.append({
                "key": key,
                "value": "added",
                "old": parsed_data2[key]
            })
        elif isinstance(parsed_data1[key], dict) and isinstance(parsed_data2[key], dict):
            child = make_diff(parsed_data1[key], parsed_data2[key])
            if child:
                diff.append({
                    "key": key,
                    "value": "tree",
                    "children": child
                })
            else:
                diff.append({
                    "key": key,
                    "value": "unchanged",
                    "meta": parsed_data1[key]
                })
        elif parsed_data1[key] == parsed_data2[key]:
            diff.append({
                "key": key,
                "value": "unchanged",
                "meta": parsed_data1[key]
            })
        elif parsed_data1[key] != parsed_data2[key]:
            diff.append({
                "key": key,
                "value": "changed",
                "new": parsed_data1[key],
                "old": parsed_data2[key]
            })
    return diff


def generate_diff(file1_path, file2_path, output_format):
    data1, extension1 = extensions_data(file1_path)
    data2, extension2 = extensions_data(file2_path)

    parsed_data1 = parse(data1, extension1)
    parsed_data2 = parse(data2, extension2)

    diff = make_diff(parsed_data1, parsed_data2)
    if output_format == "stylish":
        return output_stylish(diff)

    raise ValueError(f"Unrecognized output format: {output_format}")
