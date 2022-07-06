from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random
import Util

"""
Hunt and Target agent implementing the Agent interface

The Hunt and Target agent will randomly search the board.
After hitting an enemy ship, the Hunt and Target agent 
will attack surrounding squares until the ship is sunk.
"""
class HuntAndTargetAgent(Agent):

    def __init__(self, name):
        self.name = name

    def placeShips(self, board, ships): 
        Util.randomPlaceShips(board, ships)

    def parityChoose(matrix):
        tup = getParityTup()
        while(matrix[tup[0]][tup[1]]==-1):
            tup = getParityTup()
        return tup

    def getParityTup():
        x = random.randrange(0,10,1)
        if(x%2==0):
            y = random.randrange(0,10,2)
        else:
            y = random.randrange(1,10,2)
        tup = (x,y)
        return tup
    def getAction(self, state): 
        randomTorpedo = random.choice(list(state.getTorpedos(self.name).keys()))
        opponentToAttack = random.choice(state.getOpponents(self.name))
        sunkPositions = []
        for ship in state.getShips(opponentToAttack):
            if ship.isSunk():
                sunkPositions += ship.getPositions()

        board = state.getBoard(opponentToAttack)
        candidateActions = []
        legalMoves = state.legalTargets(opponentToAttack)
        for hitPos in board.getHitPositions():
            if hitPos not in sunkPositions:
                for adjacentTile in board.getValidNeighbors(hitPos):
                    if adjacentTile not in board.getMissedPositions() and adjacentTile in legalMoves:
                        candidateActions.append(adjacentTile)
                    
        if not candidateActions:
            candidateActions = legalMoves
        
        action = TorpedoAction(randomTorpedo, random.choice(candidateActions), opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

