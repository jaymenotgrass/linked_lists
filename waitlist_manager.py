# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None

    
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else: 
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return f"{name} was added to the end of the waitlist."
    def remove(self, name):
        current = self.head
        previous = None

        while current:
            if current.name == name:
                if previous: 
                    previous.next = current.next
                else:
                    self.head = current.next
                return f"{name} was removed from waitlist."
            previous = current
            current = current.next
        return f"{name} not found"
    def print_list(self):
        current = self.head
        if not current:
                print("The waitlist is empty.")
                return
        while current:
            print(current.name, end=" -> ")
            current = current.next
        print("None")
        


def waitlist_generator():
    # Create a new linked list instance
    wait_list = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            list = wait_list.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            list = wait_list.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            list = wait_list.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            list = wait_list.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work? 
    ## Within the list, there is one attribute and 4 methods. The attribute creates a 
    ## node using the Node class, and the 4 methods are used to alter the list when needed.
    ## The 2 add functions both start off by locating the first name value. When adding to the front,
    ## it puts the original "head" value in the next position, and replaces the "new node" to be at the "head".
    ## For adding a value at the end, it loops through all the current values until the "current.next" 
    ## equals "none", meaning that you found the end of the list. It would then place the "new node" in that position.
    ## Remove is a similar function but instead of stopping at the end of the list when 
    ## a value equals "none", it stops when it matches up with the inputed name. It then removes that name and 
    ## redirects the arrows to connect. 
- What role does the head play?
    ## The head plays a major role in having a starting point for the lists and values
    ## to be based off of. When needing to add a value at the front, it will check 
    ## to see what the head value is currently at, and then re-apply the new node to the 
    ## head function. For the rest of the functions, it uses the head to figure out what the 
    ## next value is. 
- When might a real engineer need a custom list like this?
    ## A real engineer would need a custom list like this one above when creating a task schedule.
    ## Engineers need to be very organized and are always completing tasks and adding more tasks. 
    ## This list would make it easy to remove tasks and add them while also viewing the ones you still have.
'''
