import random
import time

kullanicilar = list()


def kullaniciEkle (x):
    print('-'*30)
    print('Kullanici ekleme ekrani')
    ekle = input('Eklenecek kullaniciyi yaziniz:')
    kullanicilar.append(ekle)
    input('Devam etmek icin enter tusuna basiniz')

def kullaniciGor (x):
    print('-'*30)
    say=1
    for i in x:
        print(str(say)+'-Kullanici adi:',i)
        say+=1
    print('-'*30)
    input('Devam etmek icin enter tusuna basiniz')

def sec (x):
    say = 1
    kisiSec= int(input('Kac kisi secilsin ?: '))
    rastgeleSec = random.sample(x,kisiSec)
    for i in rastgeleSec:
        print(str(say)+'-Kullanici Adi:',i)
        say+=1
    print('-'*30)
    input('Devam etmek icin enter tusuna basiniz')

def salla(x):
    print('-'*30)
    say = 1
    random.shuffle(x)
    for i in x:
         print(str(say)+'-Kullanici adi:',i)
         say+=1
    print('-'*30)
    input('Devam etmek icin enter tusuna basiniz')

while True:
    print('**** Cekilis Uygulamasi ****')
    secim = int(input('1- Kullanici Ekle\n2- Kullanici Gor\n3- Kullanicilari Karistir\n4- Kullanici Sec\n'))
    
    if secim == 1:
        kullaniciEkle(kullanicilar)
    elif secim == 2:
        kullaniciGor(kullanicilar)
    elif secim==3:
        salla(kullanicilar)
    elif secim == 4:
        print('Kisi secme alani hesaplaniyor...')
        time.sleep(4)
        sec(kullanicilar)
    else:
        print('Yanlis secim yaptiniz')