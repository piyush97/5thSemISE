def atomicDict():
  elements = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'Li': 'Lithium'
  }
  for i in elements:
    print(elements[i])
  
  elements['C'] = 'Carbon'
  numberOfElements = len(elements)
  print("Number of elements are:", numberOfElements)

  key = input("Enter the atomic Symbol")
  value = input("Enter the Atomic Element")

  if key not in elements:
    elements[key] = value
    print("Inserted Successfully")
  else:
    print("Element is Duplicate")
  print(elements)
  print("Number of elements again are:", len(elements))

  searchedElement = input("Enter  element to search for")
  if searchedElement in elements:
    print("Yes", searchedElement, " Exists")
    print("Value is ", elements[searchedElement])
  else:
    print("Element Does'nt exists")
