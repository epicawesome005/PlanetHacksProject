import requests
import json

countryName = input("Enter the country name : ") 
print (countryName)

url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"format":"json","name":countryName}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "c8c114a5efmshff0ba887ed082d2p1100a0jsn2b06529cd9a9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
countries_data = response.text
print(countries_data)
getCountryData = json.loads(countries_data)
covid_data = getCountryData[0]
print(covid_data)
covid_confirmed = covid_data['confirmed']
covid_recovered = covid_data['recovered']
covid_critical = covid_data['critical']
covid_deaths = covid_data['deaths']

if(covid_deaths > covid_recovered):
    print("Death rate is higher in " + countryName)
else:
    print("Recovery rate is higher in " + countryName)

"""
print(covid_data['confirmed'])
print(covid_data['recovered'])
print(covid_data['critical'])
print(covid_data['deaths'])
print(covid_data['latitude'])
print(covid_data['longitude'])
print(covid_data['lastChange'])
print(covid_data['lastUpdate'])
"""