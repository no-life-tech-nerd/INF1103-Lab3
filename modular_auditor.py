from logging import warning

inventory = int(0)

errorCount = int(0)

def warnUser(message: str) -> None:
    global errorCount
    warning(message)
    errorCount += 1

def get_value_input():
    userInput = input("Enter a stock quantity: ")
    if userInput == "quit":
        return "quit"
    try:
        addedInventory = int(userInput)
        if addedInventory < 0:
            warnUser("Negative number not accepted, try again!")
            return 0
        else:
            return int(addedInventory)
    except:
        warnUser(f"Input of type {str(type(userInput))} not accepted, try again!")
        return 0

def process_delivery(current_total: int, new_value: int) -> int:
    new_total = int(current_total) + int(new_value)
    if new_total > 500:
        print("Inventory has overstocked!")
    return new_total

def calculate_tax(amount: int) -> float:
    return (0.1 * amount)
#
# def generate_report(total_units, failed_attempts) -> str:

userData = ""
while userData != "quit":
    userData = get_value_input()
    if userData == "quit":
        print("Goodbye!")
        break
    if userData > 0:
        inventory = process_delivery(inventory, userData)
        print(calculate_tax(userData))
