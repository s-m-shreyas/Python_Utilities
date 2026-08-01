import re
import os
import csv
from datetime import datetime

def get_today_date() -> str:
    dt = datetime.now()
    return dt.strftime("%Y-%m-%d")  # e.g. "2026-08-01"

def get_file_date(file_path: str) -> str:
    # Get last modified time
    mtime = os.path.getmtime(file_path)
    dt = datetime.fromtimestamp(mtime)
    return dt.strftime("%Y-%m-%d")  # e.g. "2023-12-15"

def get_last_modified_date(file_path: str) -> str:
    # Get last modified time
    mtime = os.path.getctime(file_path)
    dt = datetime.fromtimestamp(mtime)
    return dt.strftime("%Y-%m-%d")  # e.g. "2023-12-15"

def transform_data(some_str: str, 
           txt_path: str)->tuple[list[dict[str, str]] ,str]:

    result_list: list[dict[str, str]] = []
    get_date_of_file: str = get_file_date(txt_path)
    last_modified_date: str = get_last_modified_date(txt_path)
    todays_date: str = get_today_date()

    matches = re.findall(
        r'^(?P<timestamp>\d{2}:\d{2}:\d{2})\s*'
        r'From\s+(?P<from_name>.+?)\s+to\s+'
        r'(?P<to_name>.+?)'
        r'(?:\((?P<msg_type>[^)]+)\))?'
        r':\s*\n\s*(?P<message>.+?)(?=\n\d{2}:\d{2}:\d{2}|\Z)',
        some_str,
        re.MULTILINE | re.DOTALL
    )

    for time_, from_, to, msg_tp, msg in matches:

        result_dict: dict[str, str] = {
            'Input_file_created_date' : get_date_of_file,
            'Input_file_last_modified_date': last_modified_date,
            'Chat_time' : time_,
            'From' : from_,
            'To' : to,
            'Message_type' : msg_tp,
            'Message' : msg
        }

        result_list.append(result_dict)
    
    return result_list, todays_date


def write_to_csv(some_list: list[dict[str, str]], 
                 csv_path: str, 
                 file_generated_date: str)->None:
    
    with open(fr'{csv_path}\{file_generated_date}.csv', 
              'w', 
              newline='', 
              encoding='utf-8') as file:
        csv_object = csv.DictWriter(file, fieldnames=['Input_file_created_date',
                                                      'Input_file_last_modified_date',
                                                      'Chat_time',
                                                      'From',
                                                      'To',
                                                      'Message_type',
                                                      'Message'])
        csv_object.writeheader()
        csv_object.writerows(some_list)


def text_parser(text_file_path: str, 
                csv_file_out_path: str)->None:
    with open(text_file_path, 'r', encoding='utf-8') as file:
        content: str = file.read()
        load_as_csv: tuple[list[dict[str, str]] ,str]= transform_data(content, text_file_path)
        write_to_csv(load_as_csv[0], csv_file_out_path, load_as_csv[1])


def main()->None:
    text_file_in_path: str = input(fr'text_file_in_path >> ').strip('"')
    csv_file_out_path: str = input(fr'csv_file_out_path >> ').strip('"')
    text_parser(text_file_in_path, csv_file_out_path)


if __name__ == '__main__':
    main()

fr"""
Below paths are good for case, in your case please refer to the paths you have.

# text_file_in_path >> "C:\Users\User\zoom_chat_input\meeting_saved_chat (1).txt"
# csv_file_out_path >> "C:\Users\User\zoom_chat_output"
"""
