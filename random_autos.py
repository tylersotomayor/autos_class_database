import random

MAKES = ["Audi", "BMW", "Chevrolet", "Chrysler", "Dodge", "GMC", "Hyundai", "Jeep", "Mercedes-Benz", "Ram", "Toyota",
         "Volkswagen"]
MODELS = {
    "Audi": ["A3", "A4", "A5", "A6", "Q3", "Q5", "Q7"],
    "BMW": ["2 Series", "3 Series", "4 Series", "5 Series", "6 Series", "X3", "X5"],
    "Chevrolet": ["Camaro", "Colorado", "Corvette", "Equinox", "Impala", "Malibu", "Silverado"],
    "Chrysler": ["200", "300", "Pacifica", "Town & Country", "Voyager"],
    "Dodge": ["Challenger", "Charger", "Durango", "Grand Caravan", "Journey", "Ram 1500", "Ram 2500"],
    "GMC": ["Acadia", "Canyon", "Sierra 1500", "Sierra 2500HD", "Terrain", "Yukon"],
    "Hyundai": ["Accent", "Elantra", "Genesis", "Santa Fe", "Sonata", "Tucson", "Veloster"],
    "Jeep": ["Cherokee", "Compass", "Grand Cherokee", "Renegade", "Wrangler"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLA-Class", "GLC-Class", "GLE-Class", "GLS-Class", "S-Class"],
    "Ram": ["1500", "2500", "3500", "Promaster City", "Promaster"],
    "Toyota": ["4Runner", "Camry", "Corolla", "Highlander", "Prius", "RAV4", "Tacoma"],
    "Volkswagen": ["Atlas", "Beetle", "Golf", "Jetta", "Passat", "Tiguan", "Touareg"]
}


def generate_random_autos(num_autos):
    autos_data = []
    for i in range(num_autos):
        make = random.choice(MAKES)
        model = random.choice(MODELS[make])
        year = random.randint(1990, 2023)
        fuel_economy = round(random.uniform(10, 50), 1)
        price = round(random.uniform(5000, 50000), 2)
        vin = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=17))
        auto = {"vin": vin, "make": make, "model": model, "year": year, "fuel_economy": fuel_economy, "price": price}
        autos_data.append(auto)
    return autos_data


# Example usage: generate 100 autos and print the data
autos_data = generate_random_autos(100)
print(autos_data)
