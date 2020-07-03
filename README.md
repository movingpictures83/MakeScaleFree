# MakeScaleFree
# Language: Python
# Input: TXT (one line with the size of the network to produce)
# Output: GML (scale-free network with the specified number of nodes
# Tested with: PluMA 1.1, Python 3.6
# Dependency: networkx==2.2, numpy==1.16.0

PluMA plugin to build a scale-free network (Albert and Barabasi, 2002) with
a specified number of nodes.

Input is just a simple text file containing the number of nodes for the network.

The network will be output in the Graph Modeling Language (GML).
