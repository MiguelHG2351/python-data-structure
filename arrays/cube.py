from grid import Grid

class Cube():
    def __init__(self, rows, cols, depth):
        self.data = Grid(rows,cols)
        for i in range(rows):
            for j in range(cols):
                self.data[i][j] = Grid(depth,depth)
                for k in range(depth):
                    for l in range(depth):
                        self.data[i][j][k][l] = 0

    def get_height(self):
        return self.data.get_height()

    def get_width(self):
        return self.data.get_width()

    def get_depth(self):
        return self.data[0][0].get_width()

    def get_width(self):
        return len(self.data[0])

    def __str__(self) -> str:
        result = ''
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                for k in range(self.get_depth()):
                    result += str(self.data[i][j][k]) + ' '
                result += '\n'
        return result


if __name__ == '__main__':
    c = Cube(2,2,2)
    print(c)
