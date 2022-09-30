class TestNotFound(Exception):
    def __init__(self) -> None:
        super().__init__('Test not found')