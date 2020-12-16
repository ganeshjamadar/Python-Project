from saveable import Saveable

class User(Saveable):

    def __init__(self, username, password):
        """
        docstring
        """
        self.username = username
        self.password = password

    def login(self):
        return 'Logged In'

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

