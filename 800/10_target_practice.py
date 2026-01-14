t = int(input())
for _ in range(t):
    grid = []
    for _ in range(10):
        row = input()
        grid.append(row)
    
    total = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == '.':
                continue
            if i == 0 or i == 9 or j == 0 or j == 9:
                total += 1
            elif i == 1 or i == 8 or j == 1 or j == 8:
                total += 2
            elif i == 2 or i == 7 or j == 2 or j == 7:
                total += 3
            elif i == 3 or i == 6 or j == 3 or j == 6:
                total += 4
            else:
                total += 5
    
    print(total)