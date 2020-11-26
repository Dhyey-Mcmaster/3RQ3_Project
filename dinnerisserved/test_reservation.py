from dinnerisserved.email import Email
from dinnerisserved.passwor import Password
from dinnerisserved.reservation import Reservation
from dinnerisserved.createaccount import CreateAccount
from dinnerisserved.table import Table

#Requirement: Account creation

#Checks the email and password fields for account creation process
def test_email():
    email = Email()

    assert len(email) == 1, "Email cannot be empty"

def test_password():
    password = Password()

    assert len(password) == 1, "Password cannot be empty"

#Account creation is failed for couple of reasons like email-id already taken, web-application is currently under maintenance
def test_account():
    account = CreateAccount()
    check_account = account.CheckAccount(1)

    assert check_account == 1, "Account not created"

#Requirement: Login
#Login failed for errors like email-id is not registered or password is incorrect
def test_login():
    login = CreateAccount()
    check_login = login.CheckLogin(1)

    assert check_login == 1, "Login Failed"

#Requirement: Reservation for table

#Cheks if the table is available for booking or not
def test_table_available():
    table = Table()
    check_table_available = table.check_table_number(0)

    assert check_table_available == 1, "Table not available check next table"

def test_reservation_five_table():
   reservation = Reservation()
   check_reservation = reservation.Book_Reservation(2)

   assert check_reservation == 1, "Max 4 tables can be booked at a time"

def test_reservation_one_table():
    reservation = Reservation()
    check_reservation = reservation.Book_Reservation(1)

    assert check_reservation == 1, "One table should be booked"

def test_confirm_reseravation():
    reservation = Reservation()
    confirm_reserve = reservation.Confirm_Reservation(1)

    assert confirm_reserve == 1, "Reservation is not confirmed"