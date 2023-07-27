#!/usr/bin/python
# Won 1 Tie 0 Lost 3
# Head ends here
memory = []

def get_pos_of(board, what='d'):
    dirt = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == what:
                dirt.append([x, y])
    return sorted(dirt)
    

def closest_point(current_pos, targets):
    x1 = current_pos[0]
    y1 = current_pos[1]
    target = []
    shortest = -1
    for point in targets:
        x2 = point[0]
        y2 = point[1]
        distance = abs(((x2 - x1)*2 + (y2 - y1)*2))**(1/2)
        if distance == 0:
            return point
        else:
            if shortest == -1 or distance < shortest:
                target = point
                shortest = distance                    
    return target

def update_memory(memory, board):
    if len(memory) == 0:
        memory = board
    else:
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] != 'o':
                    memory[y][x] = board[y][x]
    
    return memory
        
def next_move(posy, posx, board):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UP = 'UP'
    DOWN = 'DOWN'
    CLEAN = 'CLEAN'
    global memory
    
    memory = update_memory(memory, board)
    
    dirt = get_pos_of(memory)
    invisible = get_pos_of(memory, 'o')
    dirt = closest_point([posy, posx], dirt)
    invi = closest_point([posy, posx], invisible)
    
    target = dirt
    if len(target) == 0:
        target = invi
    
    if memory[posy][posx] == 'd':
        print('CLEAN')
        memory[posy][posx] = '-'
        return CLEAN
    else:
        x = target[0]
        y = target[1]
        dif_x = x-posx
        dif_y = y-posy

        if dif_y > dif_x:
            if dif_y > 0:
                print('DOWN')
                return DOWN
            elif dif_y < 0:
                print('UP')
                return UP
            else:
                print('LEFT')
                return LEFT
        elif dif_y < dif_x:
            if dif_x > 0:
                print('RIGHT')
                return RIGHT
            elif dif_x < 0:
                print('LEFT')
                return LEFT
            else:
                print('UP')
                return UP
        else:
            if memory[posy][posx] == 'd':
                print('CLEAN')
                memory[posy][posx] = '-'
                return CLEAN
            elif dif_y > 0:
                print('DOWN')
                return DOWN
            else:
                print('UP')
                return UP


def next_move(posy, posx, board):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    CLEAN = "CLEAN"
    global memory
    memory = update_memory(memory, board)

    dirt = get_pos_of(memory)
    invisible = get_pos_of(memory, "o")
    dirt = closest_point([posy, posx], dirt)
    invi = closest_point([posy, posx], invisible)

    target = dirt
    if len(target) == 0:
        target = invi

    if memory[posy][posx] == "d":
        print("CLEAN")
        memory[posy][posx] = "-"
        return CLEAN
    else:
        x = target[0]
        y = target[1]
        dif_x = x - posx
        dif_y = y - posy

        if dif_y > dif_x:
            if dif_y > 0:
                print("DOWN")
                return DOWN
            elif dif_y < 0:
                print("UP")
                return UP
            else:
                print("LEFT")
                return LEFT
        elif dif_y < dif_x:
            if dif_x > 0:
                print("RIGHT")
                return RIGHT
            elif dif_x < 0:
                print("LEFT")
                return LEFT
            else:
                print("UP")
                return UP
        else:
            if memory[posy][posx] == "d":
                print("CLEAN")
                memory[posy][posx] = "-"
                return CLEAN
            elif dif_y > 0:
                print("DOWN")
                return DOWN
            else:
                print("UP")
                return UP

# Tail starts here
if __name__ == "__main__":
    moves = []
    pos = [0, 0]
    board = [
        ["-", "d", "-", "-", "-"],
        ["-", "d", "-", "-", "-"],
        ["-", "-", "-", "d", "-"],
        ["-", "-", "-", "d", "-"],
        ["-", "-", "d", "-", "d"]
    ]
    while len(get_pos_of(board)) != 0:
        move = next_move(pos[0], pos[1], board)
        if move == "CLEAN":
            board[pos[0]][pos[1]] = "-"
            moves.append(move)
        elif move == "LEFT":
            pos[1] = pos[1] - 1
            moves.append(move)
        elif move == "RIGHT":
            pos[1] = pos[1] + 1
            moves.append(move)
        elif move == "UP":
            pos[0] = pos[0] - 1
            moves.append(move)
        elif move == "DOWN":
            pos[0] = pos[0] + 1
            moves.append(move)
    print(len(moves))
