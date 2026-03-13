phone_book ={}
# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

phone_book["Kartik"] = "123-456-7890"  # This line adds a new entry to the phone_book dictionary, where the key is "Kartik" and the value is "123-456-7890". You can add new key-value pairs to a dictionary by simply assigning a value to a new key.
phone_book["Alice"] = "987-654-3210"  # This line adds another entry to the phone_book dictionary, where the key is "Alice" and the value is "987-654-3210". Now the phone_book dictionary contains two entries: {"Kartik": "123-456-7890", "Alice": "987-654-3210"}.
phone_book["Bob"] = "555-555-5555"  # This line adds a third entry to the phone_book dictionary, where the key is "Bob" and the value is "555-555-5555". Now the phone_book dictionary contains three entries: {"Kartik": "123-456-7890", "Alice": "987-654-3210", "Bob": "555-555-5555"}.
print(f"{BLUE}------ Adding Contacts to Phone Book ------{RESET}")
print(f"{GREEN}Added : Kartik --> {phone_book['Kartik']}{RESET}")  # This line prints the entire phone_book dictionary, which will output {'Kartik': '
print(f"{GREEN}Added : Alice --> {phone_book['Alice']}{RESET}")  # This line prints the phone number associated with the key "Alice" in the phone_book dictionary, which will output "Added : Alice -->987-654-3210".
print(f"{GREEN}Added : Bob --> {phone_book['Bob']}{RESET}")  # This line prints the phone number associated with the key "Bob" in the phone_book dictionary, which will output "Added : Bob -->555-555-5555".


print(f"{YELLOW}------Displaying Contacts from Phone Book------{RESET}")
for name, number in phone_book.items():
    print(f"{BLUE} PhoneBook : {name}: {number}{RESET}")  # This line iterates through each key-value pair in the phone_book dictionary and prints the name and corresponding phone number in a formatted string. The items() method is used to get a view object of the dictionary's key-value pairs, which allows us to access both the name (key) and number (value) in each iteration of the loop.


print(f"{YELLOW}------Searching Contacts in Phone Book------{RESET}") 
names_to_search = ("Alice", "Kartik", "Bob")  # List of names to search for
search_name = "Charlie"  # Single name to search (or you can remove this if focusing on the tuple)

for search in names_to_search:
    if search in phone_book:
        print(f"{GREEN}Contact found: {search} --> {phone_book[search]}{RESET}")
    else:
        print(f"{RED}Contact not found: {search}{RESET}")

# Then handle search_name separately if needed
if search_name in phone_book:
    print(f"{GREEN}Contact found: {search_name} --> {phone_book[search_name]}{RESET}")
else:
    print(f"{RED}Contact not found: {search_name}{RESET}")

print(f"{YELLOW}------Updating Contacts in Phone Book------{RESET}")
phone_book["Alice"] = "111-222-3333"  # This line updates the phone number associated with the key "Alice" in the phone_book dictionary to "111-222-3333". Since dictionaries are mutable, you can change the value of an existing key by assigning a new value to that key.
print(f"{GREEN}Updated : Alice --> {phone_book['Alice']}{RESET}")  # This line prints the updated phone number for "Alice" in the phone_book dictionary, which will output "Updated : Alice -->111-222-3333".



print(f"{YELLOW}------Deleting Contacts in Phone Book------{RESET}")
del phone_book["Bob"]  # This line deletes the entry with the key "Bob" from the phone_book dictionary. The del statement is used to remove a key-value pair from a dictionary by specifying the key. After this line, the phone_book dictionary will no longer contain the entry for "Bob".
print(f"{RED}Deleted : Bob{RESET}")  # This line prints a message indicating that the contact "Bob" has been deleted from the phone_book.


print(f"{YELLOW}------Displaying Contacts from Phone Book after Deletion------{RESET}")
for name, number in phone_book.items():
    print(f"{BLUE} PhoneBook : {name}: {number}{RESET}")  # This line iterates through each key-value pair in the phone_book dictionary and prints the name and corresponding phone number in a formatted string. After the deletion of "Bob", this will output the remaining contacts: "Kartik" and "Alice" with their respective phone numbers.


