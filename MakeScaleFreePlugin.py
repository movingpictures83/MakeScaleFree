# Usage: python makeCliques.py (outputfilename) (size1) (size2) ...

import sys
import networkx
import random
import math
random.seed(1234)   # ONLY FOR TEST PURPOSES, COMMENT OUT FOR BETTER RANDOMNESS

class MakeScaleFreePlugin:
   def input(self, filename):
      myfile = open(filename, 'r')
      self.N = int(myfile.readline())

   def run(self):
      self.DG = networkx.scale_free_graph(self.N)

   def output(self, filename):
      networkx.write_gml(self.DG, filename)
