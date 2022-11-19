import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def chromatic_number(G):
    p = nx.chromatic_polynomial(G)
    for i in range(len(G)):
        if(p.subs({'x': i}) > 0):
            return i
    return -1

G = nx.cycle_graph(5)
print(chromatic_number(G))