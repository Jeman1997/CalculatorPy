def cal(f,op,l):
  if op not in ['+','==','/','*','-','%']:
    print(f"Your entered {op} as the operation.It's not a valid operation")
    cal(input("Enter the first number:\n"),input("What Operation do you want to perform?\n['==','+','/','*','-','%']\n"),input("Enter the last number:\n"))
  print(f'the result is:\n{eval(f+op+l)}')
cal(input("Enter the first number:\n"),input("What Operation do you want to perform?\n['==','+','/','*','-','%']\n"),input("Enter the last number:\n"))
run=True
while run:
  if input("Do u want to use the calculator again?(y or n)\n").lower()=='y':
    cal(input("Enter the first number:\n"),input("What Operation do you want to perform?\n['==','+','/','*','-','%']\n"),input("Enter the last number:\n"))
  else:
    print("Well, Thank you!")
    run=False