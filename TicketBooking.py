username = input()
if(username == "xyz@gmail.com"):
  password = input()
  if(password == "0616"):
    print("Login Successfull")
    logged_in = True
  else:
    print("Password Error")
    logged_in = False
else:
  print("Invalid Username")
  logged_in = False

train_available = True
seat_available = True
payment = True

if(logged_in):
  if(train_available):
    if(seat_available):
      if(payment):
        print("Ticket booked")
      else:
        print("Payment Failed")
    else:
      print("Seat Not Available")
  else:
    print("Train Not Available")
else:
  print("Invalid Loggin Credentials")