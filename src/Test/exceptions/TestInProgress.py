class TestInProgress(Exception):
    def __init__(self) -> None:
        super().__init__('Another test in progress...')