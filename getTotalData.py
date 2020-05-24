import requests
import json
import time


countryopt = str(input("Do you want to search by country code (C) or country name (N) ?"))

if countryopt.upper() =="C":
    jsonValue = str(input("What is the country code:"))
    url = "https://covid-19-data.p.rapidapi.com/country/code"
    jsonKey = "code"


elif countryopt.upper() =="N":
    jsonValue = str(input("What is the country name:"))
    url = "https://covid-19-data.p.rapidapi.com/country"
    jsonKey = "name"   


querystring = {"format":"json",jsonKey:jsonValue}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "c8c114a5efmshff0ba887ed082d2p1100a0jsn2b06529cd9a9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
countries_data = response.text
getCountryData = json.loads(countries_data)
covid_data = getCountryData[0]
covid_confirmed = covid_data['confirmed']
covid_recovered = covid_data['recovered']
covid_critical = covid_data['critical']
covid_deaths = covid_data['deaths']
covid_country = covid_data['country']
covid_code = covid_data['code']
print(covid_country," Code: "+ covid_code,"  Confirmed: "+ str(covid_confirmed)," Critical: "+ str(covid_critical),"  Deaths: "+ str(covid_deaths)," Recovered: "+ str(covid_recovered))

"""
total_confirmed = 5398893
total_recovered = 2245684
total_critical = 53536
total_deaths = 343684
"""

time.sleep(2)

url = "https://covid-19-data.p.rapidapi.com/totals"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "c8c114a5efmshff0ba887ed082d2p1100a0jsn2b06529cd9a9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

world_data = response.text
getWorldData = json.loads(world_data)
covid_world_data = getWorldData[0]
total_confirmed = covid_world_data['confirmed']
total_recovered = covid_world_data['recovered']
total_critical = covid_world_data['critical']
total_deaths = covid_world_data['deaths']


total_percent = (covid_confirmed/total_confirmed)*100
total_death = (covid_deaths/total_deaths)*100
total_critic = (covid_critical/total_critical)*100
total_recover = (covid_recovered/total_recovered)*100
death_rate = (covid_deaths/covid_confirmed)*100
recovery_rate = (covid_recovered/covid_confirmed)*100

if(covid_confirmed>10000):
    print("Covid high impact area")
else:
    print("Covid low impact area")

if(covid_deaths > 5000):
    print("Death rate is higher in this country")
else:
    print("Death rate is lower in this country")

print("The percentage of the country's Covid-19 cases compared to the world's Covid-19 cases is" + " " + str(total_percent) + "% "+"as of May 23, 2020")
# Get covid total for entire world
print("The percentage of the country's Covid-19 related deaths compared to the world's Covid-19 related deaths is" + " " + str(total_death) + "% "+"as of May 23, 2020" )

print("The percentage of the country's Covid-19 critical cases compared to the world's Covid-19 critical cases is" + " " + str(total_critic) + "% "+"as of May 23, 2020")

print("The percentage of the country's Covid-19 recovered cases compared to the world's Covid-19 recovered cases is" + " " + str(total_recover) + "% "+"as of May 23, 2020")

print("The recovery rate in this country is" + " " + str(recovery_rate) + "% ")

print("The death rate in this country is" + " " + str(death_rate) + "% ")