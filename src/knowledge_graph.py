import networkx as nx
import pandas as pd
import os

def build_knowledge_graph(directory):
    G = nx.Graph()

    for file in os.listdir(directory):
        if file.endswith(".csv"):
            filepath = os.path.join(directory, file)
            data = pd.read_csv(filepath)

            jurisdiction = os.path.splitext()
