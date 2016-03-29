# Simulate the behavior of a fleet of aircraft in the Simpy Environment
# Basic Recipe
# Describe the situation to be modelled in natural language.
# Identify the nouns and verbs as candidates for classes, objects and actions, respectively.

import simpy
import numpy as np
import scipy.stats as Status
import pandas as pd

failTimes = []

class Component(object):
    def __init__(self, env, name, fDist, distParam):
        self.env = env
        self.name = name
        self.fDist = fDist
        self.distParam = distParam
        self.birthday = self.env.now

    def fly(self, fDist, distParam):
        
