import json
import os

reports = []
search_history = []


# Function 1: Add a new rescue report
def add_report(reports):
    print("\n--- Add Rescue Report ---")

    report_id = input("Enter Report ID: ")
    name = input("Enter Reporter Name: ")
    location = input("Enter Incident Location: ")
    description = input("Enter Incident Description: ")

    report = {
        "id": report_id,
        "name": name,
        "location": location,
        "description": description,
        "status": "Pending"
    }

    reports.append(report)

    reports.append(report)

with open("reports.json", "w") as file:
    json.dump(reports, file, indent=4)

print("\nReport added successfully!")


# Function 2: View all rescue reports
def view_reports(reports):
    print("\n--- Rescue Reports ---")

    if not reports:
        print("No rescue reports available.")
        return

    for report in reports:
        print("\nReport ID:", report["id"])
        print("Reporter Name:", report["name"])
        print("Location:", report["location"])
        print("Description:", report["description"])
        print("Status:", report["status"])
        print("-" * 30)


# Function 3: Update report status
def update_status(reports):
    print("\n--- Update Report Status ---")

    if not reports:
        print("No reports available to update.")
        return

    report_id = input("Enter Report ID to update: ")

    for report in reports:
        if report["id"] == report_id:
            print("Current Status:", report["status"])
            print("\nChoose New Status:")
            print("1. Pending")
            print("2. In Progress")
            print("3. Resolved")

            choice = input("Enter your choice: ")

            if choice == "1":
                report["status"] = "Pending"
            elif choice == "2":
                report["status"] = "In Progress"
            elif choice == "3":
                report["status"] = "Resolved"
            else:
                print("Invalid status choice.")
                return

            print("Report status updated successfully!")
            return

    print("Report ID not found.")


# Function 4: Add search history
def add_search_record():
    print("\n--- Add Search History ---")

    search = input("Enter search details: ")

    record = {
        "search": search
    }

    search_history.append(record)

    print("Search history added successfully!")


# Function 5: View search history
def view_search_history():
    print("\n--- Search History ---")

    if not search_history:
        print("No search history available.")
        return

    for index, record in enumerate(search_history, start=1):
        print(f"{index}. {record['search']}")


# Main menu
def main():
    while True:
        print("\n================================")
        print("     RESCUE-SHADOW SYSTEM")
        print("================================")
        print("1. Add Rescue Report")
        print("2. View Rescue Reports")
        print("3. Update Report Status")
        print("4. Add Search History")
        print("5. View Search History")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_report(reports)

        elif choice == "2":
            view_reports(reports)

        elif choice == "3":
            update_status(reports)

        elif choice == "4":
            add_search_record()

        elif choice == "5":
            view_search_history()

        elif choice == "6":
            print("Exiting Rescue-Shadow. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()