# creating a dictionary
state_capitals = {"Tamilnadu": "Chennai","Kerala": "Thiruvananthapuram", "Goa": "Panaji"}
  
# printing the dictionary
print(state_capitals)

# access the value of keys
print(state_capitals["Tamilnadu"])    # Output: Chennai
print(state_capitals["Goa"])    # Output: Panajai

# add an item with "West Bengal" as key and "Kolkata" as its value
state_capitals["West Bengal"] = "kolkata"
print(state_capitals)

# delete item having "Goa" key
del state_capitals["Goa"]
print(state_capitals)
