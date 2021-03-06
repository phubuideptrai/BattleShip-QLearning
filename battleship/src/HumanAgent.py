from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
from TextDisplay import TextDisplay
import Util

"""
HumanAgent implementing Agent interface

This Agent fulfills the Agent interface to allow
a human to play Battleship.  Display the current game
state and ask the user for his desired action.
"""
class HumanAgent(Agent):

    def __init__(self, name):
        self.name = name
   
    def drawCurrentState(self, state, opponentToAttack):
        board = state.getBoard(opponentToAttack)
        ships = state.getShips(opponentToAttack)
        TextDisplay.draw(board, ships, False) 
   
    def placeShips(self, board, ships): 
        Util.randomPlaceShips(board, ships)

    def getAction(self, state): 

        # Ask the human for the opponent to attack
        if len(state.getOpponents(self.name)) > 1:
            while True:
                print ('Please provide the index of the opponent to attack.')
                for index, opponent in enumerate(state.getOpponents(self.name)):
                    print (index, ": ", opponent)
                opponentIndex = input('Enter opponent index: ')
                if opponentIndex.isdigit():
                    opponentIndex = int(opponentIndex)
                    if opponentIndex >= 0 and opponentIndex < len(state.getOpponents(self.name)):
                        break
                print ('Invalid opponent index: ', opponentIndex)
        else:
            opponentIndex = 0

        opponentToAttack = state.getOpponents(self.name)[opponentIndex]

        # Ask the human for the target coordinates
        self.drawCurrentState(state, opponentToAttack)
        while True:
            print ('Hello human', self.name, '! Please provide x and y coordinates of your target.')

            # get position to shoot
            x = input('Enter target x: ')
            y = input('Enter target y: ')
            if not x.isdigit() or not y.isdigit():
                print ('Invalid coordinates')
                continue

            inputPos = Position(int(x), int(y))
            if inputPos in state.legalTargets(opponentToAttack):

                # get torpedo to fire
                if len(state.getTorpedos(self.name)) > 1:
                    while True:
                        availableTorpedos = {}

                        for index, (torpedo, count) in enumerate(state.getTorpedos(self.name).items()):
                            if count > 0:
                                print (index, ': ', torpedo.getTorpedoType(), '[', count, ']')
                                availableTorpedos[index] = torpedo

                        torpedoIndex = input('Enter the torpedo index: ')
                        if not torpedoIndex.isdigit():
                            print ('Invalid torpedo index')
                            continue
                        torpedoIndex = int(torpedoIndex)

                        if torpedoIndex in availableTorpedos.keys():
                            return TorpedoAction(availableTorpedos[torpedoIndex], inputPos, opponentToAttack)

                        else:
                            print ('Invalid torpedo; please try again.')
                else:
                    return TorpedoAction(list(state.getTorpedos(self.name).keys())[0], inputPos, opponentToAttack)

            else:
                print ('Invalid target; please try again.')

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

