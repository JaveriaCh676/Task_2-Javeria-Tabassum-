# Expense Tracker

A simple Python-based expense tracking program that allows users to input expenses and get a running total.

## Features

- Add multiple expense amounts
- Input validation for negative numbers and non-numeric entries
- Running total display after each entry
- Final report showing total amount spent
- User-friendly interface with clear prompts

## How It Works

1. The program starts with a total of `0`
2. Users enter expense amounts in Rupees (Rs)
3. Each valid expense is added to the running total
4. The program continues until the user enters `0`
5. A final report displays the total amount spent

## Input Rules

- **Positive numbers only** - Negative amounts are rejected
- **Numbers only** - Text input will show an error
- **Enter `0`** - Stops the program and shows the final report

## Usage Example

```
===================================
       EXPENSE TRACKER
===================================
Keep adding your expenses.
Type '0' to stop.

Enter expense amount (Rs): 250
✅ Rs. 250.00 added!
   Total so far: Rs. 250.00

Enter expense amount (Rs): 75.50
✅ Rs. 75.50 added!
   Total so far: Rs. 325.50

Enter expense amount (Rs): 0

===================================
         FINAL REPORT
===================================
  Total Spent:  Rs. 325.50
===================================
Thank you! Program is closing.
```


## Code Structure

- `total` - Accumulator variable to track running sum
- `while True` - Infinite loop until user enters `0`
- `try-except` - Handles non-numeric input
- `if-elif` - Checks for stop condition (0) and negative amounts






