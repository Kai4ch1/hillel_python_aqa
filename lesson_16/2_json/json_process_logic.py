import definitions

import json
import logging
json_storage = definitions.LINK_TO_JSON_STORAGE
json_file_1 = json_storage / 'localizations_en.json'
json_file_2 = json_storage / 'login.json'

logging.basicConfig(
            filename='json_parse.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            force=True
            )
logger = logging.getLogger("LOG EVENT")

def json_or_error(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            print(data)
            logger.info("Completed with Success")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format{json_file}")

if __name__ == '__main__':
    for file_to_process in json_storage.iterdir():
        json_or_error(file_to_process)