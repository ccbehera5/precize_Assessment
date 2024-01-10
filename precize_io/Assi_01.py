import json

data = []

def load_from_file():
    try:
        with open("results.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_to_file():
    with open("results.json", "w") as file:
        json.dump(data, file, indent=2)
    print("Data saved to 'sat_results.json' file.")

def initialize_data():
    global data
    data = load_from_file()

def insert_data():
    name = input("Enter Name: ")
    sat_score = float(input("Enter SAT Score: "))
    passed = "Pass" if sat_score > 30 else "Fail"

    candidate = {
        "Name": name,
        "SAT Score": sat_score,
        "Passed": passed
    }

    data.append(candidate)
    print("Data inserted successfully!")

def view_all_data():
    print(json.dumps(data, indent=4))

def get_rank():
    name = input("Enter Name to get rank: ")
    sorted_data = sorted(data, key=lambda x: x["SAT Score"], reverse=True)
    for i, candidate in enumerate(sorted_data, start=1):
        if candidate["Name"] == name:
            print(f"Rank of {name}: {i}")
            return
    print(f"No record found for {name}")

def update_score():
    name = input("Enter Name to update SAT score: ")
    for candidate in data:
        if candidate["Name"] == name:
            new_score = float(input("Enter new SAT score: "))
            candidate["SAT Score"] = new_score
            candidate["Passed"] = "Pass" if new_score > 30 else "Fail"
            print("SAT score updated successfully!")
            return
    print(f"No record found for {name}")

def delete_record():
    name = input("Enter Name to delete record: ")
    for candidate in data:
        if candidate["Name"] == name:
            data.remove(candidate)
            print(f"Record for {name} deleted successfully!")
            return
    print(f"No record found for {name}")

initialize_data()

while True:
    print("\nMenu:")
    print("1. Insert data")
    print("2. View all data")
    print("3. Get rank")
    print("4. Update score")
    print("5. Delete one record")
    print("6. Save to file")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        insert_data()
    elif choice == "2":
        view_all_data()
    elif choice == "3":
        get_rank()
    elif choice == "4":
        update_score()
    elif choice == "5":
        delete_record()
    elif choice == "6":
        save_to_file()
    elif choice == "7":
        save_to_file()
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
