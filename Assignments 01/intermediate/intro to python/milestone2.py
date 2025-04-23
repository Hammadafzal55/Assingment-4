# ===  All Planets ===
# planetaryweight.py

# Gravitational constants (as a fraction of Earth's gravity)
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Input from user
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Lookup and calculate weight
if planet in gravity_factors:
    planet_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"The equivalent weight on {planet}: {planet_weight}")
else:
    print("That planet is not in the list!")
