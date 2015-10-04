from tabulate import tabulate


class Tabulate:
    def __init__(self):
        pass

    @staticmethod
    def tabulate(*args, **kwargs):
        return tabulate(*args, **kwargs)
