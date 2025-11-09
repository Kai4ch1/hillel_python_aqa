import pathlib



DEFINITION_FILE = pathlib.Path(__file__)

BASE_PATH = DEFINITION_FILE.parent

LINK_TO_CSV_FILES = BASE_PATH / "lesson_16" / "1_csv" / "csv_files_to_be_processed"

PATH_TO_CSV_MERGED_FILE = BASE_PATH / "csv_processed_file"
print(BASE_PATH)
print(LINK_TO_CSV_FILES)