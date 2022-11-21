
import pandas as pd
import upsetplot
from matplotlib import pyplot

set1=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40494/cdnaFlyeGoodGenes.txt","r").readlines()
set2=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40494/cdnaWtdbg2GoodGenes.txt","r").readlines()
set3=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40499/cdnaFlyeGoodGenes.txt","r").readlines()
set4=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40499/cdnaWtdbg2GoodGenes.txt","r").readlines()
set5=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40602/cdnaFlyeGoodGenes.txt","r").readlines()
set6=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40602/cdnaWtdbg2GoodGenes.txt","r").readlines()
set7=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40753/cdnaFlyeGoodGenes.txt","r").readlines()
set8=open("/home/cbirbes/Documents/Scripts/ASMGene/VerfiBovinCLR/testVerif/40753/cdnaWtdbg2GoodGenes.txt","r").readlines()
# set1=open("40494cdnaFlyeListGenes.txt","r").readlines()
# set2=open("40494cdnaWtdbg2ListGenes.txt","r").readlines()
# set3=open("40496cdnaFlyeListGenes.txt","r").readlines()
# set4=open("40496cdnaWtdbg2ListGenes.txt","r").readlines()
# set5=open("40499cdnaFlyeListGenes.txt","r").readlines()
# set6=open("40499cdnaWtdbg2ListGenes.txt","r").readlines()
# set7=open("40501cdnaFlyeListGenes.txt","r").readlines()
# set8=open("40501cdnaWtdbg2ListGenes.txt","r").readlines()
# set9=open("40505cdnaFlyeListGenes.txt","r").readlines()
# set10=open("40505cdnaWtdbg2ListGenes.txt","r").readlines()
# set11=open("40534cdnaFlyeListGenes.txt","r").readlines()
# set12=open("40534cdnaWtdbg2ListGenes.txt","r").readlines()
# set13=open("40539cdnaFlyeListGenes.txt","r").readlines()
# set14=open("40539cdnaWtdbg2ListGenes.txt","r").readlines()
# set15=open("40550cdnaFlyeListGenes.txt","r").readlines()
# set16=open("40550cdnaWtdbg2ListGenes.txt","r").readlines()
# set17=open("40551cdnaFlyeListGenes.txt","r").readlines()
# set18=open("40551cdnaWtdbg2ListGenes.txt","r").readlines()
# set19=open("40572cdnaFlyeListGenes.txt","r").readlines()
# set20=open("40572cdnaWtdbg2ListGenes.txt","r").readlines()
# set21=open("40618cdnaFlyeListGenes.txt","r").readlines()
# set22=open("40618cdnaWtdbg2ListGenes.txt","r").readlines()
# set23=open("40627cdnaFlyeListGenes.txt","r").readlines()
# set24=open("40627cdnaWtdbg2ListGenes.txt","r").readlines()
# set25=open("40749cdnaFlyeListGenes.txt","r").readlines()
# set26=open("40749cdnaWtdbg2ListGenes.txt","r").readlines()
# set27=open("41230cdnaFlyeListGenes.txt","r").readlines()
# set28=open("41230cdnaWtdbg2ListGenes.txt","r").readlines()

set_names = ['OTEDOR - F', 'OTEDOR - W', 'OCLUCY - F', 'OCLUCY - W', 'OLIVET - F','OLIVET - W','NIPON - F', 'NIPON - W']
sets = [set1, set2, set3, set4, set5, set6, set7, set8]
# set_names = ['494F', '494W', '496F','496W']
# sets = [set1, set2, set3, set4]
#set_names = ['494F', '494W', '496F','496W','499F','499W','501F','501W','505F','505W','534F','534W','539F','539W','550F','550W','551F','551W','572F','572W','618F','618W','527F','527W','749F','749W','230F','230W']
#sets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28]
all_elems = list(set().union(*sets))
df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
df_up = df.groupby(set_names).size()
#upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000, min_subset_size=10)
upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, min_subset_size=10)
pyplot.savefig('figure1.svg',dpi=600)
pyplot.clf()
upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000, min_subset_size=10)
pyplot.savefig('figure2.svg',dpi=600)
#
# set_names = ['499F','499W','501F','501W']
# sets = [set5, set6, set7, set8]
# all_elems = list(set().union(*sets))
# df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
# df_up = df.groupby(set_names).size()
# print(df_up)
# upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000)
# pyplot.savefig('figure2.png',dpi=600)
#
# set_names = ['505F','505W','534F','534W']
# sets = [set9, set10, set11, set12]
# all_elems = list(set().union(*sets))
# df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
# df_up = df.groupby(set_names).size()
# print(df_up)
# upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000)
# pyplot.savefig('figure3.png',dpi=600)
#
# set_names = ['539F','539W','550F','550W']
# sets = [set13, set14, set15, set16]
# all_elems = list(set().union(*sets))
# df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
# df_up = df.groupby(set_names).size()
# print(df_up)
# upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000)
# pyplot.savefig('figure4.png',dpi=600)
#
# set_names = ['551F','551W','572F','572W']
# sets = [set17, set18, set19, set20]
# all_elems = list(set().union(*sets))
# df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
# df_up = df.groupby(set_names).size()
# print(df_up)
# upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000)
# pyplot.savefig('figure5.png',dpi=600)
#
# set_names = ['618F','618W','527F','527W']
# sets = [set21, set22, set23, set24]
# all_elems = list(set().union(*sets))
# df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
# df_up = df.groupby(set_names).size()
# print(df_up)
# upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000)
# pyplot.savefig('figure6.png',dpi=600)
#
# set_names = ['749F','749W','230F','230W']
# sets = [set25, set26, set27, set28]
# all_elems = list(set().union(*sets))
# df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
# df_up = df.groupby(set_names).size()
# print(df_up)
# upsetplot.plot(df_up, orientation='horizontal', sort_by='cardinality', show_counts=True, max_subset_size=5000)
# pyplot.savefig('figure7.png',dpi=600)
