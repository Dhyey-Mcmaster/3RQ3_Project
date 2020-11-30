from dinnerisserved.email import Email
from dinnerisserved.passwor import Password
from dinnerisserved.reservation import Reservation
from dinnerisserved.createaccount import CreateAccount
from dinnerisserved.table import Table
from dinnerisserved.settings import Settings
from dinnerisserved.login import Login


# Requirement: Account creation
# Checks the email and password fields for account creation process
def test_create_account_phone():
    account = CreateAccount()
    account_phone = account.Create_using_phone_email()

    assert account_phone == 1, "Creating account using Phone-number failed"

def test_create_account_email():
    account = CreateAccount()
    account_email = account.Create_using_phone_email()

    assert account_email == 0, "Creating account using Email-id failed"


def test_email():
    email = Email()

    assert len(email) == 1, "Email cannot be empty"


def test_password():
    password = Password()

    assert len(password) == 1, "Password cannot be empty"


def test_email_available():
    email = Email()
    check_email_available = email.check_email_available()

    assert check_email_available == 1, "Email not available"


def test_password_strength():
    password = Password()
    check_password_strength = password.check_password_strength()

    assert check_password_strength == 1, "Password is too weak"


# Account creation is failed for couple of reasons like email-id already taken, web-application is currently under maintenance
def test_account():
    account = CreateAccount()
    check_account = account.CheckAccount(1)

    assert check_account == 1, "Account not created"


# Requirement: Login
# Login failed for errors like email-id is not registered or password is incorrect
def test_login():
    login = Login()
    check_login = login.CheckLogin(1)

    assert check_login == 1, "Login Failed"

#requirement Login using phone number: this will check if the customer has chosen to login using phone number or email-id
def test_login_phone():
    login = Login()
    check_login_phone = login.login_phone_number()

    assert check_login_phone == 1, "Login using phone-number failed"

def test_email_id():
    login = Login()
    check_login_email_id = login.login_email_id()

    assert check_login_email_id == 1, "Login using Email-id failed"


# Requirement: Reservation for table
# Checks if the table is available for booking or not
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

    assert check_reservation == 1, "No tables booked"

#Requirement reservation details: Will look for a button click and if the customer is logged-in
def test_reservation_details():
    reserve_detail = Reservation()
    check_details = reserve_detail.Reservation_details()

    assert check_details == 1, "You can not view the reservation details"

#Requirement confirm_reservation: The customer will receive a message and he will asked to confirm his reservation but
# clicking a link provided in a message
def test_confirm_reservation():
    reservation = Reservation()
    confirm_reserve = reservation.Confirm_Reservation(1)

    assert confirm_reserve == 1, "Reservation is not confirmed"

#Requiremnet change payment option: This will look if the customer had added the correct info for the payment and is valid
def test_payment_update():
    setting = Settings()
    payment_set = setting.payment_settings(True)

    assert payment_set, "Payment cannot be updated"

#Requiremnet change password: This will allow the customer to change the password, only if the customer is logged-in
def test_change_password():
    change_password = Password()
    test_change_pass = change_password.change_password(1)

    assert test_change_password == 1, "Password is not updated"