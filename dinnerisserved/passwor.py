class Password:

    def __init__(self):
        self.password = ["Password"]

    def __len__(self):
        return len(self.password)

    def check_password_strength(self):
        return None                     #will be implemented in future

    def change_password(self, change_pass):
        if change_pass:
            return True
        else:
            None