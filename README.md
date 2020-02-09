# Airport Weather API
api-design-nadimelhelou created by GitHub Classroom

by Nadim El Helou

## Summary
This API returns a JSON object of the current weather at a desired airport.
It can receive as input either the IATA airport code, a three-letter code which is used in passenger reservation, ticketing and baggage-handling systems, or the ICAO airport code which is a four letter code used by ATC systems and for airports that do not have an IATA airport code.

## Running
In the terminal, run `python api.py` and you should see an output similar to: `Running on http://127.0.0.1:5000/`.

Enter the displayed url into your browser and you will be taken to the API home page. In order to input an airport, add the following path to the url `/weather`, then either the IATA or the ICAO code as such:
* `http://127.0.0.1:5000/weather?iata=CDG` if you wish to enter an IATA code (this will return the weather at Paris Charles de Gaulle Airport)
* `http://127.0.0.1:5000/weather?icao=KBOS` if you wish to enter an IATA code (this will return the weather at Boston Logan International Airport)
