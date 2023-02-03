import mouse


# mouse.click("right")
# click metodu içine girilen right metodu ile sağ click yapılır

# mouse.click("left")
# click metodu içine girilen left metodu ile sol click yapılır

# mouse.click("middle")

# mouse.press("left")
# parametre olarak girilen tuşa basar


print(mouse.get_position())
# get_position metodu, mouse'un pozisyonunu geri döndürür

# mouse.drag(0,0,200,200,absolute=False,duration=0.1)
# eğer absolute değeri true ise ekranın en sol üstünden başlar
# ve 3 ve 4. değerlere göre ilerleme gösterir

# eğer absolute değeri false ise farenin bulunduğu noktadan işleme başlar
#bulunduğu noktayı 0,0 alarak 3. parametreyi x ekseni, 4.parametreyi y ekseni olarak alır

# mouse.hold("right")
#print(mouse.is_pressed("right"))
# herhangi bir tuşa basılıp basılmadığını sorgular


# mouse.move(100, 100, absolute=False, duration=0.2)
# mouse.move'da ,mouse.drag gibi imleci hareket ettirmek için kullanılır
# aralarında ki fark: move fonksiyonunda herhangi bir tuşa basılmaz iken, drag fonksiyonunda tuşa basılı bir şekilde hareket eder.


mouse.wheel(2)
mouse.wheel(-4)

# whell fonksiyonu ile bulunduğumuz yerde yukarı aşşağı kaydırabilirsiniz.
# içine verdiğiniz parametrenin - yada + olması gidilen yönü belirler

# event = mouse.record()
# sağ click yapılıncaya kadar kayıt etmeye devam eder
# keyboard modülünde de olduğu gibi record fonksiyonu ile mouse hareketleri kayıt ediliyor


# print(mouse.play(event))
# play metodu ile kayıt başlatılıyor
# içine parametre olarak girilen speed_factor ile oynatma hızı ayarlanır
