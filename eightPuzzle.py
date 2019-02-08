class Node:
    def __init__(self, puzzle_matrix, level, f_score):
        self.puzzle_matrix = puzzle_matrix
        self.level = level
        self.f_score = f_score

    def find_empty(self, input_matrix, empty_char):
        for i in range(0,len(self.puzzle_matrix)):
            for j in range(0, len(self.puzzle_matrix)):
                if input_matrix[i][j] == empty_char:
                    return i,j

    def generate_child(self):
        x,y = self.find_empty(self.puzzle_matrix, 'E')
        pos_values = [[x,y-1], [x,y+1], [x-1,y], [x+1,y]]
        children = []

        for i in pos_values:
            child = self.shuffle(self.puzzle_matrix,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child, self.level+1,0)
                children.append(child_node)
        return children
    #TODO: Write shuffle function

class eightPuzzle:
    def __init__(self, inputMatrix):
        self.puzzle_matrix = inputMatrix
        self.empty_location = zip(*np.where)
