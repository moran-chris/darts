import numpy as np 
import pandas as pd 


class Scoreboard():

    def __init__(self,game_type,player_count):
        self.game_type = game_type
        self.current_player = 1
        self.player_count = player_count
        self.scores = self.create_scores(self.game_type)
        self.temp_score = self.scores[self.current_player].copy()
        self.status = True
        self.game_dict = {'301':self.create_301_scores(),
                    'Cricket':self.create_cricket_scores()
        }
        self.update_dict = {'301': self.update_score_301,
                            'Cricket': self.update_score_cricket}
    
    def create_scores(self,game_type):
        game_dict = {'301':self.create_301_scores(),
                    'Cricket':self.create_cricket_scores()
        }
        return game_dict[self.game_type]


    def create_301_scores(self):
        index = ['Score']
        values = [301] * self.player_count
        columns = [player for player in range(1,self.player_count+1)]
        scores = pd.DataFrame([values],dtype=int,index = index, columns = columns)
        return scores 
    
    def create_cricket_scores(self):
        index = [15,16,17,18,19,20,25,'Score']
        columns = [player for player in range(1,self.player_count+1)]
        scores = pd.DataFrame(np.zeros([8,self.player_count]),dtype=int,index = index, columns = columns)
        return scores 

    def next_player(self):
        self.scores[self.current_player] = self.temp_score.copy()
        if self.current_player == self.player_count:
            self.current_player = 1 
        else:
            self.current_player += 1 
        self.temp_score = self.scores[self.current_player].copy()
    
    def update_score(self,dart):
        dart = int(dart)
        self.update_dict[self.game_type](dart)

    def update_score_301(self,dart):
        #dart = int(input('enter dart'))
        self.temp_score.loc['Score'] -= dart 
        if self.temp_score['Score']< 0:
            self.temp_score = self.scores[self.current_player].copy()
            self.next_player()
        if self.temp_score.loc['Score'] == 0:
            self.status = False 

    def update_score_cricket(self,dart):
        if dart in self.scores.index:
            non_current_players = [x for x in range(1,self.player_count+1) if x != self.current_player]
            if self.temp_score.loc[dart] < 3:
                self.temp_score.loc[dart] += 1
            elif (self.scores.loc[dart][non_current_players].sum()/3) != (self.player_count - 1):
                self.temp_score['Score'] += dart
            if self.temp_score[:-1].sum() == 21 and self.temp_score['Score'] >= self.scores.loc['Score'].max():
                self.status = False


    def undo(self):
        self.temp_score = self.scores[self.current_player].copy()
        
if __name__ == '__main__':
    foo = Scoreboard('Cricket',2)
    #foo.update_score_301(20)
    foo.next_player()
    