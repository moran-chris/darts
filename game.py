from scoreboard import Scoreboard
from selenium import webdriver 
import requests
import time 
from templates import * 
from config import *
import keyinput


log = keyinput.KeyInput()
#driver = webdriver.Chrome('/home/chris/darts/chromedriver')
#url = 'http://127.0.0.1:5000/'
input_dict = {'a':1,
              'b':2,
              'c':3,
              'd':4,
              'e':5,
              'f':6,
              'g':7,
              'h':8,
              'i':9,
              'j':10,
              'k':11,
              'l':12,
              'm':13,
              'n':14,
              'o':15,
              'p':16,
              'q':17,
              'r':18,
              's':19,
              't':20,
              'u':25,
              'v':999,
              'w':888,
              'x':777
              }
display_dict = {'301':{2:twoPlayer301Display},
                'Cricket': {2:twoPlayerCricketDisplay}}
#display_file = 'file:///home/chris/darts/display.html'
game_select_dict = {1:'301',
                    2:'Cricket'}

def start_game():
    display(game_select_display)
    log.grab_keystroke()
    game = game_select_dict[input_dict[log.key_stroke]]
    display(player_count_display)
    log.grab_keystroke()
    player_count = input_dict[log.key_stroke]
    return game,player_count

def display(html):
    f = open('display.html','w+')
    f.write(html)
    f.close()
    driver.get(display_file)


def display_score(score):
    if score.status == False:
        print('Game Over')
    data = score.scores.to_dict()
    temp = score.temp_score.to_dict()
    data.update({score.current_player:temp})
    #foo = requests.post(url+score.game_type,json=data).text
    html = display_dict[score.game_type][score.player_count](data)
    display(html)
    # f = open('display.html','w+')
    # f.write(html)
    # f.close()
    # driver.get('file:///home/chris/darts/display.html')

def update_score(score):
    
    log.grab_keystroke()
    dart = input_dict[log.key_stroke]
    if dart == 999:
        return main()
    if dart == 888:
        score.next_player()
        playgame(score=score)
    if dart == 777:
        score.undo()
        playgame(score = score)
    score.update_score(dart)
    playgame(score = score)

def playgame(score):
    display_score(score)
    update_score(score)

def main():
    game_type,player_count = start_game()
    print(game_type)
    print(player_count)
    #driver = webdriver.Chrome('/home/chris/darts/chromedriver')
    #url = 'http://127.0.0.1:5000/'
    score = Scoreboard(game_type,player_count)
    playgame(score)


    # foo = requests.post(url,json=score.scores.to_dict()).text
    # f = open('test.html','w+')
    # f.write(foo)
    # f.close()
    # driver.get('file:///home/chris/darts/test.html')

    # time.sleep(5)
    # score.update_score_301(20)
    # score.next_player() 
    # score.update_score_301(20)
    # score.next_player()
    # print(score.scores)
    # foo = requests.post(url,json = score.scores.to_dict()).text
    # f = open('test.html','w+')
    # f.write(foo)
    # f.close()
    # driver.get('file:///home/chris/darts/test.html')



if __name__ == '__main__':
    main()