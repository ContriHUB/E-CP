class UnsupportedLanguage(Exception):
    def __init__(self, lang: object) -> None:
        super().__init__(f'{lang} not supported')