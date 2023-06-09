import random
import time

def bonus() :
    choice = "N"
    print("Çarpan Katlayan Belirleniyor...")
    time.sleep(1)
    print(random.randint(1,5),random.randint(1,5),random.randint(1,5),random.randint(1,5),random.randint(1,5))
    time.sleep(1)
    carpan_kat = random.randint(1,5)
    print("Çarpan Katlayan:",carpan_kat)
    if carpan_kat != 5 :
        choice = input("Son Kez Çevir? 0 Gelme Şansi Bulunur (Y|N): ")
    else :
        time.sleep(1)

    if choice == "Y" or choice == "y" :
        time.sleep(1)
        print(random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5))
        time.sleep(1)
        carpan_kat = random.randint(0,5)
        print("Çarpan Katlayan:",carpan_kat)
        time.sleep(1)

    print("Spin Sayisi Belirleniyor...")
    print(random.randint(2,5),random.randint(2,5),random.randint(2,5))
    spin_sayisi = random.randint(2,5)
    print("Spin Sayiniz:",spin_sayisi)
    time.sleep(3)

    return carpan_kat,spin_sayisi



bet = int(input("bet amount: "))
bonus_choice = input("Bonus game (Y|N): ")
if bonus_choice == "Y" or bonus_choice == "y" :
    bet /= 200
    carpan_kat,spin_sayisi = bonus()
    banka_kazanc = 0
else :
    bet /= 20
    spin_sayisi = 1

total_spin = 0

while spin_sayisi != 0 :
    grid = []
    frequency = {}
    carpan,kazanc = 0,0
    for i in range(27) :
        grid.append(0)




    def uret(carpan,kazanc,bet) :
        for i in range(len(grid)) :
            if grid[i] == 0 :
                placeholder = random.randint(0, 48) * random.randint(0, 48)
                if placeholder == 2304 :
                    grid[i] = 1500
                elif placeholder == 1 :
                    grid[i] = 1250
                elif placeholder == 2 :
                    grid[i] = 1100
                elif 2 < placeholder and placeholder <= 4 :
                    grid[i] = 1050
                elif 4 < placeholder and placeholder <= 7 :
                    grid[i] = 1025
                elif 7 < placeholder and placeholder <= 10 :
                    grid[i] = 1015
                elif 10 < placeholder and placeholder <= 13 :
                    grid[i] = 1010
                elif 13 < placeholder and placeholder <= 16 :
                    grid[i] = 1005
                elif 16 < placeholder and placeholder <= 19 :
                    grid[i] = 1004
                elif 19 < placeholder and placeholder <= 25 :
                    grid[i] = 1002
                elif 1440 < placeholder and placeholder <= 1470 :
                    grid[i] = 7
                elif 2240 < placeholder and placeholder <= 2270 :
                    grid[i] = 7
                elif 620 < placeholder and placeholder <= 660 :
                    grid[i] = 7
                elif 25 < placeholder and placeholder <= 204 :
                    grid[i] = 6
                elif 204 < placeholder and placeholder <= 295 :
                    grid[i] = 5
                elif 295 < placeholder and placeholder <= 595 :
                    grid[i] = 4
                elif 595 < placeholder and placeholder <= 1075 :
                    grid[i] = 3
                elif 1075 < placeholder and placeholder <= 1675 :
                    grid[i] = 2
                else :
                    grid[i] = 1
        grid.sort()
        print(grid)
        carpan,kazanc = kontrol(carpan,kazanc,bet)
        return carpan,kazanc



    def kontrol(carpan,kazanc,bet) :
        for i in range(7) :
            frequency[i+1] = 0

        for i in range(len(grid)) :
            if grid[i] < 50 :
                frequency[grid[i]] += 1
            elif grid[i] < 1750 :
                carpan += (grid[i] - 1000)/10
                grid[i] += 1000
        print("Çarpan yeni durum:",carpan)

        for i in range(6) :
            if frequency[i+1] >= 8 :
                kazanc += (frequency[i+1]-8+i+1)*bet
                for k in range(len(grid)) :
                    if grid[k] == i+1 :
                        grid[k] = 0
        print("Kazanç yeni durum:",kazanc)
        print(frequency)
        for i in grid :
            if i == 0 :
                carpan,kazanc = uret(carpan,kazanc,bet)
                
        return carpan,kazanc


    carpan,kazanc = uret(carpan,kazanc,bet)

    if bonus_choice == "Y" or bonus_choice == "y" :
        carpan *= carpan_kat

    float("{0:.2f}".format(carpan))
    float("{0:.2f}".format(kazanc))

    
    print('═'*50)
    if bonus_choice == "Y" or bonus_choice == "y" :
        print("Bet:",bet*200,"|","Jeton Degeri:",bet)
        banka_kazanc += kazanc*carpan
    else :
        print("Bet:",bet*20,"|","Jeton Degeri:",bet)

    time.sleep(1)
    print('═'*50)
    if kazanc/bet >= 5000 :
        print("Son Durumda Kazanç:",bet*5000,"USD with","Çarpan:",carpan)
        print("MAX WIN!")
    else :
        print("Son Durumda Kazanç:",kazanc*carpan,"USD with","Çarpan:",carpan)
    print('═'*50)
    spin_sayisi -= 1
    total_spin += 1

    if bonus_choice == "Y" or bonus_choice == "y" :
        if frequency[7] >= 3 :
            spin_sayisi += 2
            print("Bonus Uzatma. 2 Spin Eklenmistir.")
            time.sleep(1)
    elif frequency[7] >= 4 :
        print("Bonus Oyuna girildi.")
        bonus_choice = "y"
        time.sleep(1)
        carpan_kat,spin_sayisi = bonus()
        banka_kazanc = 0
        banka_kazanc += kazanc

if bonus_choice == "Y" or bonus_choice == "y" :
    banka_kazanc = f"{banka_kazanc:.2f}"
    if float(banka_kazanc)/float(bet) >= 5000 :
        print("Bonus Game Result:",bet*5000,"USD in",total_spin,"spins")
        print("MAX WIN!")
    else :
        print("Bonus Game Result:",banka_kazanc,"USD in",total_spin,"spins")

    print('═'*50)
    