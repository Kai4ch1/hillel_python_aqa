import pathlib



DEFINITION_FILE = pathlib.Path(__file__)

BASE_PATH = DEFINITION_FILE.parent

LINK_TO_CSV_FILES = BASE_PATH / "lesson_16" / "1_csv" / "csv_files_to_be_processed"

PROCESSED_CSV_FILE = BASE_PATH / "lesson_16" / "1_csv" / "result_of_2_processed_csv_files.csv"

PATH_TO_CSV_MERGED_FILE = BASE_PATH / "csv_processed_file"
