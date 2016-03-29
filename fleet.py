# Simulate the behavior of a fleet of aircraft in the Simpy Environment
# Basic Recipe
# Describe the situation to be modelled in natural language.
# Identify the nouns and verbs as candidates for classes, objects and actions, respectively.

import simpy
import numpy as np
import scipy.stats as st
import pandas as pd

failTimes = []

class Component(object):
    def __init__(self, env, name, fDist, fParams):
        self.env = env
        self.name = name
        self.fDist = fDist
        self.fParams = fParams
        self.birthday = self.env.now

    def run(self):
        while True:
            print('starting')
            yield self.env.process(self.fly())

    def fly(self):
        rollUni = st.uniform.rvs(1)
        rollDist = self.fDist.rvs(1, **self.fParams)
        if rollUni > rollDist:
            print('I done broke')
        else:
            print('Survived another day!')
        yield self.env.timeout(2)
