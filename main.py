import requests


def get_nationality(name):
    url = f"https://api.nationalize.io/?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('country') is not None:
            country_code = data['country'][0]['country_id']
            probability = data['country'][0]['probability']
            return country_code, probability
        else:
            return "Nationality not found"
    else:
        return "Error fetching data"


name = input("Enter a name: ")
result = get_nationality(name)

if type(result) == tuple:
    country_code, probability = result
    print(f"The most probable nationality for {name} is {country_code} with a probability of {probability:.2f}")
else:
    print(result)
