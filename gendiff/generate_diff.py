from gendiff.data import extensions_data
from gendiff.parser import parse


def generate_diff(file1_path, file2_path, output_format):
    data1, extension1 = extensions_data(file1_path)
    data2, extension2 = extensions_data(file2_path)

    parsed_data1 = parse(data1, extension1)
    parsed_data2 = parse(data2, extension2)
    diff = []
    for key in sorted(set(parsed_data1.keys()) | set(parsed_data2.keys())):
        if key in parsed_data1 and key in parsed_data2:
            if parsed_data1[key] == parsed_data2[key]:
                diff.append(f'  {key}: {str(parsed_data1[key]).lower()}\n')
            elif parsed_data1[key] != parsed_data2[key]:
                if key in parsed_data1:
                    diff.append(f'- {key}: {str(parsed_data1[key]).lower()}\n')
                if key in parsed_data2:
                    diff.append(f'+ {key}: {str(parsed_data2[key]).lower()}\n')

        elif key in parsed_data1:
            diff.append(f'- {key}: {str(parsed_data1[key]).lower()}\n')
        else:
            diff.append(f'+ {key}: {str(parsed_data2[key]).lower()}\n')
    return "{\n  " + "  ".join(diff) + "}"
