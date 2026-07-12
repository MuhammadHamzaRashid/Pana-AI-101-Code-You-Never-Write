# --- THE RULES (Your Private Knowledge) ---
DUE_AMOUNT = 1000  # What everyone owes for the ground
GROUP_MEMBERS = ["Ahmed", "Bilal", "Dawood", "Ehtesham", "Zahoor"]

# Rule 1: Mystery Numbers (Mapping phone numbers to names)
mystery_map = {
    "0345-XXXX789": "Dawood"
}

# Rule 2: Previous Debts (Money people owed you BEFORE this trip/ground)
previous_debts = {
    "Zahoor": 1000
}

# --- THE MESSY DATA (The Digital Record) ---
# Format: (Date, From, Amount, Memo)
transactions = [
    ("2025-10-10", "Ahmed", 1000, "Ground"),
    ("2025-10-10", "0345-XXXX789", 1000, "(No Memo)"),
    ("2025-10-11", "Bilal", 1000, "for ground booking"),
    ("2025-10-11", "Zahoor", 1000, "old balance clearance"),
    ("2025-10-12", "Ehtesham", 1000, "ground dues"),
]

# --- THE RECONCILIATION ENGINE ---
paid_amounts = {name: 0 for name in GROUP_MEMBERS}
untracked_cash = 0

for date, sender, amount, memo in transactions:
    # Identify the person
    person = mystery_map.get(sender, sender)
    
    if person in paid_amounts:
        # Check if they have a debt to settle first
        debt = previous_debts.get(person, 0)
        
        if debt > 0:
            if amount <= debt:
                # All money goes to debt
                previous_debts[person] -= amount
                print(f"Log: {person}'s {amount} cleared part of their old debt.")
            else:
                # Some goes to debt, the rest to the ground
                leftover = amount - debt
                previous_debts[person] = 0
                paid_amounts[person] += leftover
                print(f"Log: {person}'s {amount} cleared debt and added {leftover} to ground.")
        else:
            # No debt, all money goes to ground
            paid_amounts[person] += amount
    else:
        print(f"Alert: Unknown transaction from {sender} of {amount}. Ignoring.")
        untracked_cash += amount

# --- THE FINAL REPORT ---
print("\n" + "="*30)
print("FINAL RECONCILIATION REPORT")
print("="*30)

total_for_ground = 0
not_fully_paid = []

for person in GROUP_MEMBERS:
    current_paid = paid_amounts[person]
    total_for_ground += current_paid
    status = "✅ Paid" if current_paid >= DUE_AMOUNT else f"❌ Owes {DUE_AMOUNT - current_paid}"
    
    if current_paid < DUE_AMOUNT:
        not_fully_paid.append(person)
        
    print(f"{person.ljust(10)}: {status}")

print("-" * 30)
print(f"Total Cash for Ground: {total_for_ground}")
print(f"Total Expected:       {len(GROUP_MEMBERS) * DUE_AMOUNT}")

# --- THE MESSAGE FOR THE GROUP ---
if not not_fully_paid:
    message = "Everyone has paid in full. Books are closed!"
else:
    names_list = ", ".join(not_fully_paid)
    message = f"Everyone's accounted for except {names_list}. I'll message them before I close the books."

print("\nMESSAGE FOR GROUP CHAT:")
print(message)
