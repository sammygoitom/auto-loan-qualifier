import pandas as pd


class Car:

    def __init__(self, make, year, price, mileage, image_url):
        self.make = make
        self.year = year
        self.price = price
        self.mileage = mileage
        self.image_url = image_url


df = pd.read_excel("cars.xlsx")

# Pandas loops through every row given the template for what properties each car
# has, then adds each car object to a list
cars = []

for _, row in df.iterrows():
    car = Car(make=row["make"], year=row["year"], price=row["price"], mileage=row["mileage"], image_url=row["image_url"])
    cars.append(car)
