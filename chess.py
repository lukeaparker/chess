class Team():

    def __init__(self):
        self.pawns = []
    
    def pawn_count(self):
        return len(self.pawns)

class Pawn():

    def __init__(self, postion, team):

        self.position = postion 
        self.team = team


class Game():

    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.white = Team()
        self.black = Team()
        self.turn = 'white'

    
    def setup_board(self):

        for c in range(0, 8):
            pawn = Pawn((1, c), 'white')
            self.white.pawns.append(pawn)
            self.board[1][c] = '*'
        
        for c in range(0, 8):
            pawn = Pawn((6, c), 'black')
            self.black.pawns.append(pawn)
            self.board[6][c] = '^'
        

        self.display_board()
        print('Your board is all setup! Pick who is white and who is black.')
        self.play_turn()
    
    def update_board(self, current_position, new_position):
        self.board[current_position[0]][current_position[1]] = 0
        self.board[new_position[0]][new_position[1]] = '*'


    def move_pawn(self, team, current_position, new_position):
        if team == 'white':
            for pawn in self.white.pawns:
                if pawn.position[0] == int(current_position[0]) and pawn.position[1] == int(current_position[1]):
                    pawn.position = (int(new_position[0]), int(new_position[1]))
                    current_position = (int(current_position[0]), int(current_position[1]))
                    new_position = (int(new_position[0]), int(new_position[1]))
                    self.update_board(current_position, new_position)


    def play_turn(self):
        team = self.turn
        print(team)
        current_position = input('Enter position of pawn')
        new_position = input('Enter new position')
        self.move_pawn(team, current_position, new_position)
        self.display_board()
        if self.turn == 'white':
            self.turn = 'black'
        if self.turn == 'black':
            self.turn = 'white'
        return self.play_turn() 


    
 
        
    def display_board(self):
        for row in self.board:
            print(row)
        print('white: ', self.white.pawn_count())
        print('black: ', self.black.pawn_count())
    



        


def play_chess():
    round = Game()
    round.setup_board()

play_chess()
