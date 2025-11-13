import os, requests


key = os.getenv("API_KEY")



def get_weather() -> None:
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={"key": key, "q": "Paris"}
    )

    data = response.json()

    print(f"Current weather in {data["location"]["name"]} is "
          f"{data["current"]["temp_c"]}°C")


if __name__ == "__main__":
    get_weather()
