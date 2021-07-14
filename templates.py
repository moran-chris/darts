game_select_display = """ <html>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
        .grid-container {
                        display: grid;
                        grid-template-columns: auto auto ;
                        background-color: black;
                        padding: 10px;
                        }
        .grid-item {
                        background-color: black;
                        border: 1px solid;
                        border-color: black black white black;
                        padding: 20px;
                        font-size: 30px;
                        text-align: center;
                        color:red;
                        }
         .letters {
                        height:8px;
                        line-height:16px;
                        border-bottom:1px solid black;
                        font-weight: 900;
                        position:relative;
                        padding: 10px;
                        display:inline-block;
                        -webkit-transform: rotate(45deg);
                  }
         
    </style>
   <head>
      <title>Game Selection</title>
   </head>
   
   
   <body style="background-color:black;">
      
      <h1 style = "color:white;"> Game Selection</h1>
      
      <div class="grid-container"> 
        <div style="border-color: black black black black;" class="grid-item">301</div>
        <div style="border-color: black black black black;" class="grid-item">1</div>
        <div style="border-color: black black black black;" class="grid-item">Cricket</div>
        <div style="border-color: black black black black;"class="grid-item">2</div>


   </body>
</html> """

player_count_display = """<html>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
        .grid-container {
                        display: grid;
                        grid-template-columns: auto auto ;
                        background-color: black;
                        padding: 10px;
                        }
        .grid-item {
                        background-color: black;
                        border: 1px solid;
                        border-color: black black white black;
                        padding: 20px;
                        font-size: 30px;
                        text-align: center;
                        color:red;
                        }
         .letters {
                        height:8px;
                        line-height:16px;
                        border-bottom:1px solid black;
                        font-weight: 900;
                        position:relative;
                        padding: 10px;
                        display:inline-block;
                        -webkit-transform: rotate(45deg);
                  }
         
    </style>
   <head>
      <title>Select Number of Players</title>
   </head>
   
   
   <body style="background-color:black;">
      
      <h1 style = "color:white;"> Select Number of Players</h1>
      
      <div class="grid-container"> 
        <div style="border-color: black black black black;" class="grid-item"></div>
        <div style="border-color: black black black black;" class="grid-item"></div>
        <div style="border-color: black black black black;" class="grid-item"></div>
        <div style="border-color: black black black black;"class="grid-item"></div>


   </body>
</html>"""

def twoPlayer301Display(data):

   score1 = str(data[1]['Score'])
   score2 = str(data[2]['Score'])
   html ="""
   <html>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
        .grid-container {
                        display: grid;
                        grid-template-columns: auto auto auto;
                        background-color: black;
                        padding: 10px;
                        }
        .grid-item {
                        background-color: black;
                        border: 1px solid;
                        border-color: black black white black;
                        padding: 20px;
                        font-size: 30px;
                        text-align: center;
                        color:red;
                        }
         .letters {
                        height:8px;
                        line-height:16px;
                        border-bottom:1px solid black;
                        font-weight: 900;
                        position:relative;
                        padding: 10px;
                        display:inline-block;
                        -webkit-transform: rotate(45deg);
                  }
         
    </style>
   <title>TEEEEEEEEEEEEEEEEEESt</title>
   <head>
      <title>Scoreboard</title>
   </head>
   
   
   <body style="background-color:black;">
      
      <h1 style = "color:white;"> Scoreboard</h1>
      
      <div class="grid-container">
        <div style="border-color:black;"class="grid-item">Player 1</div>
        <div style="border-color:black;"class="grid-item"></div>
        <div style="border-color:black;"class="grid-item">Player 2</div>  
        <div style="border-color: black black white black;" class="grid-item">"""+score1+"""</div>
        <div class="grid-item">SCORE</div>
        <div class="grid-item">"""+score2+"""</div>  
       

   </body>
</html> """
   return html

def twoPlayerCricketDisplay(data):
   symbols = {0:'',
              1:'&#124;',
              2:'&#10005;',
              3:'&#10754;'}
   html = """ <html>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
        .grid-container {
                        display: grid;
                        grid-template-columns: auto auto auto;
                        background-color: black;
                        padding: 10px;
                        }
        .grid-item {
                        background-color: black;
                        border: 1px solid;
                        border-color: black black white black;
                        padding: 20px;
                        font-size: 30px;
                        text-align: center;
                        color:red;
                        }
         .letters {
                        height:8px;
                        line-height:16px;
                        border-bottom:1px solid black;
                        font-weight: 900;
                        position:relative;
                        padding: 10px;
                        display:inline-block;
                        -webkit-transform: rotate(45deg);
                  }
         
    </style>
   <head>
      <title>Scoreboard</title>
   </head>
   
   
   <body style="background-color:black;">
      
      <h1 style = "color:white;"> Scoreboard</h1>
      
      <div class="grid-container">
        <div style="border-color:black;"class="grid-item">Player 1</div>
        <div style="border-color:black;"class="grid-item"></div>
        <div style="border-color:black;"class="grid-item">Player 2</div>  
        <div style="border-color: black black white black;" class="grid-item">""" + str(data[1]['Score']) + """</div>
        <div class="grid-item">SCORE</div>
        <div class="grid-item">""" + str(data[2]['Score'])+"""  </div>  
        <div style="border-color: black black white black;" class="grid-item">""" +symbols[data[1][20]]+ """</div>
        <div class="grid-item">20</div>
        <div class="grid-item">"""+symbols[data[2][20]] + """</div> 
        <div class="grid-item">""" + symbols[data[1][19]]+ """</div>
        <div class="grid-item">19</div>
        <div class="grid-item">"""+symbols[data[2][19]]+"""</div> 
        <div class="grid-item"><span class='letters'>"""+symbols[data[1][18]]+"""</span></div>
        <div class="grid-item">18</div>
        <div class="grid-item">"""+symbols[data[2][18]]+"""</div> 
        <div class="grid-item">"""+symbols[data[1][17]]+"""</div>
        <div class="grid-item">17</div>
        <div class="grid-item">"""+symbols[data[2][17]]+"""</div> 
        <div class="grid-item">"""+symbols[data[1][16]]+"""</div>
        <div class="grid-item">16</div>
        <div class="grid-item">"""+symbols[data[2][16]]+"""</div>  
        <div class="grid-item">"""+symbols[data[1][15]]+"""</div>
        <div class="grid-item">15</div>
        <div class="grid-item">"""+symbols[data[2][15]]+"""</div>  
        <div class="grid-item">"""+symbols[data[1][25]]+"""</div>
        <div class="grid-item">&#128002;</div>
        <div class="grid-item">"""+symbols[data[2][25]]+"""</div>  
      </div>

   </body>
</html> 
"""
   return html