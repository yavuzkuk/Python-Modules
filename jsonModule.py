import json


# dictionary

kisisel = {"name":"Yavuz","surname":"Kuk","age":20,"city":"Samsun"}

# print(type(kisisel))
# print(kisisel["name"])
# print(kisisel["surname"])
# print(kisisel["city"])
# json formatı dictionarye benzer yapıdadır


# json formatı string bir dictionary olarak da düşünebilir.

kisisel2 = '{"name":"Yavuz","surname":"Kuk","age":20,"language":["C","Java","Python"]}'

# sonuc = json.loads(kisisel2)
# json modülünde bulunulan loads fonksiyonu ile json veri tipini parçaladık
# dictionary de kullandığımız şekilde ulaşabiliyoruz

# print(sonuc["name"])
# print(type(kisisel2))
# print(sonuc["name"])
# print(sonuc["surname"])
# print(sonuc["language"][2])


# json uzantılı bir dosyanın va olduğunu düşünelim ve içinde yukarıda ki bilgilerin aynısı olsun

# with open("kisiselDeneme.json","r") as file:
#     sonuc3 = json.load(file)
#     print(sonuc3)
    # isterseniz tek seferde bütün bilgiyi de yazdırabilirsiniz

    # print(sonuc3["name"])
    # print(sonuc3["surname"])
    # print(sonuc3["age"])

# loads() fonksiyonu string bir veriyi işlemek için kullanılır
# load() fonksiyonu ise string olmayan veriyi işlemek için kullanılır




# dictionary olan bir veriyi json çevirmek için ise dumps() metodu kullanılır

kisisel_dict = {"name":"Yavuz","surname":"Kuk","age":20,"language":["C","Java","Python"]}

# sonuc4 = json.dumps(kisisel_dict)
# print(type(sonuc4))

# type'ını yazdırdığımız zaman string olduğunu gördük

#with open("kisiselDeneme.json") as file:
#    json.dump(sonuc4,file)

# dosyanın içine json veri tipinde bilgi yazdık



result2 = json.dumps(kisisel_dict,indent=2)

print(result2)

print(type(result2))

# format olarak girintili çıkıntılı bir şey istediğimiz de dumps() fonksiyonunun indent parametresine bir değer vermemiz yeterli

