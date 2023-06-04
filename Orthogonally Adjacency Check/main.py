import random

grid = [['0' for row in range(4)] for col in range(5)]

def uret() :

    for i in range(len(grid)) :
        for k in range(len(grid[0])) :

            if random.randint(0,2) == 1 :
                grid[i][k] = "A"

    for i in range(len(grid)) :
        print(grid[i])


def kontrol(row,col,total_numb) :

    if grid[row][col] == "A" :
        grid[row][col] = "B"
                
        if col != len(grid[0]) - 1 and grid[row][col + 1] == "A" :
            total_numb += 1
            total_numb = kontrol(row,col + 1,total_numb)
                
        if row != len(grid) - 1 and grid[row + 1][col] == "A" :
            total_numb += 1
            total_numb = kontrol(row + 1,col,total_numb)
                
        if col != 0 and grid[row][col - 1] == "A" :
            total_numb += 1
            total_numb = kontrol(row,col - 1,total_numb)
                
        if row != 0 and grid[row - 1][col] == "A" :
            total_numb += 1
            total_numb = kontrol(row - 1,col,total_numb)
    return total_numb

def nokta() :

    for row in range(len(grid)) :
        for col in range(len(grid[0])) :
            total_numb = 0
            total_numb = kontrol(row,col,total_numb)
            if total_numb > 0 :
                total_numb += 1
            max_adj.append(total_numb)


uret()
max_adj = []
nokta()

print("--------------------------")
for line in grid :
    print(line)

print("Adjacency List:",max_adj)
print("Maximum Number of Adjacent Blocks:",max(max_adj),"Starting at Row:",int(max_adj.index(max(max_adj)) / len(grid[0])),", Column:",max_adj.index(max(max_adj)) % len(grid[0]))
if max(max_adj) == 0 :
    print("There are no adjacent blocks that are more than one.")
