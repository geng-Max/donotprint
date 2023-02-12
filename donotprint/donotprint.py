class Print(object):
    def __init__(self, prt):
        self.__prt = prt
        dic = {False: 'off', True: 'open'}
        print('Ice.print is', dic[prt])

    def print(self, *args, sep=' ', end='\n', file=None):
        if self.__prt:
            print(*args, sep=sep, end=end, file=file)