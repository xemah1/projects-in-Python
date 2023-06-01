import random

#bet = input("bet amount: ")
bet = 1
grid = []
frequency = {}
carpan,kazanc = 1,0
pat = []
for i in range(30) :
    grid.append(0)

def uret(carpan,kazanc,bet) :
    for i in range(len(grid)) :
        if grid[i] == 0 :
            placeholder = random.randint(0, 500)
            if placeholder == 0 :
                grid[i] = 1500
            elif placeholder == 1 :
                grid[i] = 1250
            elif placeholder == 2 and placeholder == 3 :
                grid[i] = 1100
            elif 3 < placeholder and placeholder <= 6 :
                grid[i] = 1050
            elif 6 < placeholder and placeholder <= 11 :
                grid[i] = 1025
            elif 11 < placeholder and placeholder <= 17 :
                grid[i] = 1015
            elif 17 < placeholder and placeholder <= 27 :
                grid[i] = 1010
            elif 27 < placeholder and placeholder <= 40 :
                grid[i] = 1005
            elif 40 < placeholder and placeholder <= 57 :
                grid[i] = 1004
            elif 57 < placeholder and placeholder <= 79 :
                grid[i] = 1002
            elif 79 < placeholder and placeholder <= 109 :
                grid[i] = 6
            elif 109 < placeholder and placeholder <= 149 :
                grid[i] = 5
            elif 149 < placeholder and placeholder <= 199 :
                grid[i] = 4
            elif 199 < placeholder and placeholder <= 279 :
                grid[i] = 3
            elif 279 < placeholder and placeholder <= 379 :
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

    for i in grid :
        if i < 50 :
            frequency[i] += 1
        else :
            carpan += i - 1000
    print("Çarpan yeni durum:",carpan)

    for i in range(6) :
        if frequency[i+1] >= 8 :
            kazanc += (i+1)*frequency[i+1]*carpan*bet/320
            pat.append(i+1)
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
print("Son Durumda Kazanç:",kazanc,"Çarpan:",carpan)