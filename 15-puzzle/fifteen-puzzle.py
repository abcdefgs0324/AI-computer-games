
import logging
logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)

class Board:

    def __init__(self, initBoard):
        assert len(list(initBoard)) == 16 # check 15 puzzle
        self.size = 16
        self.width = 4
        self.board = initBoard
        self.AstarPath = None
        self.bfsPath = None

    def show(self, board):
        print('-----------------')
        for i in range(self.size):
            if i % self.width == 0:
                print('|', end='')
            if board[i] is None:
                print('   |', end='')
            else:
                print('{:3d}|'.format(board[i]), end='')
            if i % self.width == (self.width - 1):
                print()
                print('-----------------')
        print()

    def move(self, board, directon):
        blank = board.index(None)
        moveRes = board[:]
        if (directon == 'r') and (blank % self.width != 0):
            moveRes[blank] = moveRes[blank-1]
            moveRes[blank-1] = None
        if (directon == 'l') and (blank % self.width != 3):
            moveRes[blank] = moveRes[blank+1]
            moveRes[blank+1] = None
        if (directon == 'u') and (blank < (self.size-self.width)):
            moveRes[blank] = moveRes[blank+self.width]
            moveRes[blank+self.width] = None
        if (directon == 'd') and (blank >= self.width):
            moveRes[blank] = moveRes[blank-self.width]
            moveRes[blank-self.width] = None
        return moveRes

    def expand(self, board):
        blank = board.index(None)
        expandDirections = []
        if blank // self.width != 0:
            expandDirections.append('d')
        if blank // self.width != (self.width-1):
            expandDirections.append('u')
        if blank % self.width != 0:
            expandDirections.append('r')
        if blank % self.width != (self.width-1):
            expandDirections.append('l')
        newPath = []
        for direction in expandDirections:
            newPath.append(self.move(board, direction))
        return newPath

    def getPos(self, board, x, y):
        """
            x, y: range from 0 to 3
        """
        return board[self.width*y + x]

    def check(self, board):
        return self.manhattan_distance(board) == 0

    def manhattan_distance(self, board):
        distance = 0
        for i in range(self.size - 1):
            distance += abs(i // self.width - board.index(i+1) // self.width)
            distance += abs(i % self.width - board.index(i+1) % self.width)
        return distance

    def Astar(self):
        """
            A* algorithm
        """
        state = []
        stateDist = []
        path = [self.board]
        traversed = []
        while self.check(path[-1]) != True:
            if len(traversed) % 200 == 0:
                logging.info('A* has traversed ' + str(len(traversed)) + ' nodes')
            if path[-1] not in traversed:
                for node in self.expand(path[-1]):
                    if node not in traversed:
                        state.append(path + [node])
                        stateDist.append(self.manhattan_distance(node))
                        if path[-1] not in traversed:
                            traversed.append(path[-1])
            nextIndex = stateDist.index(min(stateDist))
            path = state[nextIndex]
            state = state[:nextIndex] + state[nextIndex+1:]
            stateDist = stateDist[:nextIndex] + stateDist[nextIndex+1:]
        self.AstarPath = path

    def breadth_first(self):
        """
            Breadth First Search algorithm
        """
        state = []
        path = [self.board]
        traversed = []
        while self.check(path[-1]) != True:
            if len(traversed) % 200 == 0:
                logging.info('BFS has traversed ' + str(len(traversed)) + ' nodes')
            if path[-1] not in traversed:
                for node in self.expand(path[-1]):
                    if node not in traversed:
                        state.append(path + [node])
                traversed.append(path[-1])
            path = state[0]
            state = state[1:]
        self.bfsPath = path

    def showAstarSol(self):
        if self.AstarPath == None:
            self.Astar()
        print('A* algorithm solution:')
        for step in range(len(self.AstarPath)):
            print('Step ' + str(step) + ':')
            self.show(self.AstarPath[step])

    def showBfsSol(self):
        if self.bfsPath == None:
            self.breadth_first()
        print('BFS algorithm solution:')
        for step in range(len(self.bfsPath)):
            print('Step ' + str(step) + ':')
            self.show(self.bfsPath[step])




if __name__ == '__main__':
    b = Board([15,2,3,4,5,6,7,8,9,10,11,12,13,1,14,None])
    b.showAstarSol() # b.showBfsSol()


