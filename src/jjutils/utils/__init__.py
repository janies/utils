import csv
import json

__all__ = (
    "csv_file_to_list",
    "json_file_to_list",
)

def csv_file_to_list(filename, config=None):
    """
    This funtion takes the name of a CSV file and produces a list of dictionary
    items from the content of the file.
    """
    output_list = []
    with open(filename) as f:
        reader= csv.DictReader(f)
        for line in reader:
            output_list.append(line)
    return output_list

def json_file_to_list(filename, config=None):
    """
    This function takes the name of a JSON file and produces a list of
    dictionaries.
    """
    with open(filename) as fp:
        return json.load(fp)
