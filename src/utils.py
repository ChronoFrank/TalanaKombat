import os
import json
import requests

BASE_JSON_FILE_PATH = os.path.join("src", "../game_champions.json")


def read_json_file(file_path: str = BASE_JSON_FILE_PATH):
    path = file_path
    with open(path, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
            return data
        except json.JSONDecodeError as e:
            print("Error parsing the json data from file")
            raise e


def load_json_from_url(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            text = response.text
            data = json.loads(text)
            return data
        except json.JSONDecodeError as e:
            print("Error parsing the json data from url")
            raise e
