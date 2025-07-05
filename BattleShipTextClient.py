#Israel Prusente(PRSISR001)
#Joseph Duda(DDXVUS002)
from GameClient import *
from PyQt5.QtCore import *

class BattleShipTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [x[:] for x in [[' ']*6]*6] # creates 6x6 game board
        self.role = None # role C (for captain) or G (for general)
        
    def clear_board(self):
        self.board = [x[:] for x in [[' ']*6]*6]
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-5,0-5):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self, col=0, row=0,character=''):
        num = 0
        for j in self.board:
            print("{:-^25}".format(""))
            for rows in range(1):
                for column in range(7):
                    if column == col and num == row:
                        vetical = "|{:^3}".format(character)
                        print(vetical,end="")   
                    else:   
                        vetical = "|{:3}".format('')
                        print(vetical,end="")
                print()
            num += 1
        print("{:-^25}".format(""))             
   
    def handle_message(self,msg):
        self.msg=msg
        if self.msg=='new game,C':
            print('...New Game for Battleship Initiated...')
            print('...You are the Captain...')
            
        elif self.msg=='new game,G':
            print('...New Game for Battleship Initiated...')
            print('...You are the General...')  
            
    
        elif self.msg=='opponents move':
            print('Wait for opponent\'s move.')
            
        elif self.msg=='your move':
            print('It is your turn to play.Enter you move.')
            self.move = self.input_move()
            self.send_message(self.move)         
            
        elif 'valid move' in self.msg:
            self.captain_score=self.msg[17]
            self.general_score=self.msg[19]
            col=int(self.msg[15])
            row=int(self.msg[13])
            if 'G' in self.msg:
                print('General played a valid move.')
                self.display_board( col, row,'G')
            elif 'C' in self.msg:
                print('Captain played a valid move.')
                self.display_board( col, row,'C')
            print('Captain Score: ',self.captain_score)
            print('General Score: ',self.general_score)        
            
        elif self.msg=='invalid move':
            print('Invalid move.Enter your move again.')
            self.move = self.input_move()
            self.send_message(self.move)
    
        elif 'game over' in self.msg:
            if self.msg=='game over,T':
                print('Game over and it is a tie.')
            elif self.msg=='game over,C':
                print('Game over and Captain is the winner.')              
            elif self.msg=='game over,G':
                print('Game over and General is the winner.')            
            
        elif self.msg=='play again':
            self.send_message( input_play_again())
        
        elif self.msg=='exit':
            print('Game has been exited.')
            
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
class LoopThread(QThread,GameClient):
    update_label_signal = pyqtSignal(str)
    def __init__(self,ip_address=None):
        QThread.__init__(self)   
        GameClient.__init__(self)
        self.ip_address=ip_address
       
    def run(self): 
        try:
            self.connect_to_server(self.ip_address)
            self.update_label_signal.emit('Connected...')
            while True:
                msg = self.receive_message()
                if len(msg)>0:
                    self.update_label_signal.emit(msg)            
        except:
            self.update_label_signal.emit('Error to connecting to the server...')                     
def main():
    bstc = BattleShipTextClient()
    while True:
        try:
            bstc.connect_to_server(bstc.input_server())
            break
        except:
            print('Error connecting to server!')
    bstc.play_loop()
    input('Press enter to exit.')

if __name__ == "__main__":
    main()