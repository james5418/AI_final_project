# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math;


# %%
class Car:
    # car_num 車子編號(int)
    # isvertical 垂直/水平(boolean)
    # size 大小(int)
    # istarget 是否是需要移出的那台車(boolean)
    # x,y 以車子的左邊，上面車子的頭(int)
    def __init__(self,car_num,isvertical,size,x,y) :
        self.car_num = car_num
        self.isvertical = isvertical
        self.size = size
        # istarget
        # self.istarget = istarget
        self.x = x
        self.y = y

    # 下面這個method執行car的移動方向
    def car_move(self,direction):
        if direction == "L":
            self.go_left()
        elif direction == "R":
            self.go_right()
        elif direction == "U":
            self.go_up()
        elif direction == "D":
            self.go_down()
    # 水平：
    # 向左移動1格
    def go_left(self):
        self.y = self.y - 1
    # 向右移動1格
    def go_right(self):
        self.y = self.y + 1
    # 垂直
    # 向上移動1格
    def go_up(self):
        self.x = self.x - 1
    # 向下移動1格
    def go_down(self):
        self.x = self.x + 1


# %%
class Board:    
    def __init__(self, board, cars):
        self.size = len(board);
        self.exit = ((self.size-1) // 2, self.size-1);
        self.emptySymbol = "o";
        self.wallToken = "x";
        self.board = board;
        self.directions = ["U", "D", "L", "R"];
        
        if (cars is None):
            self.cars = [];
            self.setCars();

        else:
            self.cars = cars;
            
    def setCars(self):
        # car_num,isvertical,size,x,y
        for i in range(26):
            self.cars.append(None);
            
        #self.cars.append(Car("A", False, 2, 0, 0));
        
        for i in range(self.size):
            for j in range(self.size):
                token = self.board[i][j];
                
                if (token == self.wallToken or token == self.emptySymbol):
                    continue;
                    
                elif (i > 0 and self.board[i-1][j] == token):
                    continue;
                    
                elif (j > 0 and self.board[i][j-1] == token):
                    continue;
                    
                else:
                    size = 0;
                    vertical = True;
                    
                    if (i+1 < self.size and self.board[i+1][j] == token):
                        vertical = True;
                        
                        if (i+2 < self.size and self.board[i+2][j] == token):
                            size = 3;
                        else:
                            size = 2;
                    else:
                        vertical = False;
                        
                        if (j+2 < self.size and self.board[i][j+2] == token):
                            size = 3;
                        else:
                            size = 2;
                            
                    self.cars[ord(token) - ord('A')] = Car(token, vertical, size, i, j);
    
    def tokenToIndex(self, token):
        return ord(token) - ord('A');
    
    def solved(self):
        target = self.cars[0];
        
        for i in range(target.y + target.size, self.size):
            if (self.occupied(target.x, i)):
                return False;

        return True;
    
    def printBoard(self):
        for i in range(self.size + 2):
            print("-", end="");
            
        print("");
        
        for i in range(self.size):
            print("|", end="");
            
            for j in range(self.size):
                print(self.board[i][j], end="");
            
            if (i == self.exit[0]):
                print(" ");
            else:
                print("|")
            
        for i in range(self.size + 2):
            print("-", end="");
            
        print("\n");
    
    # check if a spot on the board is occupied by a car
    def occupied(self, x, y):
        return self.board[x][y] != self.emptySymbol;
    
    def carCanMove(self, token):
        index = self.tokenToIndex(token);
        
        for d in self.directions:
            if (self.validMove(index, d, 1)):
                return True;
        
        return False;
        
    # check if a move is legal
    def validMove(self, index, direction, steps):
        car = self.cars[index];
        
        if (direction == "U"):
            if (not car.isvertical):
                #print("invalid direction!");
                return False;
            
            elif (car.x - steps < 0):
                #print("out of bound!");
                return False;
            
            for i in range(1, steps+1):
                if (self.occupied(car.x - i, car.y)):
                    #print("car crash!");
                    return False;
            
            else:
                return True;
            
        elif (direction == "D"):
            if (not car.isvertical):
                #print("invalid direction!");
                return False;
            
            elif (car.x + car.size - 1 + steps >= self.size):
                #print("out of bound!");
                return False;
            
            for i in range(1, steps+1):
                if (self.occupied(car.x + car.size - 1 + i, car.y)):
                    #print("car crash!");
                    return False;
                
            else:
                return True;
            
        elif (direction == "L"):
            if (car.isvertical):
                #print("invalid direction!");
                return False;
            
            elif (car.y - steps < 0):
                #print("out of bound!");
                return False;
            
            for i in range(1, steps+1):
                if (self.occupied(car.x, car.y - i)):
                    #print("car crash!");
                    return False;
            
            else:
                return True;
            
        elif (direction == "R"):
            if (car.isvertical):
                #print("invalid direction!");
                return False;
            
            elif (car.y + car.size - 1 + steps >= self.size):
                #print("out of bound!");
                return False;
            
            for i in range(1, steps+1):
                if (self.occupied(car.x, car.y + car.size - 1 + i)):
                    #print("car crash!");
                    return False;
                
            else:
                return True;
            
    def play(self, index, direction, steps):
        if (self.validMove(index, direction, steps)):
            car = self.cars[index];
            
            if (direction == "U"):
                for i in range(steps):
                    self.board[car.x - 1][car.y] = car.car_num;
                    self.board[car.x + car.size - 1][car.y] = self.emptySymbol;
                    car.car_move(direction);
                    
            elif (direction == "D"):
                for i in range(steps):
                    self.board[car.x + car.size][car.y] = car.car_num;
                    self.board[car.x][car.y] = self.emptySymbol;
                    car.car_move(direction);
                    
            elif (direction == "L"):
                for i in range(steps):
                    self.board[car.x][car.y - 1] = car.car_num;
                    self.board[car.x][car.y + car.size - 1] = self.emptySymbol;
                    car.car_move(direction);
                    
            elif (direction == "R"):
                for i in range(steps):
                    self.board[car.x][car.y + car.size] = car.car_num;
                    self.board[car.x][car.y] = self.emptySymbol;
                    car.car_move(direction);
                    
            return True;
        
        else:
            return False;

    def copyBoard(self):
        cpy = [];
        
        for i in range(self.size):
            cpy.append([]);
            for j in range(self.size):
                cpy[i].append(self.board[i][j]);
                
        return cpy; 
    
    def copyCars(self):
        cpy = [];
            
        for car in self.cars:
            if (car is None):
                cpy.append(None);
            
            else:
                copyCar = Car(car.car_num, car.isvertical, car.size, car.x, car.y);
                cpy.append(copyCar);
            
        return cpy;
    
    def stateAfterMove(self, index, direction, steps):
        if (self.validMove(index, direction, steps)):
            newBoard = Board(self.copyBoard(), self.copyCars());
            newBoard.play(index, direction, steps);
            
            return newBoard;
        
        else:
            return None;
        
    def expand(self):
        frontier = [];
        
        for i in range(len(self.cars)):
            if (self.cars[i] is None):
                continue;
            
            for d in self.directions:
                for step in range(1, self.size):
                    nextBoard = self.stateAfterMove(i, d, step);
                
                    if (nextBoard is not None):
                        node = (nextBoard, i, d, step);
                        frontier.append(node);
        
        return frontier;


# %%
def convertBoard(string):
    size = int(math.sqrt(len(string)));
    board = [];
    
    for i in range(size):
        board.append([]);
            
        for j in range(size):
            board[i].append(string[i * size + j]);
            
    return board;


# %%
class StateNode(object):
    def __init__(self, fx, depth, state, path):
        self.fx = fx
        self.depth = depth
        self.state = state
        self.path = path
  
    def __lt__(self, other):
        return self.fx < other.fx


# %%
import heapq

def blockDepth(state, token, depth): # state is a Board object
    if (depth > 3):
        return math.inf;
    
    if (state.carCanMove(token)):
        return depth;
    
    else:
        car = state.cars[state.tokenToIndex(token)];
        d1 = math.inf;
        d2 = math.inf;
        
        if (car.isvertical):    
            if (car.x > 0 and state.board[car.x-1][car.y] != state.wallToken):
                d1 = blockDepth(state, state.board[car.x-1][car.y], depth+1);
            if (car.x + car.size < board.size and state.board[car.x + car.size][car.y] != state.wallToken):
                d2 = blockDepth(state, state.board[car.x + car.size][car.y], depth+1);
        
        else:
            if (car.y > 0 and state.board[car.x][car.y-1] != state.wallToken):
                d1 = blockDepth(state, state.board[car.x][car.y-1], depth+1);
            if (car.y + car.size < board.size and state.board[car.x][car.y + car.size] != state.wallToken):
                d2 = blockDepth(state, state.board[car.x][car.y + car.size], depth+1);
        
        return min(d1, d2);
            

# 算車頭到出口的距離
# inadmissible (depends on how we count the steps)
def manhattan(board):
    return abs(board.cars[0].y - board.exit[1]);

# 計算車頭到出口被幾臺車擋住
# admissible
def h2(board):
    count = 0;
    target = board.cars[0];
    
    for i in range(target.y + target.size, board.size):
        if (board.occupied(target.x, i)):
            count = count + 1;
        
    return count;

# same as h2, but if the car which blocks the way cannot move, add another 1
# inadmissible
def h3(board):
    count = 0;
    target = board.cars[0];
    
    for i in range(target.y + target.size, board.size):
        if (board.occupied(target.x, i)):
            count = count + 1;
            
            if (not board.carCanMove(board.board[target.x][i])):
                count = count + 1;
        
    return count;

def h4(board):
    count = 0;
    target = board.cars[0];
    
    for i in range(target.y + target.size, board.size):
        if (board.occupied(target.x, i)):
            count = count + 1 + blockDepth(board, board.board[target.x][i], 0);
        
    return count;
  
def h5(board):
    heu = 0
    target = board.cars[0]
    for i in range(target.y+target.size,board.size):
        if board.occupied(target.x,i):
            heu += 1
            if (board.cars[board.tokenToIndex(board.board[target.x][i])].x <= (board.size/2)-1 ):
                heu += board.cars[board.tokenToIndex(board.board[target.x][i])].x
            else:
                 heu += board.size - board.cars[board.tokenToIndex(board.board[target.x][i])].x - 1
    return heu
    
def astar(state, heuristic): # state is a Board obj, heuristic is the heauristic function
    ans = []
    visited = []
    start = [] 

    #hx = manhatten(state) + heuristic(state);
    depth = 0;
    #fx = hx + depth;
    fx = heuristic(state) + depth;
    
    statenode = StateNode(fx, depth, board, start);

    node_list = []
    heapq.heapify(node_list)
    heapq.heappush(node_list, statenode)

    visited.append(board.board)

    while node_list:
        node = heapq.heappop(node_list);

        if node.state.solved():
            ans = node.path+[(0, "R", node.state.size - node.state.cars[0].y - 2)];
            return ans, len(visited), len(visited)+len(node_list);
    
        # use expand1() if you want to move only 1 step far per expansion
        for B, car_id, d, s in node.state.expand():
      
            if B.board not in visited:            
                g = node.depth + 1;
                f = heuristic(B) + g;
                tmp = StateNode(f, g, B, node.path+[(car_id, d, s)]); # 紀錄path

                heapq.heappush(node_list, tmp);
                visited.append(B.board);
    

# %% [markdown]
# # Export 1 File

# %%
fileName = "medium sample.txt"; #change ======================
readPath = "./puzzles/medium_result/" + fileName;
writePath = "./puzzles/medium_result/" + "Manhattan.txt"; #change ======================

file = open(readPath, "r");
lines = file.readlines();
file.close();

results = open(writePath, "w");

def heuristic(board):
    return  manhattan(board); # change ======================

for line in lines:
    steps, puzzle, nodes = line.split(" ");
    
    # if (int(i) % 10 == 0): print(i);
    
    board = Board(convertBoard(puzzle), None);
    ans, visited, expanded = astar(board, heuristic);
    results.write("{} {} {}\n".format(len(ans), visited, expanded));
    '''
    if (len(ans) != int(steps)): 
        results.write(" suboptimal\n");
    else:
        results.write("\n");
    '''
    
results.close();


# %%
for i in range(10, 70, 10):
    fileName = str(i) + " sample.txt"; #change ======================
    readPath = "./puzzles/" + fileName;
    writePath = "./puzzles/results/h4_manhattan/" + "results_" + fileName; #change ======================

    file = open(readPath, "r");
    lines = file.readlines();
    file.close();

    results = open(writePath, "w");

    def heuristic(board):
        return manhattan(board) + h4(board); # change ======================

    print("\n", fileName);
    for line in lines:
        i, steps, puzzle, nodes = line.split(" ");

        if (int(i) % 10 == 0): print(i);

        board = Board(convertBoard(puzzle), None);
        ans, visited, expanded = astar(board, heuristic);
        results.write("{} {} {} {}\n".format(i, len(ans), visited, expanded));
        '''
        if (len(ans) != int(steps)): 
            results.write(" suboptimal\n");
        else:
            results.write("\n");
        '''

    results.close();

# %% [markdown]
# # Play the Game

# %%
def playGame(board):
    board.printBoard();

    while (not board.solved()):
        print("\n\n");
        car = input("car: ");
        direction = input("direction: ");
        steps = input("steps: ");

        board.play(board.tokenToIndex(car), direction, int(steps));
        board.printBoard();

    print("problem solved!");


# %%
puzzle = "ooFBBxooFGoHoAAGoHoooooHDDDxoooooooo";
board = Board(convertBoard(puzzle), None);
board.printBoard()
playGame(board);

# %% [markdown]
# # Solve a Puzzle

# %%
puzzle = "ooxGGoooBCooAABCooooBCoooEEDDoooooo";
board = Board(convertBoard(puzzle), None);
board.printBoard();

ans, visited, expanded = astar(board, h2);

print("{} node are expanded, {} of them are visited".format(expanded, visited));
print("The solution takes {} steps:\n".format(len(ans)));

for car, direction, steps in ans:
    d = "";
    if (direction == "U"):
        d = "up";
    elif (direction == "D"):
         d = "down";
    elif (direction == "L"):
        d = "left";
    elif (direction == "R"):
        d = "right";
        
    print("Car {} goes {} by {}.".format(board.cars[car].car_num, d, steps));
    board.play(car, direction, steps);
    board.printBoard();


# %%



