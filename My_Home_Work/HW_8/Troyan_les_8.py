# Класс родитель
class CarsStat():

    """В этом классе будут приведены характеристики авто"""

    def __init__(self, speed, brand):
        """Скорость и марка"""
        self.speed = speed
        self.brand = brand

    def release(self):

        """Максимальная скорость"""

        print(
            "Машина под названием " + self.brand +
            " с максимальной скоростью " + str(self.speed) +
            " Продана "
        )

    def on_the_run(self):

        print("BMW Машина на ходу")

# Класс наследник


class CountryCarsStat(CarsStat):
    """Страна производитель"""

    def __init__(self, country, brand):
        """Эта функуия дополняет страну"""
        super().__init__(self, brand)
        self.country = country

    def on_the_run(self):
        print("AUDI Машина на ходу")


Country1 = CountryCarsStat("Germany", None)
print("Страна производитель " + Country1.country)
cars1 = CarsStat(260, "BMW")
cars2 = CarsStat(255, "AUDI")
cars1.on_the_run()
Car2Country = CountryCarsStat("Germany", "AUDI")
print(Car2Country.on_the_run())
cars1.release()
cars2.release()
