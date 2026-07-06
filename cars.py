from io import BytesIO
import boto3
import pandas as pd


class Car:

    def __init__(self, make, year, price, mileage, image_url):
        self.make = make
        self.year = year
        self.price = price
        self.mileage = mileage
        self.image_url = image_url


def load_cars_from_s3():

    s3 = boto3.client("s3")

    response = s3.get_object(
        Bucket = "vehicles7614",
        Key = "cars.xlsx",
    )

    excel_file = BytesIO(response["Body"].read())
    df = pd.read_excel(excel_file)

    cars = []

    for _, row in df.iterrows():
        car = Car(
            make=row["make"],
            year=row["year"],
            price=row["price"],
            mileage=row["mileage"],
            image_url=row["image_url"]
        )
        cars.append(car)

    return cars

#Bypass import error for eb
try:
    cars = load_cars_from_s3()
except Exception as e:
    print(f"ERROR loading cars from S3: {e}", flush=True)
    cars = []
