# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        print "mdp ", self.mdp
        print "discount", self.discount
        print "iterations", self.iterations
        print "values", self.values
        print "mdp.getStates()", mdp.getStates()
        print "possible actions((0,0))", mdp.getPossibleActions((0,0))
        print "mdp.getTransitionStatesAndProbs('0,0', mdp.getPossibleActions('0,0')[0])", mdp.getTransitionStatesAndProbs((0,0), mdp.getPossibleActions((0,0))[0])


        for i in range(self.iterations):
	        for state in self.mdp.getStates():
	        	q_values = []
	        	if state != 'TERMINAL_STATE':	
		        	for possible_action in self.mdp.getPossibleActions(state):
		        		q_values.append(self.getQValue(state, possible_action))
		        	self.values[state] = max(q_values)


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # Q value is the expected value, or probability times real value. Q-value is more than just this though!

        Q_value = 0
        gamma = self.discount
        long_list = mdp.getTransitionStatesAndProbs(state,action)

        for action_prob in long_list:
        	probability = long_list[action_prob][1]
        	next_state = long_list[action_prob][0]
        	Q_value += [self.values(next_state)*gamma + self.getReward(state, action, next_state)]*probability

        return Q_value

        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
