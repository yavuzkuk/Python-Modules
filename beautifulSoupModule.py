from bs4 import BeautifulSoup
import requests

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python BeatifulSoup</title>
</head>
<body>
    <h1>Mehaba Python Kursiyerleri</h1>

    <div>
        <h2>Kurs 1</h2>
        <ul>
            <li>Menü 1.1</li>
            <li>Menü 1.2</li>
            <li>Menü 1.3</li>
        </ul>
    </div>

    <div>
        <h2>Kurs 2</h2>
        <ul>
            <li>Menü 2.1</li>
            <li>Menü 2.2</li>
            <li>Menü 2.3</li>
        </ul>

    </div>

    <a href="https://www.google1.com"></a>
    <a href="https://www.google2.com"></a>
    <a href="https://www.google3.com"></a>


</body>
</html>
"""

# kendimiz bir html içeriği kopyalaıp yapıştırabileceğimiz gibi
# request modülü ile de html içeriğini alabiliriz

# content = requests.get("https://www.google.com")
# content = content.text
# Google'un html dökümanına eriştik ilerleyen süreçte bu html dökümanı üzerinden etiketlere erişebiliriz


content = BeautifulSoup(html_doc,"html.parser")
# BeautiflSoup içine parametre olarak html kaynak kodumuzu verdik
# ikinci parametre olarak ise kaynak kodunu neye göre parçalicağını belirttik


result = content.prettify()
# prettify() metodu ile kaynak kodunda ki girdi hatalarını düzeltti


result = content.body
result = content.head
# html dosyasının içinden istediğmiz etikete .body , .head , .title vb. diye erişebiliyoruz

result = content.title.string
# ama .title dediğimiz zaman html etiketleri ile birlikte gelmekte
# .title.string yaptığımız zaman içindeki yazıya erişmiş oluruz
result = content.h1.string


# bulunmasını istediğimiz etiketten kaynağın içinde birden fazla olabilir
# bu yüzden findAll() fonksiyonu kullanılır ve içine bir etiket ismi verilir.
# bu fonksiyon bulduğu cevapları bir liste halinde saklar

# result = content.findAll("h2")
# result = result[0].string
# result = result[1].string

result = content.find("div")
# bütün div etiketlerini bir listeye atar

result = content.findAll("div")[1]
# bütün div etiketleri arasından 1.indexli div etiketini result değişkenine atar

result = content.findAll("div")[1].ul.li
# 1.indexli divin içindeki ul etiketini içindeki ilk li etiketine result değişkenine atar

result = content.findAll("a")

print(result)

# allText = content.get_text()
# get_text() fonksiyonu ise sayfadaki bütün metinleri elde etmemize yarar
#
# print(allText)

# for link in result:
#     print(link)
#     print(link.get("href"))
# get metodu ile etiketin istediğimiz özelliğine erişebiliriz





