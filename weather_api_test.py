import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

api_url = "https://api.openweathermap.org/data/2.5/weather"

def test_status_code_200():

    p = {"q":"London", "appid": api_key}
    try:
        response = requests.get(api_url, params=p)

        assert response.status_code, 200
        print("test_status_code_200 is passed")

    except requests.exceptions.RequestException as e:
        print(e)
        print("Error: Your URL is invalid")

@pytest.mark.script1
def test_by_city_name():
    city_name = "Kyiv"
    p = {"q":city_name,"appid": api_key}

    try:
        response = requests.get(api_url, params=p)
        json = response.json()

        actual = json["name"]
        assert actual, city_name
        print("test_by_city_name is passed")

    except requests.exceptions.RequestException as e:
        print(e)
        print("Error: Your URL is invalid")

@pytest.mark.script2
def test_by_lat_lon():
    coord = {
        "lon": 30.5167,
        "lat": 50.4333
    }

    p = {"lat":  coord['lat'], "lon": coord["lon"], "appid": api_key}
    try:
        response = requests.get(api_url, params=p)
        json = response.json()

        actual = json['coord']
        assert actual, coord
        print("test_by_lat_lon is passed")

    except requests.exceptions.RequestException as e:
        print(e)
        print("Error: Your URL is invalid")

@pytest.mark.script3
def test_by_zip_code():
    zip_code = 94040
    p = {"zip": zip_code, "appid": api_key}
    try:
        response = requests.get(api_url, params=p)
        json = response.json()

        expected = "Mountain View"
        actual = json['name']
        assert actual, expected
        print("test_by_zip_code is passed")

    except requests.exceptions.RequestException as e:
        print(e)
        print("Error: Your URL is invalid")