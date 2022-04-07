# windchill.py
# some functions to work with the Windchill calculator to make sure
# inputs are correct and the calculation works as well as displaying
# the output in a well-formatted display

def get_results(temp, speed):
    """ returns the results of trying to calculate wind chill """
    temp = get_temp(temp)
    wind = get_wind_speed(speed)

    # check for warnings
    if "Warning" in temp:
        return temp
    if "Warning" in wind:
        return wind

    # We can safely process Wind chill factor
    temp = int(temp)
    wind = int(wind)
    windchill = get_wind_chill(temp, wind)

    results = "A temperature of {}F ".format(temp)
    results += "and a wind speed of {}mph ".format(wind)
    results += "feels like {}F.".format(windchill)
    return results

def get_temp(temp):
    """ receives a temp (str) and returns an integer or error message """
    if not temp:
        return "Warning: Temperature was missing."

    # if there are no errors (convert to int)
    try:
        temp = int(temp)
        if temp > 50:
            return "Warning: Your temperature must be below 50 degress."
        else:
            return str(temp)
    except ValueError:
        return "Warning: You must enter a number for your temperature."


def get_wind_speed(speed):
    """ receives a speed (str) and returns a number or error message """
    if not speed:
        return "Warning: Wind Speed was missing."

    # if there are no errors (convert to int)
    try:
        speed = int(speed)
        if speed < 0:
            return "Warning: Your windspeed must be greater than 3 mph."
        else:
            return str(speed)
    except ValueError:
        return "Warning: You must enter a number for the wind speed."

def get_wind_chill(t, s):
    """Calculate wind chill """
    bmi = 35.74 + 0.6215 * t - 35.75 * s**0.16 + 0.4275 * t * s**0.16
    return int(round(bmi))