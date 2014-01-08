# Su Doku
# Problem 96

# Su Doku (Japanese meaning number place) is the name given to a popular
# puzzle concept. Its origin is unclear, but credit must be attributed to
# Leonhard Euler who invented a similar, and much more difficult, puzzle
# idea called Latin Squares. The objective of Su Doku puzzles, however,
# is to replace the blanks (or zeros) in a 9 by 9 grid in such that each
# row, column, and 3 by 3 box contains each of the digits 1 to 9. Below
# is an example of a typical starting puzzle grid and its solution grid.

#     003  020  600               483  921  657
#     900  305  001               967  345  821
#     001  806  400               251  876  493
#
#     008  102  900               548  132  976
#     700  000  008               729  564  138
#     006  708  200               136  798  245
#
#     002  609  500               372  689  514
#     800  203  009               814  253  769
#     005  010  300               695  417  382

# A well constructed Su Doku puzzle has a unique solution and can be solved
# by logic, although it may be necessary to employ "guess and test" methods
# in order to eliminate options (there is much contested opinion over this).
# The complexity of the search determines the difficulty of the puzzle; the
# example above is considered easy because it can be solved by straight
# forward direct deduction.
#
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
# contains fifty different Su Doku puzzles ranging in difficulty, but all
# with unique solutions (the first puzzle in the file is the example above).
#
# By solving all fifty puzzles find the sum of the 3-digit numbers found in
# the top left corner of each solution grid; for example, 483 is the 3-digit
# number found in the top left corner of the solution grid above.

import time

start = time.time()

class SolveException(Exception):
    pass

class UnsolvableException(Exception):
    pass

class SuDoku:    
    def __init__(self, puzzle, debug=False):
        self.puzzle = puzzle
        self.__unknown_count = sum([1 for row in range(9) for col in range(9) if puzzle[row][col] == 0])
        self.__debug = debug
        self.__rollback_cache = []

    def __repr__(self):
        s = ''
        for row in range(9):
            s += ' '.join([str(x) for x in self.get_row(row)]) + '\n'
        return s
    
    @property
    def signature(self):
        return int(''.join([str(self.get(x,0)) for x in range(3)]))

    def solve(self):
        while self.__simple_pass() > 0:
            pass

        while self.__unknown_count > 0:
            if self.__debug: print('  There are {} unknowns'.format(self.__unknown_count))
            x,y = [(x,y) for x in range(9) for y in range(9) if self.get(x,y) == 0][0]
            if self.__debug: print('  First unknown is ({},{})'.format(x,y))
            possibles = self.possibles(x,y)
            if self.__debug: print('  Possibilities are', possibles)
            for attempt in possibles:
                if self.__debug: print('  Setting to ',attempt)
                self.__rollback_cache.append(self.puzzle)
                self.set_cell(x,y,attempt)
                self.__unknown_count -= 1
                solved = False
                try:
                    self.solve()
                    solved = True
                    break
                except SolveException:
                    if self.__debug: print('  SolveException')
                
        if self.__unknown_count > 0:
            raise UnsolvableException('Puzzle has no possible solution')

    def get(self,x,y):
        return self.puzzle[y][x]

    def set_cell(self,x,y,val):
        self.puzzle[y][x] = val
    
    def get_row(self,rownum):
        return self.puzzle[rownum]
    
    def get_col(self,colnum):
        return [row[colnum] for row in self.puzzle]
        
    def get_block(self,x,y):
        box_x = x // 3
        box_y = y // 3
        return [self.get(x2,y2)
                for x2 in range(box_x * 3, (box_x + 1) * 3)
                for y2 in range(box_y * 3, (box_y + 1) * 3)
        ]
    
    def possibles(self,x,y):
        if self.get(x,y) > 0:
            return [self.get(x,y)]

        not_possible = set()
        not_possible |= set([i for i in self.get_row(y) if i > 0])
        not_possible |= set([i for i in self.get_col(x) if i > 0])
        not_possible |= set([i for i in self.get_block(x,y) if i > 0])
        
        return [i for i in range(1,10) if i not in not_possible]

    def __simple_pass(self):
        calculated = 0
        for x in range(9):
            for y in range(9):
                if self.get(x,y) == 0:
                    poss = self.possibles(x,y)
                    if len(poss) == 1:
                        self.set_cell(x,y,poss[0])
                        calculated += 1
                        self.__unknown_count -= 1
                    elif len(poss) == 0:
                        raise SolveException("No possible values at ({},{})".format(x,y))
        return calculated

    def __rollback(self):
        if len(self.__rollback_cache) == 0:
            raise Exception('Nothing to rollback')
        
        self.puzzle = self.__rollback_cache.pop()
        self.__unknown_count = sum([1 for x in range(9) for y in range(9) if self.get(x,y) == 0])

'''
puzzle = [
[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0]
]


sudoku = SuDoku(puzzle)
print(sudoku)
sudoku.solve()
print(sudoku)
print('Signature:', sudoku.signature)
'''

result = 0

with open('euler96_sudoku.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines() if line[0] != 'G']

print(lines)
num_puzzles = len(lines) // 9
for p in range(num_puzzles):
    print ('Solving puzzle', p+1)
    puzzle = []
    for l in range(p*9,(p+1)*9):
        puzzle.append([int(i) for i in lines[l]])
    sudoku = SuDoku(puzzle, p == 2)
    sudoku.solve()
    result += sudoku.signature
        
print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
