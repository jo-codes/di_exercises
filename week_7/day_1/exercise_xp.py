# Exercise 1

#     Below are the two lists convert it into the dictionary
#     Hint: Use the zip method

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# # Expected output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# result = dict(zip(keys, values))
# print(result)


# Exercise 2

#     Create a dictionary called store. Inside this variable, translate this information into keys and values

store = {"name": "Zara",
         "creation_date": 1975,
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"],
         "number_stores": 7000,
         "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}}


# Change the number of stores to 2

store["number_stores"] = 2

# Print a sentence that explains who the clients of Zara are


# print("The clients of Zara are people who buy things sometimes and like Zara?")


# Add country_creation: Spain to the dictionary (it’s a new key)

store["country_creation"] = "Spain"

# If the key international_competitors is in the dictionary, add the store Desigual

store["international_competitors"].append("Desigual")

# Delete the information about the date of creation

del(store["creation_date"])

# Print the last international competitor

# last_competitor = store["international_competitors"].pop()
# print(last_competitor)

# Print in a sentence, the major colors in the US

major_us_color = store["major_color"]["US"]
# print(f"{major_us_color}")

# Print the length of the dictionary

# print(f"{len(store)}")

# Print the keys of the dictionary

# for key, value in store.items():
#   print(key)

# Create another dictionary called more_on_store with this information

more_on_store = {"creation_date": 1975,
                 "number_stores": 10000}

store.update(more_on_store)

print(store)
