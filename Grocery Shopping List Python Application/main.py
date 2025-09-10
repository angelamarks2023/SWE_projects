#This is a Grocery Shopping List
#It is created by using Python and a List as a data structure
#There are four options for the user to choose from in the #program: add, remove, display, and quit

#Create a list of strings to keep track of the grocery item in #the shopping list
groceryList = []


#Adding a grocery item to the list
def add_groceryItem(groceryItem):
  groceryList.append(groceryItem)
  print("Grocery item was added successfully.")


#Removed the grocery list once the shopping is completed
def remove_groceryItem(groceryItem):
  if groceryItem in groceryList:
    groceryList.remove(groceryItem)
    print("Grocery item removed successfully.")
#In case the user put in a non-existent data
  else:
    print("Grocery item not found.")


#Displaying the grocery item in the list in order
def display_groceryList():
  if groceryList:
     print(" Grocery list contains: ")
     for index, groceryItem in enumerate(groceryList, start=1):
       print(f"{index}.{groceryItem}")
#In case the user put in a non-existen data
  else:
      print("The grocery list is empty.")


#This part is to prompt the user to input the data into the program
# Adding a grocery item to the list
def get_groceryItem_from_user():
  return input("Enter the grocery item: ")


#Removing an item from the grocery list
def get_groceryItem_to_remove():
  return input("Enter the grocery item to remove: ")


#Displaying the options for the user to choose what they want #to do
#There are four options to choose
#'A' is for adding a grocery item to the list
#'R' is for removing a grocery item from the list
#'D' is for displaying a grocery item in order
#'Q' is for quitting the program
def get_groceryItem_choice():
  return input("Enter:\n"
               "'A'to add a grocery list\n"
               "'R' to remove a grocery list\n"
               "'D' to display grocery lists\n"
               "'Q' to quit the program: ").upper()


#Create the loop to run the program

while True:
  print("Hello!\n"
        "Welcome to Grocery Shopping List.")
  option = get_groceryItem_choice()
  if option == 'A':
    groceryItem = get_groceryItem_from_user()
    add_groceryItem(groceryItem)
  elif option == 'R':
    groceryItem = get_groceryItem_to_remove()
    remove_groceryItem(groceryItem)
  elif option == 'D':
    display_groceryList()
  elif option == 'Q':
    break
  else:
    print("Invalid choice. Please try again. ")
