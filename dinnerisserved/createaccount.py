# noinspection PyMethodMayBeStatic
class CreateAccount:

    def CheckAccount(self, num_account):
        if num_account == 1:  # When the customer has successfully created his account
            return 1
        else:  # When the customer has errors in creating his accounts
            return 0

    def CheckLogin(self, num_login):
        if num_login == 1:  # When the customer has successfully logged in
            return 1
        else:  # When the customer has some errors while logging
            return 0
