from logging import warning

inventory = float(0)

errorCount = float(0)

def warnUser(message: str) -> None:
    global errorCount
    warning(message)
    errorCount += 1

def get_value_input() -> float:
    userInput = ""
    while userInput != "quit":
        userInput = input("Enter a stock quantity: ")
        if userInput == "quit":
            print("Goodbye!")
            break
        try:
            addedInventory = float(userInput)
            if addedInventory < 0:
                warnUser("Negative number not accepted, try again!")
            else:
                return float(addedInventory)
        except:
            warnUser(f"Input of type {str(type(userInput))} not accepted, try again!")
            continue
    return 0

def process_delivery(current_total: float, new_value: float) -> float:
    new_total = float(current_total) + float(new_value)
    if new_total > 500:
        print("Inventory has overstocked!")
    return new_total
#
# def calculate_tax(amount) -> float:
#
# def generate_report(total_units, failed_attempts) -> str:
