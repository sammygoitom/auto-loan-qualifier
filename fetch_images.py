import requests
import pandas as pd
import time

API_KEY = "****"

df = pd.read_excel("cars.xlsx")


def get_image_url(make, year):
    params = {
        "engine": "google_images",
        "q": f"{year} {make} car",
        "api_key": API_KEY,
        "num": 1
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    try:
        return data["images_results"][0]["original"]
    except (KeyError, IndexError):
        return ""


image_urls = []
for _, row in df.iterrows():
    url = get_image_url(row["make"], row["year"])
    print(f"{row['year']} {row['make']} → {url}")
    image_urls.append(url)
    time.sleep(1)

df["image_url"] = image_urls
df.to_excel("cars.xlsx", index=False)
print("done")