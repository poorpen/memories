from memories.domain.user.value_objects import credentials


class User:
    def __init__(self, email: credentials.EmailAddress, password: credentials.Password):
        self.email = email
        self.password = password
