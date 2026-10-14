import json
import os

FILE = "reports.json"


def load_reports():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_reports(reports):
    with open(FILE, "w") as file:
        json.dump(reports, file, indent=4)


def add_report(reports):
    name = input("Missing person's name or identifier: ").strip()
    location = input("Last known location: ").strip()
    details = input("Additional details: ").strip()

    if not name or not location:
        print("Name/identifier and location are required.")
        return

    report = {
        "id": len(reports) + 1,
        "identifier": name,
        "location": location,
        "details": details,
        "priority": "Needs assessment",
        "status": "Reported",
        "verified": False
    }

    reports.append(report)
    save_reports(reports)
    print("Report saved successfully!")


def view_reports(reports):
    if not reports:
        print("No reports available.")
        return

    for report in reports:
        print("\n----------------------")
        print("Report ID:", report["id"])
        print("Identifier:", report["identifier"])
        print("Location:", report["location"])
        print("Details:", report["details"])
        print("Priority:", report["priority"])
        print("Status:", report["status"])
        print("Verified:", report["verified"])


def update_status(reports):
    try:
        report_id = int(input("Enter report ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for report in reports:
        if report["id"] == report_id:
            print("1. Reported")
            print("2. Under assessment")
            print("3. Rescue in progress")
            print("4. Resolved")
            choice = input("Select status: ")

            statuses = {
                "1": "Reported",
                "2": "Under assessment",
                "3": "Rescue in progress",
                "4": "Resolved"
            }

            if choice in statuses:
                report["status"] = statuses[choice]
                save_reports(reports)
                print("Status updated!")
            else:
                print("Invalid choice.")
            return

    print("Report ID not found.")


def main():
    reports = load_reports()

    while True:
        print("\n=== RESCUE-SHADOW ===")
        print("1. Add missing-person report")
        print("2. View reports")
        print("3. Update report status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_report(reports)
        elif choice == "2":
            view_reports(reports)
        elif choice == "3":
            update_status(reports)
        elif choice == "4":
            print("Exiting Rescue-Shadow.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
