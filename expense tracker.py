# ================================
#   EXPENSE TRACKER - Python
# ================================

total = 0  # Accumulator

print("=" * 35)
print("       EXPENSE TRACKER")
print("=" * 35)
print("Keep adding your expenses.")
print("Type '0' to stop.\n")

while True:
    try:
        expense = float(input("Enter expense amount (Rs): "))

        if expense == 0:
            break
        elif expense < 0:
            print("❌ Negative amount not allowed. Try again.\n")
            continue

        total = total + expense  # Accumulator (main logic)
        print(f"✅ Rs. {expense:.2f} added!")
        print(f"   Total so far: Rs. {total:.2f}\n")

    except ValueError:
        print("❌ Please enter numbers only. Try again.\n")

# Final result
print("\n" + "=" * 35)
print("         FINAL REPORT")
print("=" * 35)
print(f"  Total Spent:  Rs. {total:.2f}")
print("=" * 35)
print("Thank you! Program is closing.")