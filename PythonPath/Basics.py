def atomicDictionary():
    atomicElements = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'Au': 'Gold',
    'S': 'Sulphur'
    }
    atomicElements['Li'] = 'Lithium'

    # Printing the atomic atomicElements
    for i in atomicElements:
        print("Key is ", i, "Value is", atomicElements[i])

    numb = len(atomicElements)
    print("Original no of elements",numb)
    print("Enter the new atomic element")
    answer = "y"

    # Add elements into the dicitonary by interacting with user
    while answer == 'y' or answer == 'Y':
        key = input("Enter the atomic symbol: \t")
        value = input("Enter the atom Name: \t")
        atomicElements[key] = value
        answer = input("Do you want to enter elements Y or N")

    print(atomicElements)

    print('New Number of elements is', len(atomicElements))

    # Search for the element that the user gives
    search = " "
    search = input("Enter the key symbol to search for")

    if search in atomicElements:
        print("Yes element %s exists", search)
        print("Its value is ", atomicElements[search])
    else:
        print("Element not found")
