
class Menu:
    def __init__(self, controller):
        self._ctrl = controller
    
    @staticmethod
    def keyboardCmd(line):
        count = 0
        while line[count] != " ":
            count+=1
        cmd = line[:count]
        params = line[count+1:].split(";")
        return cmd, params
    
    def start(self):
        print("Welcome to the QuizMaster 2000!")
        alive = True
        try:
            while (alive):
                userInput = input("Input command: ")
                cmd, params = Menu.keyboardCmd(userInput)
                if cmd == 'add':
                    Menu.f_add(self,params)
                if cmd == 'create':
                    Menu.f_create(self, params)
                if cmd == 'start':
                    Menu.f_start(self,params)
                if cmd == 'exit':
                    exit()
        except Exception as x:
            print (x)
                
    def f_add(self, params):
        self._ctrl.add(params)
    def f_create(self, params):
        self._ctrl.create(params)
    
    def f_start(self, params):
        print(self._ctrl.start(params))
                 

