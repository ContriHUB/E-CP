class UsernameNotFound(Exception):
    def __init__(self, userName) -> None:
        super().__init__(f'{userName} not found.')