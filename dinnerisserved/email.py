class Email:

    def __init__(self):
        self.email = ["xyz@gmail.com"]

    def __len__(self):
        return len(self.email)

    def check_email_available(self):
        return None                 #will be implemented in future