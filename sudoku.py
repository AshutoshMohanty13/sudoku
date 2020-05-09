board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def solve(b):

    find = find_empty(b)
    if not find:
        return True
    else:
        (row, col) = find

    for i in range(1,10):
        if valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b): # here we recursively use the solve function until we reach the condition in line 15, if not then we backtrack
                return True

            b[row][col] = 0

    return False




def valid(b, num, pos): # where 'b' is the sudoku board, 'num' is the number to be placed in the position 'pos'

    #check row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

     #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(b):

    for i in range(len(b)):
        if i%3 == 0 and i!=0:   # for rows
            print('--------------------')

        for j in range(len(b[0])):
            if j%3 == 0 and j!=0:   #for columns
                print('|', end='')  #we use end because the pointer should not go to the next line

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end='')

#print_board(board)

def find_empty(b):

    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j) #row, column

    return  None

print_board(board)
solve(board)
print('after solving')
print_board(board)