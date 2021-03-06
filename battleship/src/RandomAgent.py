from Agent import Agent
from Position import Position
from TorpedoAction import TorpedoAction
import random
import Util

"""
RandomAgent implementing the Agent interface

The RandomAgent will randomly place his ships and
randomly pick targets to attack.
"""
class RandomAgent(Agent):

    def __init__(self, name):
        self.name = name
   
    def placeShips(self, board, ships): 
        Util.randomPlaceShips(board, ships)

    def getAction(self, state): 
        randomTorpedo = random.choice(list(state.getTorpedos(self.name).keys()))
        opponents = state.getOpponents(self.name)
        opponentToAttack = random.choice(opponents)
        candidateActions = state.legalTargets(opponentToAttack)
        action = TorpedoAction(randomTorpedo, random.choice(candidateActions), opponentToAttack)
        return action

    def incorporateFeedback(self, state, action, reward, newState):
        pass

    def prepareForTesting(self):
        pass

