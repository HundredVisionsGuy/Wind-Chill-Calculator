import pytest
import windchill

def test_get_temp_for_0():
    expected = "0"
    results = windchill.get_temp("0")
    assert expected == results

def test_get_temp_for_empty_string():
    expected = "Warning: Temperature was missing."
    results = windchill.get_temp("")
    assert expected == results

def test_get_temp_for_negative_5():
    expected = "-5"
    results = windchill.get_temp("-5")
    assert expected == results

def test_get_temp_for_incorrect_string():
    expected = "Warning: You must enter a number for your temperature."
    results = windchill.get_temp("eg")
    assert expected == results

def test_get_temp_for_out_of_range():
    expected = "Warning: Your temperature must be below 50 degress."
    results = windchill.get_temp("55")
    assert expected == results

def test_get_wind_speed_for_empty():
    expected = "Warning: Wind Speed was missing."
    results = windchill.get_wind_speed("")
    assert expected == results

def test_get_wind_speed_for_non_numbers():
    expected = "Warning: You must enter a number for the wind speed."
    results = windchill.get_wind_speed("asd")
    assert expected == results

def test_get_wind_speed_for_below_range():
    expected = "Warning: Your windspeed must be greater than 3 mph."
    results = windchill.get_wind_speed("-1")
    assert expected == results

def test_get_wind_chill_for_16_10_4():
    expected = 4
    results = windchill.get_wind_chill(16, 10)
    assert expected == results

def test_get_wind_chill_for_neg60_50_neg116():
    expected = -116
    results = windchill.get_wind_chill(-60, 50)
    assert expected == results