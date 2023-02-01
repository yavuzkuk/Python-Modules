import os

# print(os.sep)
# windows işletim sisteminde \\ , linux ve MacOs işletim sistemlerinde /
# pathleri ayırmak için kullanılan ayırıcıdır

# print(os.name)
# windows işletim sisteminde 'nt', linux ve MacOs işletim sistemlerinde 'posix' değerlerini döndürür
# bu sayede hangi işletim sisteminde olduğumuzu görebiliriz

dizin  = os.getcwd()
# get current working directory(getcwd) ile içinde bulunulan dizini döndürür

# print(dizin)

print(os.listdir())
# içinde bulunulan dizinin dosyalarını ve klasörleri gösterir

print(os.curdir)
# current directory (curdir) ile içinde bulunulan dizini temsil eden "." işareti döndürür
# dizin ismini döndürmez!!
# "." içinde bulunulan dizine ulaşmak için kullanılır

print(os.pardir)
# parent directory (pardir) ile içinde bulunulan dizinin bir üst dizinini temsil eden ".." işaretini döndürür
# dizin ismini döndürmez!!
# ".." bir üst dizine ulaşmak için kullanılır

# print(os.listdir(os.pardir))
# pardir ile bir üst dizine ulaşılır ve listdir fonksiyonu ile
# üst dizinin içindeki klasörler ve dosyaları yazdırır

# os.startfile()
# içine girilen dosya çalışması gereken uygulamada çalışmaya başlar
# txt dosyaları -notepad vb.


# os.mkdir(os.path.join(os.getcwd(),"deneme"))
# os.mkdir ile dosya oluşturulmasını sağlar
# os.path.join() içine verilen iki parametre bir birine bağlandı yeni bir path oluşturuldu
# mkdir ile o dizine dosya oluşturuldu

# os.makedirs()
# var olmayan iç içe dosyaları oluşturmayı sağlar

# os.rename("dpzelt.txt","düzelt.txt")
# rename içine girilen 1. parametreyi 2. parametreye döndürür

# os.remove("sil.txt")
# remove() fonksiyonu ,dosyaları silmeye yarar




# print(os.path.abspath("osModule.py"))
# osModule.py dosyasının tam pathini döndürür

# os.path.dirname("osModule.py")
# osModule.py dosyasının dosya yolunu döndürür

# print(os.path.exists("osModule.py"))
# içine girilen path yada dosyanın var olup olmadığına bakar. true/false diye döndürür


# os.path.isdir()
# içine girilen dizinin yada dosyanın, klasör olup olmadığına bakar. true/false diye değer döndürür

# os.path.isfile()
# içine girilen dizinin yada dosyanın , dosya olup olmadığını bakar. true/false diye değer döndürür

# os.path.join()
# içine girilen dizini veya dosya isimlerini, os.sep fonksiyonundan dönen değere göre birleştirir



