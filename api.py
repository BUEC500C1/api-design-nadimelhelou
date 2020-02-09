# Nadim El Helou - EC 500 C1 - HW2 Weather API

# References: 
# Airports dataset: https://github.com/datasets/airport-codes
# Creating an API: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#installing-python-and-flask
# Weather API documentation: https://openweathermap.org/api

import flask
from flask import request, jsonify
import csv
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Airport Weather API</h1><p>This API returns the current weather at a given airport. By Nadim El Helou</p>"


@app.route('/weather', methods=['GET'])
def api_id():
    # Check if an airport code was provided in the URL.
    if 'iata' in request.args:
        airport_code = request.args['iata']
    elif 'icao' in request.args:
    	airport_code = request.args['icao']
    else:
        return "Error: No code provided. Please enter the IATA (3 letter code) or the ICAO (4 letter code) code of the desired airport."

    # flag to signal if the airport code provided is valid/exists
    flag = False

    # Loop through the airport data to find the coordinates of the requested airport.
    with open('airport-codes.csv', encoding="utf8") as airports:
    	csv_reader = csv.reader(airports)
    	for line in csv_reader:
    		if line[0] == airport_code or line[9] == airport_code:
    			flag = True
    			coord = line[11]
    			coord = coord.split(', ')
    			latitude = coord[0]
    			longitude = coord[1]
    
    # Call weather API if airport coordinates were successfully found
    if (flag == True):
    	url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&APPID=4c67e7c09a136bce71be5999f76593cc"
    	data = requests.get(url).json()
    	
    	# return data
    	temp = round(data["main"]["temp"] - 273, 2)
    	feels_like = round(data["main"]["feels_like"] - 273, 2)
    	city = data["name"]
    	description = data["weather"][0]["description"]
    	pressure = data["main"]["pressure"]
    	humidity = data["main"]["humidity"]
    	wind_speed = data["wind"]["speed"]
    	return "The weather in " + city + " is " + description + " with temperature " + str(temp) + " ºC (feels like " + str(feels_like) + " ºC). Wind speed: " + str(wind_speed) + " m/s. Humidity: " + str(humidity) + "%. Pressure: " + str(pressure) + " hpa."
    else:
    	return "Invalid IATA/ICAO code"

        
app.run()

