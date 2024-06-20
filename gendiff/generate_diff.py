from gendiff.data import extensions_data
from gendiff.parser import parse
from gendiff.stylish import stylish


def build_diff(parsed_data1, parsed_data2):
    return {
        "value": "root",
        "children": make_diff(parsed_data1, parsed_data2)
    }


def make_diff(parsed_data1, parsed_data2):
    diff = []
    for key in sorted(set(parsed_data1.keys()) | set(parsed_data2.keys())):
        if key in parsed_data1 and key in parsed_data2:
            if isinstance(parsed_data1[key], dict) and isinstance(parsed_data2[key], dict):
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
            else:
                diff.append({
                    "key": key,
                    "value": "changed",
                    "new": parsed_data1[key],
                    "old": parsed_data2[key]
                })
        elif key not in parsed_data2:
            if isinstance(parsed_data1[key], dict):
                diff.append({
                    "key": key,
                    "value": "tree",
                    "children": make_diff(parsed_data1[key], {})
                })
            else:
                diff.append({
                    "key": key,
                    "value": "removed",
                    "new": parsed_data1[key]
                })
        elif key not in parsed_data1:
            if isinstance(parsed_data2[key], dict):
                diff.append({
                    "key": key,
                    "value": "tree",
                    "children": make_diff({}, parsed_data2[key])
                })
            else:
                diff.append({
                    "key": key,
                    "value": "added",
                    "old": parsed_data2[key]
                })
    return diff


def generate_diff(file1_path, file2_path, output_format):
    data1, extension1 = extensions_data(file1_path)
    data2, extension2 = extensions_data(file2_path)

    parsed_data1 = parse(data1, extension1)
    parsed_data2 = parse(data2, extension2)

    diff = build_diff(parsed_data1, parsed_data2)
    if output_format == "stylish":
        return stylish(diff)

    raise ValueError(f"Unrecognized output format: {output_format}")
