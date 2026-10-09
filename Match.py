a = int(input())
b = int(input())
operator = input()
match operator:
  case '+':
    print(a+b)
  case '-':
    print(a-b)
  case '*':
    print(a*b)
  case '/':
    print(a/b)
  case _:
    print("Invalid Operator")