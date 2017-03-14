from Repository.MasterList import masterList
from random import shuffle
from copy import deepcopy

class masterController:
    def __init__(self, repo):
        self._repo = repo
    
    '''
    function that calls the add function in the repo.
    it takes as input the param of the new question and passes them on to the next funct
    '''
    def add(self, params):
        self._repo.add(params)
    
    '''
    Create function which takes as param the diff, no of questions and name of file
    and then creates a new file with the required questions
    input = parameters
    output - none, the function creates a file
    '''
    def create(self, params):
        if params[0] not in ['easy', 'medium', 'hard']:
            raise Exception("invalid1!!")
        g = open (params[2], "w")
        no = int(params[1])
        enough = False
        
        if params[0] == 'easy':
            no1 = no//2
            no2 = no-no1
            for q in self._repo._masterList:
                if no1 == 0:
                    enough = True
                    break
                    
                if q._difficulty == 'easy\n':
                    g.write(str(q))
                    no1 -=1
            for q in self._repo._masterList:
                if no2 == 0:
                    break
                    
                if q._difficulty != 'easy\n':
                    g.write(str(q))
                    no2 -=1
        if params[0] == 'medium':
            no1 = no//2
            no2 = no-no1
            for q in self._repo._masterList:
                if no1 == 0:
                    enough = True
                    break
                    
                if q._difficulty == 'medium\n':
                    g.write(str(q))
                    no1 -=1
            for q in self._repo._masterList:
                if no2 == 0:
 
                    break
                    
                if q._difficulty != 'medium\n':
                    g.write(str(q))
                    no2 -=1
                    
        if params[0] == 'hard':
            no1 = no//2
            no2 = no-no1
            copy1 = deepcopy(self._repo._masterList)
            shuffle(copy1)
            for q in copy1:
                if no1 == 0:
                    enough = True
                    break
                    
                if q._difficulty == 'hard\n':
                    g.write(str(q))
                    no1 -=1
            for q in self._repo._masterList:
                if no2 == 0:
                    break

                if q._difficulty != 'hard\n':
                    g.write(str(q))
                    no2 -=1
        
        if enough == False:
            raise Exception("Not enough entries")
        g.close()
        
    '''
    Start function which opens the file and creates a quiz game
    it reads all entries in the file and requests input from the user
    after all lines are read, the function ends and returns the score
    input - parameters
    output - score
    '''
    def start(self, params):
        file = open(params[0], "r+")
        line = file.readline()
        score = 0
        while (line!=''):
            show = line.split(";")
            print(show[0], show[1], show[2], show[3], show[4])
            n = input("Your answer: ")
            
            if n == show[5]:
                if show[6] == 'easy\n':
                    score += 1
                if show[6] == 'medium\n':
                    score += 2
                if show[6] == 'hard\n':
                    score += 3
            line = file.readline()
                
        return score
    
    @staticmethod
    def verifyCreate(params, questions):
        if params[0] not in ['easy\n', 'medium\n', 'hard\n']:
            raise Exception("invalid1!!")
        
def testCreate():
    repo = masterList()
    ctrl = masterController(repo)
    assert len(repo._masterList) == 0
    #ctrl.create(['easy','2','adasdasd.txt'])
    f = open ("adasdasd.txt", "r+")
    line = f.readline()
    leng = 0
    #while line != '':
    #    leng+= 1
    #    line = f.readline()
    
    assert leng == 0
    
    '''
    1;which number is biggest?;1;4;3;4;easy
2;which number is smallest?;1;4;3;1;easy
3;which number is prime?;1;2;4;2;easy
4;which number is div by 2?;2;1;3;2;medium
5;which is a fish?;fp;asia;carp;carp;medium
6;first satellite?;apollo;sputnik;idk;sputnik;hard
7;a mole can be?;animal;idk;sth;animal;medium
8;name of a good book?;HarryPotter;Lotr;hungerGames;Lotr;hard
9;random input with answer 1?;1;2;3;1;easy
10;how hard was the fp test?;veryhard;hard;easy;very;easy

    '''
