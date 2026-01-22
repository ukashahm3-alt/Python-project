# ------------------------------------------------------------
# Rental Property Management System
# ------------------------------------------------------------
# Tasks covered:
#   1. Input rent or maintenance record
#   2. Input rent or maintenance records
#   3. Build and display summary table
# ------------------------------------------------------------
properties = {
    "B12-3AB": {"original_cost": 153450, "mortgage": 112345},
    "B13-4CD": {"original_cost": 212130, "mortgage": 180234},
    "B14-5GH": {"original_cost": 120100, "mortgage":  85980},
    "B15-6JK": {"original_cost": 135230, "mortgage": 101321},
    "B16-7MO": {"original_cost": 183230, "mortgage": 130234},
}

# To store rent/repair records
entries = {prop: [] for prop in properties}

# ------------------------------------------------------------
#  Task 2 – Input rent or maintenance records
# ------------------------------------------------------------
def property_data():
    print("\nProperty Data Entry")
    print("=============================")
    print("{:<15} {:<15}".format("Property #", "Location ID"))
    print("=============================")
    for idx, prop_code in enumerate(properties.keys(), 1):
        print("{:<15} {:<15}".format(str(idx), prop_code))
    print("=============================")
    while True:
        prop_code = input("Enter the property code (e.g., B12-3AB): ").strip().upper()
        if not prop_code:
            print("Property code cannot be empty. Please try again.")
            continue
        if prop_code not in properties:
            print("Property code not found. Please enter a valid property code from the list above.")
            continue

        description = input("Enter a brief description (e.g., 'Monthly rent' or 'Plumbing fix'): ").strip()
        if not description:
            print("Description cannot be empty. Please enter a description.")
            continue

        date = input("Enter the date for this record (YYYY-MM-DD): ").strip()
        if not date:
            print("Date cannot be empty. Please enter a date.")
            continue

        amt_in = input("Enter the amount (e.g., Rent=760 or Repairs=-150): ").strip()
        try:
            amount = int(amt_in)
        except ValueError:
            print("Amount must be a whole number. Please try again.")
            continue

        # Store the entry with date
        entries[prop_code].append({"description": description, "amount": amount, "date": date})
        print("Entry recorded successfully!\n")

        more = input("Would you like to enter another record? (Y/N): ").strip().upper()
        if more != "Y":
            break

# ------------------------------------------------------------
def property_report():
    print("\nDetailed Property Report")
    print("=============================")
    prop_code = input("Enter the property code to view details (e.g., B12-3AB): ").strip().upper()
    if prop_code not in properties:
        print("Property code not found. Returning to menu.")
        return
    print(f"\nRecords for {prop_code}:")
    if not entries[prop_code]:
        print("No records found for this property.")
        return
    print("{:<12} {:<15} {:<10}".format("Date", "Description", "Amount"))
    print("-" * 40)
    for rec in entries[prop_code]:
        print("{:<12} {:<15} {:<10}".format(rec.get("date", "-"), rec["description"], rec["amount"]))
    print()

# ------------------------------------------------------------
#  Task 3 – Build and display summary table
# ------------------------------------------------------------
def summary_data():
    print("\nRental Summary Report, :)")

    # aggregate
    summary = {prop: {"rent": 0, "repairs": 0} for prop in properties}
    for prop, recs in entries.items():
        for rec in recs:
            amt = rec["amount"]
            if amt < 0:
                summary[prop]["repairs"] += abs(amt)
            else:
                summary[prop]["rent"] += amt

    # table
    header = "{:<10} {:>15} {:>10} {:>17} {:>15} {:>10} {:>10}"
    row    = "{:<10} {:>15,} {:>10,} {:>17,} {:>15,} {:>10,} {:>9.2f}%"
    print()
    print(header.format("Property#", "Orig. Cost", "Repairs",
                        "Amended Cost", "Mortgage", "Rent", "Rent %"))

    tot_cost = tot_rep = tot_amend = tot_mort = tot_rent = 0

    for prop, master in properties.items():
        ocost = master["original_cost"]
        mort  = master["mortgage"]
        repairs = summary[prop]["repairs"]
        rent    = summary[prop]["rent"]
        amend   = ocost + repairs
        rent_pct = (rent / mort * 100) if mort else 0.0

        print(row.format(prop, ocost, repairs, amend, mort, rent, rent_pct))

        tot_cost  += ocost
        tot_rep   += repairs
        tot_amend += amend
        tot_mort  += mort
        tot_rent  += rent

    total_pct = (tot_rent / tot_mort * 100) if tot_mort else 0.0
    print("-" * 100)
    print(row.format("Total", tot_cost, tot_rep,
                     tot_amend, tot_mort, tot_rent, total_pct))
    print()     # blank line after table

# ------------------------------------------------------------
#  Task 1 – Menu and validation
# ------------------------------------------------------------
def display_menu():
    print("\nProperty Management Menu")
    print("1. Update Property Records")
    print("2. Get Rentals Summary")
    print("3. View Detailed Property Report")
    print("4. Exit the Program")

def get_valid_choice():
    while True:
        choice = input("Please enter your choice (1-4): ").strip()
        if not choice:
            print("Input cannot be empty. Please enter a number from 1 to 4.")
        elif not choice.isdigit():
            print("Invalid input. Please enter a digit (1, 2, 3, or 4).")
        elif len(choice) > 1:
            print("Please enter a single digit (1, 2, 3, or 4).")
        else:
            choice = int(choice)
            if choice in (1, 2, 3, 4):
                return choice
            print("Choice must be 1, 2, 3, or 4. Please try again.")

# ------------------------------------------------------------
#  Main Loop
# ------------------------------------------------------------
if __name__ == "__main__":
    while True:
        display_menu()
        user_choice = get_valid_choice()

        if user_choice == 1:
            property_data()
        elif user_choice == 2:
            summary_data()
        elif user_choice == 3:
            property_report()
        elif user_choice == 4:
            print("\nThank You For Using This Program, Goodbye! :)")
            break
