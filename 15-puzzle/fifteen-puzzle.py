

class Board:

    def __init__(self, initBoard):
        assert len(list(initBoard)) == 16 # check 15 puzzle
        self.size = 16
        self.width = 4
        self.path = []
        self.path.append(initBoard)
        self.distance = []
        self.distance.append(self.manhattan_distance())

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
        print('\n\n')

    def move(self, directon):
        blank = self.path[-1].index(None)
        moveRes = self.path[-1][:]
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

    def expand(self):
        blank = self.path[-1].index(None)
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
            newPath.append(self.move(direction))
        return newPath

    def getPos(self, x, y):
        """
            x, y: range from 0 to 3
        """
        return self.path[-1][self.width*y + x]

    def check(self):
        solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None]
        return solution == self.path[-1]

    def manhattan_distance(self):
        distance = 0
        for i in range(self.size - 1):
            distance += abs(i // self.width - self.path[-1].index(i+1) // self.width)
            distance += abs(i % self.width - self.path[-1].index(i+1) % self.width)
        return distance



if __name__ == '__main__':
    b = Board([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None])
    while True:
        b.show(b.path[-1])
        i = input()
        b.move(i)


