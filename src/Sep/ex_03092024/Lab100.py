class VWOLoginPage:

    def __init__(self, emailid, passw):
        self.email = emailid
        self.password = passw

    def page_details(self):
        if self.email == "ankitadhamne@gmail" and self.password == "Anki123":
            print("Successfully login")
        else:
            print("Try again")

email = input("Enter the email \n")
password = input("Enter the password \n")


vwo_obj = VWOLoginPage(email, password)
vwo_obj.page_details()
