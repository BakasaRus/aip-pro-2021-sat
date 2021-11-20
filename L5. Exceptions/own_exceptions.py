class TextRuError(Exception):
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return f'Error {self.code}: {self.description}'


try:
    raise TextRuError(187, 'Error while checking for originality')
except TextRuError as error:
    print(error.code)
