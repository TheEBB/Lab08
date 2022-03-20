#print ("Hello World, my name is Eve Cran and I love Python!")

userName = input ("Hello! Please enter your first name.")
print ("Hello,",userName,"! Nice to meet you.")
userPassword = input ("Please enter your password.")
if(userName.lower() == "eve" and userPassword == "Passwordofmychoice"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")
