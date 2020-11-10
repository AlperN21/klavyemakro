#Burada da https://github.com/AlperN21/MouseMakro da olduğu gibi klavyeyi dinliyeceğiz.
import keyboard #Klavye kütüphanesi
import time #Zaman k

keyboard.start_recording() #Klavyeyi dinliyoruz
ksüre = int(input("Klavye kaydı kaç saniye sürsün----->"))
print("Kayıt başlatılıyor!")
print("3")
print("2")
print("1")
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/4))#str a çeviriyoruzki cümle içinde olsun aksi takdir de olmaz.
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/3))
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/2))
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/1))
time.sleep(ksüre)
print("KAYIT TAMAMLANDI!")
time.sleep(1)
kayıtlar = keyboard.stop_recording() #Dinlemeyi durduyoruz.
print("KAYIT BAŞARILI! KAYIT BAŞLATILIYOR.")
keyboard.replay(kayıtlar)#Kayıtları başlatıyoruz.