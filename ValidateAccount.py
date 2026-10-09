username = "vimaljayganthan16@gmail.com"
password = "shrivim10.08"

userInput = str(input())
if(userInput == username):
  passwordInput = str(input())
  if (passwordInput == password):
    print("Correct Password, Login Successfull")
  else:
    print("Invalid Password, Access Denied")
else:
  print("Invalid Credentials")