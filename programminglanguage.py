class ProgrammingLanguage:
    def __str__(self, *args, **kwargs):
        return "{}, {} typing, reflection={}, First appeared in {}".format(self.language, self.typing, self.reflection,
                                                                           self.year)

    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year
