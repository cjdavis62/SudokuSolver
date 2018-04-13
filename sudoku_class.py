class sudoku:
    
    def __init__(self, name):
        self.name = name
        width = 9
        length = 9
        initial = [[ 0 for x in range(width)] for y in range(length)]
        self.values = initial

    def change_name(self, new_name):
        self.name = new_name

    def change_value(self, new_value, row, column):
        self.values[row][column] = new_value

    def check_row(row):
        pass

    def check_column(column):
        pass

    def check_square(square):
        pass

    def show(self):
        for x in range(9):
            for y in range(9):
                print (self.values[x][y], end = ' ')
            print("")

