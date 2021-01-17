import requests
from pprint import pprint
def weather_data(query):

	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();

def print_weather(result,cityName):
	print("{}'s sää on: {}°C astetta ".format(cityName,result['main']['temp']))
	print("Tuuli: {} m/s ".format(result['wind']['speed']))
	print("Kuvaus: {}".format(result['weather'][0]['description']))
	print("Sää tyyppi: {}".format(result['weather'][0]['main']))

def main():
	cityName=input('Anna kaupunki: ')
	print()
	try:
	  query='q='+cityName;
	  w_data=weather_data(query);
	  print_weather(w_data, cityName)
	  print()
	except:

	  print('Sellaista ei löydy....')

if __name__=='__main__':
	main()

########################
#Toiminassa tapahtuu vain kun syötät kaupungin nimen mukaan ja analysoi TÄMÄN hetkisen sään asteikkon celsius
#Sitä ei voi analysoida mm. seuraavan tunnin tapahtuman tai päivän tulevien sää ennustamisen
####Output:: 
#Anna kaupunki: Oslo
#Oslo's sää on: -8.46°C astetta 
#Tuuli: 0.57 m/s 
#Kuvaus: overcast clouds
#Sää tyyppi: Clouds
##
