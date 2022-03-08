class Manufacturer:
    def __init__(self, code: int, arrival_times: list[int],
                 prices: dict[int: [float]]):
        self.__code = code
        self.__arrival_times = self.custom_remove(arrival_times, None)
        self.__prices = {}
        prices = self.custom_remove(prices, None)
        for key in prices:
            if type(prices.get(key)) == list:
                self.__prices[key] = sum(prices.get(key)) / len(prices.get(key))
            else: self.__prices[key] = prices.get(key)

    def __str__(self):
        return f"Manufacturer:" \
               f"code = {self.__code}," \
               f"arrival_times = {self.__arrival_times}" \
               f"prices = {self.__prices}"

    def get_code(self):
        return self.__code

    def get_arrival_times(self):
        return self.__arrival_times

    def get_prices(self):
        return self.__prices

    def get_prices_for_year(self, year: int):
        if year in self.__prices.keys():
            return self.__prices.get(year)
        else:
            return None

    @staticmethod
    def custom_remove(origin, param):
        if param in origin:
            if type(origin) == dict:
                while param in origin:
                    origin.pop(None, None)
            else:
                while param in origin:
                    del origin[origin.index(param)]
        return origin
