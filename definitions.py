import pathlib



DEFINITION_FILE = pathlib.Path(__file__)

BASE_PATH = DEFINITION_FILE.parent

LINK_TO_CSV_FILES = BASE_PATH / "lesson_16" / "1_csv" / "csv_files_to_be_processed"

LINK_TO_JSON_STORAGE = BASE_PATH / "lesson_16" / "2_json" / "json_files_to_be_processed"

PROCESSED_JSON_FILE = BASE_PATH / "lesson_16" / "2_json" / "result_of_test_json.json"

XML_FILES_STORAGE = BASE_PATH / "lesson_16" / "3_xml" / "xml_files_to_be_parsed"

PROCESSED_CSV_FILE = BASE_PATH / "lesson_16" / "1_csv" / "result_of_2_processed_csv_files.csv"

SAVE_DECORATOR_LOG = BASE_PATH / "lesson_17" /"3_decorators"

PATH_TO_CSV_MERGED_FILE = BASE_PATH / "csv_processed_file"

PATH_TO_API_SERVER = BASE_PATH / "lesson_19" / "1_api_server" / "app.py"

PATH_TO_NASA_PHOTO_1 = BASE_PATH / "lesson_19" / "photo_1.jpg"
