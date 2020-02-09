import csv

def get_airports_coords(airport_code):
	flag = False
	with open('airport-codes.csv', encoding="utf8") as airports:
		csv_reader = csv.reader(airports)
		for line in csv_reader:
			if line[0] == airport_code or line[9] == airport_code:
				flag = True
				return line[11]

	if flag == False:
		return "Error"

print(get_airports_coords("OOMA"))