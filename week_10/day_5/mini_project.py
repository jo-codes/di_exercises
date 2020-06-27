from pyowm.owm import OWM
owm = OWM('9c187cc9a10d9712216b0ee1d25c92a5')
reg = owm.city_id_registry()


city_to_search = input("Pick a city, any city: ").title().strip()
country_code = input("Gimme a country code: ").upper().strip()

list_of_tuples = city = reg.ids_for(city_to_search, country=country_code)
city_to_check = list_of_tuples[0][0]

mgr = owm.weather_manager()
observation = mgr.weather_at_id(city_to_check)
weather = observation.weather
wind_mph = weather.wind(unit="miles_hour")["speed"]
sunrise = weather.sunrise_time(timeformat="iso")
sunset = weather.sunset_time(timeformat="iso")
forecast = mgr.forecast_at_id(city_to_check, '3h').forecast

# The preferred method for working with owm is with a city ID. This did not work for lat and lon. I therefore took user input and searched for location saving it to another variable. It seems extra, and it is, but the docs weren't too great.

list_of_locations = reg.locations_for(city_to_search, country=country_code)
non_id_loc_for_coi = list_of_locations[0]
lat = non_id_loc_for_coi.lat
lon = non_id_loc_for_coi.lon

# with lat and lon successfully fetched, the below should work. running dir on it shows not coindex_anything properties, just a pollution manager with zero documentation


# coi = owm.coindex_around_coords(lat, lon)


print(f"\nYour city ID is: {city_to_check}, not that you asked... \n")

print(f"Currently the weather is: {weather.status} \n")
print(f"Currently the wind speed is: {wind_mph} mph \n")
print(f"Sunrise is at {sunrise}, sunset is at {sunset} \n")

print("Your forecast below... \n\n")

for weather in forecast:
    print(weather.reference_time("iso"), weather.status)


# print(f"\n\nThe CO index is {coi} ")


print("\n\nPretty cool huh? \n")
