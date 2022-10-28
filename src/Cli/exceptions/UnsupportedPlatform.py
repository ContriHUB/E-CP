class UnsupportedPlatform(Exception):
    '''Raised when an unsupported website url is used'''
    def __init__(self) -> None:
        super().__init__('url points to unsupported website')