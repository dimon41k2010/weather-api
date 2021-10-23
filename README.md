# weather-api
Test project to test weather APIs

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install libs.

```bash
pip install -r requirements.txt
```

You need to create a file .env where you store [api key](https://openweathermap.org/current):

```bash
API_KEY = {API key}
```

## Usage

To execute all pytest tests run command:

```bash
pytest weather_api_test.py 
```

or if you don't have enironmental variables set up run:

```bash
python3 -m pytest weather_api_test.py 
```

To generate HTML and XML reports run command:

```bash
pytest weather_api_test.py -rA --html=MyHTML_API_Jokes_Result.html 
pytest weather_api_test.py -rA --junitxml=MyXML_API_Jokes_Result.xml
```
To execute tests separately with reports run commands accordingly:
    script1: Run test by city name.
    script2: Run test by latitude and longitude.
    script3: Run test by ZIP code.

```bash
pytest weather_api_test.py -k script1
pytest weather_api_test.py -k script2
pytest weather_api_test.py -k script3
```
