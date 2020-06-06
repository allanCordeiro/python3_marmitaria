from datetime import date, datetime
from src.utils import Append

class Products:
    def __init__(self, id_product: int, category: str, description: str, manufacture_dt: date, qty: int):
        self.__id = id_product
        self.__category = category
        self.__description = description
        self.__manufacture_dt = manufacture_dt
        self.__qty = qty

    @property
    def category(self):
        return self.__category

    @property
    def description(self):
        return self.__description

    @property
    def manufacture_dt(self):
        return self.__manufacture_dt

    @property
    def qty(self):
        return self.__qty

    def create_product(self):
        create_file = Append()
        data: list = [self.__id,
                      self.__category,
                      self.__description,
                      self.__manufacture_dt,
                      self.__qty
                      ]
        create_file.flush_file(data, 'data/stock.csv')

    @staticmethod
    def get_products():
        read_file = Append()
        dump = read_file.load_file('data/stock.csv')
        products_list: list = []
        for item in dump:
            product: Products = Products(item[0],
                                         item[1],
                                         item[2],
                                         datetime.strptime(
                                             item[3], '%Y-%m-%d %H:%M:%S'
                                         ),
                                         item[4]
                                         )
            products_list.append(product)
        return products_list
