import requests
import json
import time

while 1==1:
    countryopt = str(input("Do you want to search by country code (C) or country name (N) ?"))
    if countryopt.upper()=='C' or countryopt.upper()=='N':
        break

url = "https://covid-19-data.p.rapidapi.com/help/countries"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "44efa3aff1msh3eea9d7a9e96681p1c8e0bjsn9f06ccff323e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

countriesList_data = response.text
getCountryListData = json.loads(countriesList_data)

getCountryCodeList = []
getCountryNameList = []

for countryDtl in getCountryListData:
    countryCode=countryDtl['alpha3code']
    countryName=countryDtl['name']
    getCountryCodeList.append(countryCode)
    getCountryNameList.append(countryName.upper())


if countryopt.upper() =="C":
    print("Choose Country Code from below:\n")
    print(getCountryCodeList)
    while 1==1:
        jsonValue = str(input("What is the country code:"))

        if jsonValue.upper() in getCountryCodeList:
            break

    url = "https://covid-19-data.p.rapidapi.com/country/code"
    jsonKey = "code"


if countryopt.upper() =="N":
    print("Choose Country Name from below:\n")
    print("getCountryCodeName:", getCountryNameList)
    while 1==1:
        jsonValue = str(input("What is the country name:"))

        if jsonValue.upper() in getCountryNameList:
            break

    url = "https://covid-19-data.p.rapidapi.com/country"
    jsonKey = "name"


querystring = {"format":"json",jsonKey:jsonValue}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "c8c114a5efmshff0ba887ed082d2p1100a0jsn2b06529cd9a9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
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

time.sleep(2)

url = "https://covid-19-data.p.rapidapi.com/totals"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "c8c114a5efmshff0ba887ed082d2p1100a0jsn2b06529cd9a9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)



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
    print("Death rate is high in this country")
else:
    print("Death rate is low in this country")

print("The percentage of the country's Covid-19 cases compared to the world's Covid-19 cases is" + " " + str(total_percent) + " % ")

print("The percentage of the country's Covid-19 related deaths compared to the world's Covid-19 related deaths is" + " " + str(total_death) + " % ")

print("The percentage of the country's Covid-19 critical cases compared to the world's Covid-19 critical cases is" + " " + str(total_critic) + " % ")

print("The percentage of the country's Covid-19 recovered cases compared to the world's Covid-19 recovered cases is" + " " + str(total_recover) + " % ")

print("The recovery rate in this country is" + " " + str(recovery_rate) + " % ")

print("The death rate in this country is" + " " + str(death_rate) + " % ")

print("ALL DATA FROM RAPID API")

