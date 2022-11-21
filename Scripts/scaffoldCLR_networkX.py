import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
from Bio.Seq import Seq
import itertools

input_fasta = open("originalFiles/coturnix.bp.p_ctg.gfaOneLine.fa","r")
output_fasta = open("coturnix.out.fa","w")

def create_network():
    G = nx.Graph()

#Create all nodes from index
    chrom = open("chrom_sizes_sorted.tsv","r")
    for lines in chrom:
        line = lines.strip("\n").split("\t")
        G.add_nodes_from([(line[0], {"length":int(line[1])})])

#Read paf and create all alignment as edges. Self aligment are removed.
    paf = open("ListReadsMultipleAligned.paf","r")
    line = paf.readline()
    while (line != ''):
        readsName = line.split("\t")[0]
        ctgList = []
        while line.split("\t")[0] == readsName:
            ctgList.append(line.split("\t")[5])
            line = paf.readline()
        uniq_ctgList = []
        for item in ctgList:
            if item not in uniq_ctgList:
                uniq_ctgList.append(item)
        pair_ctgList = itertools.combinations(uniq_ctgList,2)
        for items in pair_ctgList:
            if G.has_edge(items[0],items[1]):
                G.edges[items[0],items[1]]['weight'] += 1
            else:
                G.add_edge(items[0],items[1])
                G.edges[items[0],items[1]]['weight'] = 1

    #nx.draw(G, with_labels=False, node_size=20, width=1, edgecolors="red")
    #plt.savefig("Network.png")
    #nx.write_gml(G, "graph.gml")
    return G

G = create_network()
print("Number of edges: " + str(G.number_of_edges()))
print("Number of nodes: " + str(G.number_of_nodes()))

#Remove edges with weight < 2
listToRemove = []
listToRemove2 = []
for (u,v,wt) in G.edges.data("weight"):
    if wt <2:
        listToRemove.append(u)
        listToRemove2.append(v)
for x in range (0,len(listToRemove)):
    G.remove_edge(listToRemove[x],listToRemove2[x])
print("Number of edges after clearing weigth <3: " + str(G.number_of_edges()))
print("Number of nodes after clearing weigth <3: " + str(G.number_of_nodes()))

for x in range(0,40):
    print("\n On a supprimé le noeud le plus connecté: " + str(max(dict(G.degree()).items(), key = lambda x : x[1])))
    G.remove_node(max(dict(G.degree()).items(), key = lambda x : x[1])[0])
    print("Number of edges after this deletion: " + str(G.number_of_edges()))
    print("Number of nodes after this deletion: " + str(G.number_of_nodes()))

    list_of_soloNodes = [node for node in G.nodes if G.degree(node) == 0]
    list_of_monoLinkNodes = [node for node in G.nodes if G.degree(node) == 1]
    list_of_dualLinkNodes = [node for node in G.nodes if G.degree(node) == 2]
    print("State of nodes: Alone: " + str(len(list_of_soloNodes)) + " mono: " + str(len(list_of_monoLinkNodes)) + " dual: " + str(len(list_of_dualLinkNodes))   )
    # if x%100 == 0:
    #     for nodeName in list_of_soloNodes:
    #         G.remove_node(nodeName)
    #     plt.clf()
    #     nx.draw(G, with_labels=False, node_size=20, width=1, edgecolors="red")
    #     plt.savefig("Network"+str(x)+"WithWeight3.png")




#Write node with no edges in the fasta file
list_of_soloNodes = [node for node in G.nodes if G.degree(node) == 0]
for nodeName in list_of_soloNodes:
    write_nextLine = False
    for line in input_fasta:
        if write_nextLine:
            output_fasta.write(line)
            write_nextLine = False
            break
        if line.startswith(">"+str(nodeName)):
            output_fasta.write(line)
            write_nextLine = True
    input_fasta.seek(0)
    print("on supprime "+str(nodeName))
    G.remove_node(nodeName)
#nx.draw(G, with_labels=False, node_size=20, width=1, edgecolors="red")
#plt.savefig("Network_filtered_noSoloNodes.png")
#nx.write_gml(G, "graph_filtered_noSoloNodes.gml")
#print(G.number_of_nodes())
#
#
#
# #G=nx.read_gml("graph_filtered_noSoloNodes.gml")
#
#
while G.number_of_nodes() != 0:
    if G.number_of_edges() == 0:
        list_of_soloNodes = [node for node in G.nodes if G.degree(node) == 0]
        for nodeName in list_of_soloNodes:
            write_nextLine = False
            for line in input_fasta:
                if write_nextLine:
                    output_fasta.write(line)
                    write_nextLine = False
                    break
                if line.startswith(">"+str(nodeName)):
                    output_fasta.write(line)
                    write_nextLine = True
            input_fasta.seek(0)
            print("on supprime "+str(nodeName))
            G.remove_node(nodeName)
        break
    # On cherche le noeud de départ avec le poids le plus elevé
    list_of_monoLinkNodes = [node for node in G.nodes if G.degree(node) == 1]
    weight = 0
    for start_nodes in list_of_monoLinkNodes:
        current_edge = str(G.edges(start_nodes, "weight", default=1))
        wt = int(current_edge.split(",")[2].strip(" ").strip(")]"))
        if wt > weight:
            best_node = start_nodes
            weight = wt



    # Tant qu'on a des noeuds avec des sorties
    while G.degree(best_node) != 0:
        # On cherche le meilleur noeud suivant
        weight = 0
        for u,v,wt in G.edges(best_node, "weight", default=1):
            print(str(u)+" "+str(v)+" "+" "+str(wt))
            if wt > weight:
                node1 = u
                node2 = v
                weight = wt
        print(str(node1)+" "+str(node2)+" "+" "+str(weight))
        # On ecrit le noeud "vieu", et on le supprime
        write_nextLine = False
        for line in input_fasta:
            if write_nextLine:
                output_fasta.write(line)
                write_nextLine = False
                input_fasta.seek(0)
                break
            if line.startswith(">"+str(best_node)):
                output_fasta.write(line)
                write_nextLine = True
        # On supprime l'arrete qu'on vient d'utiliser, et le noeud s'il n'a plus d'arrettes
        if best_node == node1:
            G.remove_edge(best_node,node2)
            if G.degree(best_node) == 0:
                G.remove_node(best_node)
            best_node = node2
        elif best_node == node2:
            G.remove_edge(node1,best_node)
            if G.degree(best_node) == 0:
                G.remove_node(best_node)
            best_node = node1
        if G.degree(best_node) == 0:
            write_nextLine = False
            for line in input_fasta:
                if write_nextLine:
                    output_fasta.write(line)
                    write_nextLine = False
                    input_fasta.seek(0)
                    break
                if line.startswith(">"+str(best_node)):
                    output_fasta.write(line)
                    write_nextLine = True
        print("On a fait 1 passage !!!")
    print("On a fait un chemin complet, on passe au point de depart suivant")
    print("nodes: " + str(G.number_of_nodes()))
    print("edges: " + str(G.number_of_edges()))
