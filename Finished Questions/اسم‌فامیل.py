# https://quera.org/college/3078/chapter/9362/lesson/103390/?comments_page=1&comments_filter=ALL

#################################################################
# adding the correct names to a list selectedwords
#################################################################

import csv
selectedwords = [[] for i in range(6)]
def ready_up():
    address = '/Users/ryan/Vscode repos/Quera-College/Advanced Python Programming and Object-Oriented Thinking/Finished Questions/اسم‌فامیل.csv'
    with open(address, 'r') as csv:
        lines = csv.readlines()
        for line in lines[1:]:
            names = line.rstrip().split(',')
            for i in range(len(names)):
                ii = names[i].replace(' ', '')
                if len(ii) != 0:
                    selectedwords[i].append(ii)   

#################################################################
# adding the players answers to a list
#################################################################

players_and_answers = {}
given_words = [[] for i in range(6)]
def add_participant(participant, answers):    
    xlist = list(answers.values())
    for i in range(len(xlist)):
        xlist[i] = xlist[i].replace(' ', '')
        given_words[i].append(xlist[i])
    players_and_answers[participant] = xlist
    
#################################################################
# adding the players answers to a list
#################################################################

def calculate_all():
    points = {i: 0 for i in players_and_answers.keys()}
    for name, answer in players_and_answers.items():
        for i in range(len(answer)): 
            kalame = answer[i]
            kalameha = selectedwords[i]
            tedad_bazikon = len(players_and_answers.keys())
            tedad_javaba = len([j for j in given_words[i] if j])
            
            if kalame not in kalameha: points[name] += 0
            elif tedad_bazikon == tedad_javaba and given_words[i].count(kalame)  > 1: points[name] += 5
            elif tedad_bazikon == tedad_javaba and given_words[i].count(kalame) == 1: points[name] += 10
            elif tedad_bazikon  > tedad_javaba and given_words[i].count(kalame)  > 1: points[name] += 10
            elif tedad_bazikon  > tedad_javaba and given_words[i].count(kalame) == 1: points[name] += 15
    return points

#################################################################
# tests
#################################################################

def test_subjects(): 
    add_participant(
        participant="salib",
        answers={
            "esm": "علی",
            "famil": "عبدی",
            "keshvar": "عمان",
            "rang": "عسلی",
            "ashia": "عینک",
            "ghaza": "عدسی",
        },
    )
    add_participant(
        participant="kianoush",
        answers={
            "esm": "عباس",
            "famil": "عباسی",
            "keshvar": "عراق",
            "rang": "عسلی",
            "ashia": "عینک",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="sajjad",
        answers={
            "esm": "عارف",
            "famil": "عباس پور",
            "keshvar": "عراق",
            "rang": "عسلی",
            "ashia": "عینکی",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="ali",
        answers={
            "esm": "عرفان",
            "famil": "عامل",
            "keshvar": "عراق",
            "rang": "عسلی",
            "ashia": "عصا",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="mamad",
        answers={
            "esm": "عارف",
            "famil": "علی",
            "keshvar": " ",
            "rang": "عنکبوتی",
            "ashia": "عصا",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="alireza",
        answers={
            "esm": "علی",
            "famil": "عامل",
            "keshvar": "عربستان",
            "rang": "",
            "ashia": "عروسک",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="sama",
        answers={
            "esm": "علی",
            "famil": "عباس",
            "keshvar": "عربستان",
            "rang": "عنابی",
            "ashia": "عروسک",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="aida",
        answers={
            "esm": "علی",
            "famil": "عباسی",
            "keshvar": "عربستان",
            "rang": "عنابی",
            "ashia": "عروسک",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="farhad",
        answers={
            "esm": " علی ",
            "famil": "عباسی پور",
            "keshvar": "عربستان",
            "rang": "عنابی",
            "ashia": "عن",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="mahdi",
        answers={
            "esm": "علی",
            "famil": "عباس پور",
            "keshvar": "عربستان",
            "rang": "عنابی",
            "ashia": "عروسک",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="mina",
        answers={
            "esm": "علی",
            "famil": "عباسی",
            "keshvar": "عراق",
            "rang": "عدسی",
            "ashia": "عینک ها",
            "ghaza": "عدس پلو",
        },
    )
    add_participant(
        participant="saman",
        answers={
            "esm": "علی",
            "famil": "عمران",
            "keshvar": "عراق",
            "rang": "عدسی",
            "ashia": "عصای",
            "ghaza": "عدس پلو",
        },
    )

#################################################################
# run
#################################################################

def main():
    ready_up()
    test_subjects()
    for i,j in calculate_all().items():
        print(i,':', j)
    
if __name__ == '__main__':
    main()
