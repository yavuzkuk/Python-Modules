# pip install keyboard
# cmd üzerinden keyboard modülü yüklendi

import keyboard


keyboard.add_hotkey("ctrl+a",lambda :print("Bütün dosyalar seçildi"))
keyboard.add_hotkey("ctrl+s",lambda :print("Dosya kayıt edildi"))
# add_hotkey() 1. parametre olarak verilen tuşlara basıldığında 2. parametredeki fonksiyon yapılır

# keyboard.press_and_release("p")
# içine parametre olarak verilen tuşa basılır ve bırakır

# keyboard.send("ğ")
# send() metodu , press_and_release() metodu gibi bir tuşa basıp bırakmayı sağlar



# keyboard.press("ş")
# içine parametre olarak verilen tuşa basılır

# print(keyboard.is_pressed("a"))
# herhangi bir tuşun basılıp basılmadığını true/false şeklinde geri döndürür

keyboard.write("Github: yavuzkuk")
# write() fonksiyonu ile içine girilen cümle yada kelimeleri yazdırmak için kullanılır

keyboard.write("Linkedin: yavuzkuk",delay=0.2)
# write() fonksiyonu içine girilen delay parametresi ile yazının yazılma hızını ayarlar

print("Çıkış için ctrl tuşlarına basın")
record = keyboard.record("ctrl")

keyboard.play(record, speed_factor=0.9)
# record() ve play() fonksiyonları sayesinde kullanıcı tarafından girilen tuşları kayıt eden fonksiyonlar
# play() içine girilen opsiyonel speed_factor ile hızı değiştirebiliriz

#içine verilen tuşa basılana kadar programı durduran fonksiyon
keyboard.wait("esc")
print("Program durdu")
