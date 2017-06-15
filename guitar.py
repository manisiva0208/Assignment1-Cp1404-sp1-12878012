class Guitar:
    def __str__(self, *args, **kwargs):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return 2017 - self.year

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False