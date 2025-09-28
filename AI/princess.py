# def displayPathtoPrincess(m, grid):
#     for idx, row in enumerate(grid):
#         if 'p' in row:
#             princess = (idx, row.index('p'))
#         if 'm' in row:
#             mario = (idx, row.index('m'))
        

#     drows = princess[0] - mario[0]
#     dcols = princess[1] - mario[1]

#     return ''.join(['UP\n' * abs(drows) if drows < 0 else 'DOWN\n' * drows,
#                     'LEFT\n' * abs(dcols) if dcols < 0 else 'RIGHT\n' * dcols])

    
# if '_input' in globals():
#     _input = _input.strip().split()
#     m = int(_input[0], 10)
#     grid = _input[1:]
# else:
#     m = input()
#     grid = []

#     for i in range(0, m):
#         grid.append(raw_input().strip())

# print(displayPathtoPrincess)



def displayPathtoPrincess(n,grid):
    pos_col = {}
    pos_row = {}
    not_find = True

    for i in range(n):
        line = len(grid[i])
        for j in range(line):
            if grid[i][j] == 'm':
                pos_row['m'] = i
                pos_col['m'] = j
            elif grid[i][j] == 'p':
                pos_row['p'] = i
                pos_col['p'] = j

    while (not_find):
        if pos_row['m'] < pos_row['p']:
            pos_row['m'] = pos_row['m'] + 1
            print ('DOWN')
        elif pos_row['m'] > pos_row['p']:
            pos_row['m'] = pos_row['m'] - 1
            print ('UP')

        if pos_col['m'] < pos_col['p']:
            pos_col['m'] = pos_col['m'] + 1
            print ('RIGHT')
        elif pos_col['m'] > pos_col['p']:
            pos_col['m'] = pos_col['m'] - 1
            print ('LEFT')
        
        if pos_col['m'] == pos_col['p'] and pos_row['m'] == pos_row['m']:
            not_find = False

#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)