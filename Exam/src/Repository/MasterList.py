from Repository.Question import question
class masterList:
    def __init__(self):
        self._masterList = []
        #self.loadFromFile()
    '''
    Function to add a new question to repo
    input - param to create a question
    raises exception if the id of the question in invalid
    '''
    def add (self, params):
        masterList.verifyQuestionParams(params)
        for q in self._masterList:
            if q._id == params[0]:
                raise Exception("ID already in list!!!")
        newQuestion = question(params[0], params[1], params[2], params[3], params[4], params[5], params[6])
        self._masterList.append(newQuestion)
        #self.storeToFile()
    '''
    Filter functions to extract the questions that match the specific difficulty
    returns the list of questions which match the criterion
    '''
    def filter_after_dif(self, dif):
        l = []
        for q in self._masterList:
            print(q._difficulty)
            if q._difficulty == dif:
                l.append(q)
        print(l)
        return l
    
    def filter_after_notDif(self, dif):
        l = []
        for q in self._masterList:
            if q._difficulty != dif:
                l.append(q)
        return l
    #convert to string
    def __str__(self):
        msg = ''
        for q in self._masterList:
            msg += str(q._id)+ ';'+ str(q._text)+ ';'+str(q._choice_a)+ ';' + str(q._choice_b)+ ';' + str(q._choice_c)+ ';' + str(q._correct)+ ';' + str(q._difficulty) + "\n"
        return msg
    
    @staticmethod
    def verifyQuestionParams(params):
        try:
            params[0] = int(params[0])
            assert params[1] != ''
            assert params[2] != ''
            assert params[3] != ''
            assert params[4] != ''
            assert params[5] != ''
            assert params[6] in ['easy', 'medium', 'hard','easy\n', 'medium\n', 'hard\n']
        except:
            raise Exception("Invalid parameters for add!!")
    
    
    #===========================================================================
    # def loadFromFile(self):
    #     try:
    #         f = open("masterLine.txt", "r")
    #         line = f.readline()
    #         while line != "":
    #             attrs = line.split(";")
    #             print(attrs)
    #             #question1 = question(attrs[0], attrs[1], attrs[2], attrs[3], attrs[4], attrs[5], attrs[6])
    #             masterList.add(self, attrs)
    #             line = f.readline()
    #     except:
    #         raise Exception("Could not load from File!")
    #     finally:
    #         f.close()
    #===========================================================================
    
    #===========================================================================
    # def storeToFile(self):
    #     f = open("masterLine.txt", "w")
    #     sts = self._masterList
    #     for q in sts:
    #         strf = str(q._id)+ ';'+ str(q._text)+ ';'+str(q._choice_a)+ ';' + str(q._choice_b)+ ';' + str(q._choice_c)+ ';' + str(q._correct)+ ';' + str(q._difficulty) + "\n"
    #         f.write(strf)
    #     f.close()
    #===========================================================================
    
def addTest():
    a = masterList()
    assert len(a._masterList) == 0
    a.add(["1","waaww",'1','2','3','3','hard'])
    assert a._masterList[0] != question("1","waaww",'1','2','3','3','hard')
    assert len(a._masterList) == 1
    a.add(["32","waaww",'1','2','3','3','hard'])
    assert len(a._masterList) == 2
