

class Table:
    """"""

    def __init__(self, data: list):
        """Класс для баз данных"""
        # self.name = name
        # self.columns = columns
        # self.data = data
        self.name = data[2]
        self.columns = data[0]
        self.data = data[1]


    # def __repr__(self):
    #     return
