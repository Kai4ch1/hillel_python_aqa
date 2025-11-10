import csv
import definitions
file_1_csv = definitions.LINK_TO_CSV_FILES / "file_1.csv"
file_2_csv = definitions.LINK_TO_CSV_FILES / "file_2.csv"

def compare_the_files(file_1, file_2):
    list_1 = []
    list_2 = []
    with open(file_1, newline='') as f1:
        reader = csv.DictReader(f1)
        for i in reader:
            list_1.append(i)

    with open(file_2, newline='') as f2:
        reader_2 = csv.DictReader(f2)
        for j in reader_2:
            list_2.append(j)

    unprocessed_lists = list_1 + list_2
    unique_elements_list = []
    for i in unprocessed_lists:
        if i not in unique_elements_list:
            unique_elements_list.append(i)

    with open(definitions.PROCESSED_CSV_FILE, "w", newline='') as res:
        writer = csv.DictWriter(res, fieldnames=unique_elements_list[0].keys())
        writer.writeheader()
        writer.writerows(unique_elements_list)

    print(f"result ={unique_elements_list}")

if __name__ == "__main__":
    compare_the_files(file_1_csv, file_2_csv)