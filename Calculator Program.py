print("Welcome to Calculator.")

operation = ["Add", "Subtract", "Multiply", "Divide"]

a = input(operation)

def calculator():
  if a== "add":
    add1 = int(input("Enter the Number of your choosing."))
    add2 = int(input("Enter the Number of your choosing."))
    answeradd = (print(add2 + add1))
  if a== "subtract":
      sub1 = int(input("Enter the Number of your choosing."))
      sub2 = int(input("Enter the Number of your choosing."))
      answersub = (print(sub1 - sub2))
  if a== "multiply":
    times1 = int(input("Enter the Number of your choosing."))
    times2 = int(input("Enter the Number of your choosing."))
    answertimes = print(times1 * times2)
  if a == "divide":
    div1 = int(input("Enter the Number of your choosing."))
    div2 = int(input("Enter the Number of your choosing."))
    answerdiv = print(div1 / div2)
calculator()