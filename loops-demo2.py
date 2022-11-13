#sayı tahmin uygulaması


import random

sayi = random.randint(10,100)


hak = 5

while hak > 0:
    hak-=1
    x = int(input("Sayıyı tahmin edin: "))
    if(sayi > x):
        print("Yukarı")
    elif(sayi == x):
        print("Sayıyı bildiniz.")
        break
    else:
        print("Aşağı")    

if (hak == 0):
    print(f"Hakkınız kalmadı:(:( tutulan sayı {sayi}")            
     