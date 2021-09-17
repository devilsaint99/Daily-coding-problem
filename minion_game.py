"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points."""



def minion_game(string):
    kev,st=0,0    
    vowels=['A','E','I','O','U']
    kev_score,stu_score,length=0,0,len(string)
    for i in range(length):
        if string[i] in vowels:
            kev_score+=length-i
        else:
            stu_score+=length-i
    if kev_score>stu_score:
        print('Kevin',kev_score)
    elif stu_score>kev_score:
        print('Stuart',stu_score)
    else:
        print('Draw')
minion_game('BANANA')