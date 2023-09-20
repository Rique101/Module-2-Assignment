from serialsearch import *  # Import the serial search function

def identical(list1, list2):
     # Iterate through the index
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False  

    else:
        return True  

def main():
    #Write down lists to test
    List1 = ['E', 'B', 'E', 'F', 'A', 'F']
    List2 = ['E', 'B', 'E', 'F', 'A', 'F']

    #List1 = ['E', 'B', 'E', 'F', 'A', 'C']
    #List2 = ['E', 'B', 'E', 'F', 'A', 'F']
    

    # List1 = ['E', 'B', 'E', 'F', 'A', 'F', 'C']
    # List2 = ['E', 'B', 'E', 'F', 'A', 'F']

    if identical(List1, List2):
        print("Two lists are strictly identical!")
    else:
        print("Two lists aren't strictly identical!")

    # Print out the two lists
    print("List1:", List1)
    print("List2:", List2)

if __name__ == "__main__":
    main()
