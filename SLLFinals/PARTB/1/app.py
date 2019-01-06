TempData = []
def FarToCel(far):
  cel = (far - 32) * 5 / 9
  data = (far , cel)
  TempData.append(data)
  print("From F to C is", data)
def celToFar(cel):
  far = (cel * 9 / 5) + 32 
  data = (cel, far)
  TempData.append(data)
  print("From C to F is", data)

while(1):
  choice = int(input("1 for cel to far \n 2 for far to cel \n 3 for display \n 4 for exit"))
  if (choice == 1):
    temp = float(input("Enter temperature in celcius"))
    celToFar(temp)

  elif (choice == 2):
    temp = float(input("Enter temperature in Far"))
    FarToCel(temp)

  elif (choice == 3):
    print(TempData)
  
  elif (choice == 4):
    exit(0)
