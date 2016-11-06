"""
This short example shows how you can mine frequent graphs using the wrapper
"""
from parsemis import ParsemisMiner
import networkx as nx
import os

# Load our graphs
graph_folder = "example_dataset"
graphs = []
for f in os.listdir(graph_folder):
    path = "%s/%s" % (graph_folder, f)
    graphs.append(nx.read_gml(path))

frequent_graphs = ParsemisMiner(
    "data", "parsemis.jar", minimum_frequency="2%", close_graph=True, store_embeddings=True, debug=True
).mine_graphs(graphs)

# Count our subgraphs
frequent_graph_counts = []
for frequent_graph in frequent_graphs:
    count = 0
    for graph in graphs:
        if graph.graph['id'] in frequent_graph.graph['embeddings']:
            count += 1
    frequent_graph_counts.append((count, frequent_graph))

for frequent_graph in sorted(frequent_graph_counts, key=lambda subgraph: subgraph[0], reverse=True):
    if len(frequent_graph[1].edges()) == 0:
        print("%i - %s" % (frequent_graph[0], frequent_graph[1].nodes()))
    else:
        print("%i - %s" % (frequent_graph[0], frequent_graph[1].edges()))
