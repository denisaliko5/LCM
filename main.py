while True:
  try:
    int1 = int(input("Enter the 1st integer: "))
    break
  except:
    print("Your input must be an integer: ")
while True:
  try:
    int2 = int(input("Enter the 2nd integer: "))
    break
  except:
    print("Your input must be an integer: ")
for i in range(int1*int2):
  if (i+1) % int1 == 0 and (i+1) % int2 == 0:
    break
print("The LCM of", int1, "and", int2, "is", i+1)