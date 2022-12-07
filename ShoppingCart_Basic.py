class ShoppingCart:
    def __init__(self):
        self.name = "none"
        self.price = 0
        self.quantity = 0
    
    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setQuant(self, quantity):
        self.quantity = quantity

#this is the class that creates each item that will be put into the shopping cart
#-----------------------------------------------------------------------------------------------------------------------------
def printMenuFun():
    print("MENU")
    print("a - Add item to cart")
    print("d - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit")

    #This prints the menu of operations that the user can use

#-----------------------------------------------------------------------------------------------------------------------------
def addItem(shoppingCartList):
    obj1 = ShoppingCart()

    objName = input("Please enter the name of an item: ")
    obj1.setName(objName)

    objPrice = int(input("Please enter items price: "))
    obj1.setPrice(objPrice)

    objQuant = int(input("Please enter items quantity: "))
    obj1.setQuant(objQuant)

    shoppingCartList.append(obj1)

    #This function creates a new object and then takes all of the input parameters from the user
    #Once all of the input parameters are created the new object is appended to the list AKA shopping cart
    
#-----------------------------------------------------------------------------------------------------------------------------

def remItem(shoppingCartList):
    sizeOfList = int(len(shoppingCartList))
    i = int(0)

    itemRemove = input("Please enter the name of the item you want to remove: ")

    while(i < sizeOfList):
        if(itemRemove == shoppingCartList[i].name):
            shoppingCartList.pop(i)
        else:
            print("Item not found, please try again.")
        i += 1

    #This takes the user input of the items name and then if it finds that item it will remove the item from the "shopping cart"

#-----------------------------------------------------------------------------------------------------------------------------

def changeQuant(shoppingCartList):
    sizeOfList = int(len(shoppingCartList))
    i = int(0)

    itemQuant = input("Please enter the name of the item you want to change quantity: ")

    while(i < sizeOfList):
        if(itemQuant == shoppingCartList[i].name):
            newQuant = input("Please enter new quantity: ")
            shoppingCartList[i].quantity = newQuant
            break
        else:
            print("Item not found, please try again.")
        i += 1

        #This takes the user input of what item they want to change and then compares the name to the elements in the list names 
        #if the element is found it prompts the user for a new quantity and then updates the quantity
        #if the item is not found it informs the user to try again

#-----------------------------------------------------------------------------------------------------------------------------

def outputShoppingCart(shoppingCartList):
    sizeOfList = int(len(shoppingCartList))
    i = int(0)
    totalPrice = int(0)
    
    while(i < sizeOfList):
        print(shoppingCartList[i].name + ": " + str(shoppingCartList[i].quantity) + " @ $" + str(shoppingCartList[i].price))
        totalPrice += (int(shoppingCartList[i].price) * int(shoppingCartList[i].quantity))
        i += 1

    print("Total cart price: $" + str(totalPrice))
    #This outputs all of the intems in the cart with their name, quantity, and price and then outputs the total value of all the items

#-----------------------------------------------------------------------------------------------------------------------------

def executeMenu(userInp, shoppingCartList):
    if(userInp == 'a'):
        addItem(shoppingCartList)
    elif(userInp == 'd'): 
        remItem(shoppingCartList)
    if(userInp == 'c'):
        changeQuant(shoppingCartList)
    if(userInp == 'o'):
        outputShoppingCart(shoppingCartList)
    if(userInp == 'q'):
        return 
    #this function takes the users char input and then converts it into a function call for the program to handle

 #-----------------------------------------------------------------------------------------------------------------------------   
def main():
    shoppingCartList = [] #creates a new list to store all of the shopping cart elements
    userInp = "/0"

    while(userInp != 'q'): #runs while the user doesn't want to quit
        printMenuFun() #prints the menue again for he loop
        if userInp == 'q':
            return#ends the program if the user wants to quit
        userInp = input("Choose an option from the menu: ") #takes the user input to see what they want to do from the menue
        executeMenu(userInp , shoppingCartList) #Passes the users input and the list into a new function to execute what the user wants to do
        print("")#this just adds whitespace to make the program easier to read


if __name__ == "__main__":
    main()


