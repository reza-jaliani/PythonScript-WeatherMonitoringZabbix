#!/usr/bin/env python3
import requests
import sys

API_KEY = <"YOUR_API_KEY">
CITY = <"YOUR_CITY_NAME">
COUNTRY = <"YOUR_COUNTRY_NAME">
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"

def get_temperature():
        try:
                response = requests.get(URL, timeout=10)
                response.raise_for_status()
                data = response.json()
                temperature = data['main']['temp']
                return temperature
        except requests.exceptions.RequestException as e:
                print(f"Error: {e}",file=sys.stderr)
                return None
        except KeyError:
                print("Error: Invalid response format", file=sys.stderr)
                return None

def main():
        temperature = get_temperature()
        if temperature is not None:
                print(temperature)
        else:
                print(0,0)
                sys.exit(1)

if __name__ == "__main__":
        main()
