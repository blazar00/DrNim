'''
Author: Braxton Lazar
Date: Juy 19th, 2018

Description:
    Dr. Nim was an old game made in the 1960's where the goal was to get the last ball on the track.
    This is a varient of taht game but in involes dollars. The goal being to get the last dollar from the pile.
    But, Dr. Nim knows how to beat you no matter what. The trick is that you need to chang the amount of dollars
    in the pile to something that isn't a multiple of 4.
'''
class DrNim:

    def __init__(self, name):
        self.lastTurn = 0
        self.name = name

    def takeTurn(self, dollars, playerTurn):
        num = 4 - playerTurn
        self.lastTurn = num

        dollars = dollars - num

        print(self.__repr__())
        print()

        if dollars == 0:
            print(self.victory())

        return dollars

    def victory(self):
        return 'The Doctor took the alst dollar from the pile. Looks like the Doctor has won again. Try again next time!\n\n'

    def __repr__(self):
        return self.name + ' took ' + str(self.lastTurn) + ' from the pile.'

class Player:

    def __init__(self, name):
        self.lastTurn = 0
        self.name = name

    def takeTurn(self, dollars):
        num = 0
        while num < 1 or num > 3:
            user_in = input('Enter the number of dollar bills you want to take (1-3): ')
            num = int(user_in)
        if num < 1 or num > 3:
            print('Whoops! You can only take 1-3 dollars at a time. Try again.')

        self.lastTurn = num
        dollars = dollars - num

        print()
        print(self.__repr__())
        print()

        if dollars == 0:
            self.victory()

        return dollars

    def victory(self):
        return 'You took the last dollar from the pile.\nWhat!? You beat the Doctor? That\'s impossible, no one could have beaten the Doctor. You probably cheated. Take you money and go.\n\n'

    def __repr__(self):
        return 'You took ' + str(self.lastTurn) + ' from the pile.'


#==========================================================
def main():
    '''
    main for DrNim.py. The main functions run through each turn until there are no more dollars on the table.
    The player always goes first, followed by Dr. Nim. 
    '''
    name = input('What is your name? ')
    print(name + ', welcome to Dr. Nim! Do you think you can beat the Doctor?')
    print('\nDr. Nim has 12 dollars on the table. You take a turn taking 1, 2, or 3 dollars from the pile.')
    print('Whoever gets the last dollar from the pile wins everything. Simple, but much harder than it looks.')
    dollars = 12
    player = Player(name)
    drNim = DrNim('Dr. Nim')

    while dollars > 0:
        print('\nThere are ' + str(dollars) + ' dollars in the pile.\n\n')
        dollars = player.takeTurn(dollars)
        dollars = drNim.takeTurn(dollars, player.lastTurn)

if __name__ == '__main__':
    main()
