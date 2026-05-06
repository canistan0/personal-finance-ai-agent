import csv

def load_expenses(file_path):
    expenses = []
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
        return expenses
    except FileNotFoundError:
        raise Exception("CSV file not found.")