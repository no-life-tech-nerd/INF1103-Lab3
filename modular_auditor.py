from logging import warning

inventory = int(0)

userInput = ""

errorCount = int(0)

def warnUser(message: str) -> None:
    global errorCount
    warning(message)
    errorCount += 1

while userInput != "quit":
    userInput = input("Enter a stock quantity: ")
    if userInput == "quit":
        print("Goodbye!")
        break
    try:
        addedInventory = int(userInput)
        if addedInventory < 0:
            warnUser("Negative number not accepted, try again!")
        else:
            inventory = int(inventory) + int(addedInventory)
    except:
        warnUser(f"Input of type {str(type(userInput))} not accepted, try again!")
        continue
    if inventory > 500:
        print("Inventory has overstocked!")
        break

print(f"Total Units Processed: {str(inventory)}")
print(f"Number of Failed/Rejected Entries: {str(errorCount)}")
