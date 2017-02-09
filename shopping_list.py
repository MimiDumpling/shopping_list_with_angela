#make our list
#create our menus in a dictionary
#have user input a menu choice
# #0 - Main Menu
# 1 - Show all lists.
# 2 - Show a specific list.
# 3 - Add a new shopping list.
# 4 - Add an item to a shopping list.
# 5 - Remove an item from a shopping list.
# 6 - Remove a list by nickname.
# 7 - Exit when you are done.


shopping_lists = {"Target": ["socks", "soap", "detergent", "sponges"],
    "Bi-Rite": ["butter", "cake", "cookies", "bread"],
    "Berkeley Bowl": ["apples", "oranges", "bananas", "milk"],
    "Safeway": ["oreos", "brownies", "soda"]}

menu_choices = {0: "Main Menu", 1: "Show all lists.", 2: "Show a specific list.",
3: "Add a new shopping list.", 4: "Add an item to a shopping list.",
5: "Remove an item from a shopping list.", 6: "Remove a list by nickname.",
7: "Exit when you are done."}


def sorting_dictionary(menu_items):
    sorted_keys = menu_items.keys()
    sorted_keys.sort()
    for item in sorted_keys:
        print str(item) + "-" + str(menu_items[item])

def going_shopping(lists):
    sorting_dictionary(menu_choices)
    choice = int(raw_input("What would you like to do? "))
    if choice == 0:
        print menu_choices
        #make the program keep going
    elif choice == 1:
        print " "
        print "Here are your lists: "
        sorting_dictionary(shopping_lists)
    elif choice == 2:
        print " "
        list_choice = raw_input("Which list do you want to look at? ").title()
        print shopping_lists[list_choice] #ask user input for what list they want
    elif choice == 3:
        print " "
        new_list = raw_input("What would you like to call your new list? ")
        new_value = raw_input("What would you like to add to this list? ")
        shopping_lists[new_list] = new_value.split(",")
        sorting_dictionary(shopping_lists)
        #add a new key/value to shopping lists dictionary
        #can't have dup shopping lists
        #.title the rawinput
    elif choice == 4:
        print " "
        list_choice = raw_input("Which list do you want to look at? ").title()
        new_value = raw_input("What would you like to add to this list? ")
        shopping_lists[list_choice].append(new_value)
        sorting_dictionary(shopping_lists)
        #ask which list
        #ask what they want to add
        #make sure there's no dups
    elif choice == 5:
        print " "
        sorting_dictionary(shopping_lists)
        list_choice = raw_input("Which list do you want to look at? ").title()
        remove_value = raw_input("What would you like to remove from this list? ").lower()
        print shopping_lists[list_choice]
        shopping_lists[list_choice].remove(remove_value)
        sorting_dictionary(shopping_list)
        #ask which list
        #ask which item to remove from that list
        #check if that item is in the list
        #remove item
    elif choice == 6:
       print " "
        #ask which list
        #check if list exists
        #remove list
    elif choice == 7:
        #exit program
    else:
        print "That's not a valid command!"

going_shopping(shopping_lists)
