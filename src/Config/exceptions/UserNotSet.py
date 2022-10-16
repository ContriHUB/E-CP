class UserNotSet(Exception):
    def __init__(self, msg="User not set yet."):
        super().__init__(self, msg)