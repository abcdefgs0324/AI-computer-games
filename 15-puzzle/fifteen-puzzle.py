

class Board:

    def __init__(self, pos):
        assert len(list(pos)) == 16 # check 15 puzzle
        self.size = 16
        self.width = 4
        self.pos = pos

    def show(self):
        print('-----------------')
        for i in range(self.size):
            if i % self.width == 0:
                print('|', end='')
            if self.pos[i] is None:
                print('   |', end='')
            else:
                print('{:3d}|'.format(self.pos[i]), end='')
            if i % self.width == (self.width - 1):
                print()
                print('-----------------')
        print('\n\n')

    def move(self, directon):
        blank = self.pos.index(None)
        if (directon == 'r') and (blank % self.width != 0):
            self.pos[blank] = self.pos[blank-1]
            self.pos[blank-1] = None
        if (directon == 'l') and (blank % self.width != 3):
            self.pos[blank] = self.pos[blank+1]
            self.pos[blank+1] = None
        if (directon == 'u') and (blank < (self.size-self.width)):
            self.pos[blank] = self.pos[blank+self.width]
            self.pos[blank+self.width] = None
        if (directon == 'd') and (blank >= self.width):
            self.pos[blank] = self.pos[blank-self.width]
            self.pos[blank-self.width] = None

    def getPos(self, x, y):
        """
            x, y: range from 0 to 3
        """
        return self.pos[self.width*y + x]

    def check(self):
        solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None]
        return solution == self.pos

    def manhattan_distance(self):
        distance = 0
        for i in range(self.size - 1):
            distance += abs(i // self.width - self.pos.index(i+1) // self.width)
            distance += abs(i % self.width - self.pos.index(i+1) % self.width)
            print(distance)
        return distance



if __name__ == '__main__':
    b = Board([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None])
    while True:
        b.show()
        i = input()
        b.move(i)


