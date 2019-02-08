
goal_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', 'E']]

with open('prog1_input.txt') as f:
    num_puzzles = int(f.readline())
    print(num_puzzles)
    for i in range(num_puzzles):
        current_puzzle = []

        # eight puzzle means three lines of numbers
        for j in range(3):
            current_line = f.readline().strip('\n')
            while current_line == '':
                current_line = f.readline().strip('\n')
            current_puzzle.append(current_line.split())

        print(current_puzzle)
        #for k in current_puzzle:
            #print(k)
        #print('\n')


