import csv
from get_airports_coords import get_airports_coords

def test_get_airports_coords_1():
	assert get_airports_coords("BOS") == "42.36429977, -71.00520325"

def test_get_airports_coords_2():
	assert get_airports_coords("KBOS") == "42.36429977, -71.00520325"

def test_get_airports_coords_3():
	assert get_airports_coords("BEY") == "33.820899963378906, 35.488399505615234"
	
def test_get_airports_coords_4():
	assert get_airports_coords("CDG") == "49.012798, 2.55"
	
def test_get_airports_coords_5():
	assert get_airports_coords("OOMA") == "20.675399780273438, 58.890499114990234"

def test_get_airports_coords_6():
	assert get_airports_coords(" ") == "Error"
	
def test_get_airports_coords_6():
	assert get_airports_coords("Boston") == "Error"
