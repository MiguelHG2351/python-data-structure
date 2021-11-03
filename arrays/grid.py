from arrays import Array

class Grid():
    def __init__(self, rows, cols, fill_value=0):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(cols, fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self): # Similar a un override
        result = ''
        for row in self.data:
            for col in row:
                result += str(col) + ' '
            result += '\n'
        return result
