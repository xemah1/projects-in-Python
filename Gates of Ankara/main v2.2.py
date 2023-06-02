import random

#bet = input("bet amount: ")
bet = 100
grid = []
frequency = {}
carpan,kazanc = 0,0
for i in range(25) :
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
    for i in range(6) :
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
            kazanc += (frequency[i+1]-8+i+1)*bet/10
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
float("{0:.2f}".format(carpan))
float("{0:.2f}".format(kazanc))
print("Bet:",bet)
print("Son Durumda Kazanç:",kazanc*carpan,"Çarpan:",carpan)