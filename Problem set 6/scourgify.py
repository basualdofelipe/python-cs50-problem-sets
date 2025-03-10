import csv, sys

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments ")
    else:
        try:
            table = list(open_csv(f"csv/{sys.argv[1]}"))
            output = f"csv/{sys.argv[2]}"
        except IndexError:
            print("Too few command-line arguments")
        except FileNotFoundError:
            print(f"Could not read {sys.argv[1]}")
        else:
            save_csv(table, output)

def open_csv(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            fname, lname = row["name"].split(",") 
            yield [fname, lname, row["house"]]

def save_csv(table, output):
    with open(output, "w", newline="") as csvfile:
        fieldnames = ["first_name", "last_name", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in table:
            print(student)
            writer.writerow(
                {"last_name": student[0],
                "first_name": student[1],
                "house": student[2]}
                )


if __name__ == "__main__":
    main()