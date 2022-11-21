import random
import argparse

parser = argparse.ArgumentParser(description='Create random fasta file and apply mutations')
parser.add_argument('--FastaSize', help = "Taille de la sequence", required=False, default=30000000)

args = vars(parser.parse_args())

# Création des valeurs de bases : liste de nucleotides, liste d'evenements et taille du fichier fasta (nombre de caractères), Compteur de modifications pour connaitre la différence de taille entre sesquence initiale et finale
# Taukke minimale et maximale des évènements
Nucleotides = ["A","T","C","G"]
GC = ["G","C"]

FastaSize  = int(args['FastaSize'])



# Preparation des fichiers Output
ReferenceFile = open("Reference.fasta", "w")
FastaSeq=random.choices(Nucleotides, k=FastaSize)

ReferenceFile.write(''.join(map(str, FastaSeq)))
ReferenceFile.close()

# Création de la séquence de manière aléatoire
