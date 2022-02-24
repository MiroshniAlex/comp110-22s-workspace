"""Dictionaries."""


# Declaring type of dict
schools: dict[str, int]

schools = dict()

# Set a key-value paring
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150


# Prints literal representation
print(schools)

# Access value by key.
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from dict
schools.pop("Duke")

# Test the existence of key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update/Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Empty literal dict
schools = {}

# initialize key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150
}

for key in schools:
    print(f"Key: {key}, {schools[key]}")