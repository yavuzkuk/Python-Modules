import requests
import json

api_url = "https://v6.exchangerate-api.com/v6/1fc6757f5fe281e9aac65bc8/latest/"



bozulan_doviz = input("Bozmak istediginiz dövizi girin")
istenen_doviz = input("Donüştürmek istediginiz dövizi girin")
miktar = int(input("Ne kadar "+ bozulan_doviz + " bozdurmak istersiniz?"))

api_url = api_url+bozulan_doviz

x = requests.get(api_url)

x = json.loads(x.text)


print(istenen_doviz + " deger:  "+str(x["conversion_rates"][istenen_doviz]))
print(f"{x['conversion_rates'][istenen_doviz]} x {miktar} => {x['conversion_rates'][istenen_doviz] * miktar} {istenen_doviz}")
