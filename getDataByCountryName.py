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

total_confirmed = 5398893
total_recovered = 2245684
total_critical = 53536
total_deaths = 343684

total_percent = (covid_confirmed/total_confirmed)*100
total_death = (covid_deaths/total_deaths)*100
total_critic = (covid_critical/total_critical)*100
total_recover = (covid_recovered/total_recovered)*100

if(covid_confirmed>10000):
    print("Covid high impact area")
else:
    print("Covid low impact area")
    
if(covid_deaths > 5000):
    print("Death rate is higher in" + countryName)
else:
    print("Death rate is lower in" + " " + countryName)

print("The percentage of the country's Covid-19 cases compared to the world's Covid-19 cases is" + " " + str(total_percent) + "%")
# Get covid total for entire world
print("The percentage of the country's Covid-19 related deaths compared to the world's Covid-19 related death is" + " " + str(total_death) + "%" )

print("The percentage of the country's Covid-19 critical cases compared to the world's Covid-19 critical cases is" + " " + str(total_critic) + "%")

print("The percentage of the country's Covid-19 recovered cases compared to the world's Covid-19 recovered cases is" + " " + str(total_recover) + "%")