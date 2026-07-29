# Importing required libraries.

import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict
import re

# A function that checks the running status of any website.

def web_status_check(url: str)->None:
    try:
        response: Response = requests.get(url)

        # Extracting response details.
        status_code: int = response.status_code

        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')

        response_time: float = response.elapsed.total_seconds()

        # Displaying the information regarding the URL
        print(f'{"-"*20}')
        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')
        print(f'{"-"*20}')

    except RequestException as e:
        print(f'Error: {e}')


# A function to read the file containing URLs.

def load_url(file_path: str)->str:

    with open(file_path, 'r') as file:

        contents = file.read()
        re_content_list: list = re.findall(r"https?://[^\s]+", contents)
        return re_content_list


# Create a main entry point

def main() -> None:
    file_path: str = input(fr'Please provide the file path containing URLs >>').strip('"')
    url_list_to_check: str = load_url(file_path)
    for url in url_list_to_check:
        web_status_check(url)


# Run the script

if __name__ == '__main__':
    main()
