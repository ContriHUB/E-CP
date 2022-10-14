class UsernameNotFound(Exception):
    def __init__(self, msg="User not found"):
        super().__init__(self, msg)