#!/bin/env python

joined1 = open("joined1.txt","r")
joined2 = open("joined2.txt","r")

Hap1Only = open("Hap1.txt","w")
Hap2Only = open("Hap2.txt","w")
Both = open("Both.txt","w")

for line in joined1:
    try:
        hap1 = line.strip("\t").split(" ")[1]
    except:
        Hap1Only.write("Pas present dans Hap1 : "+str(line.strip("\t").split(" ")[0])+("\n"))
        hap1 = 0
    try:
        hap2 = line.strip("\t").split(" ")[2]
    except:
        Hap2Only.write("Pas present dans Hap2 : "+str(line.strip("\t").split(" ")[0])+("\n"))
        hap2 = 0
    if int(hap1) > 3*(int(hap2)) and hap2 != 0:
        Hap1Only.write(str(line.strip("\t").split(" ")[0] + " " +str(hap1)+" "+str(hap2)))
    elif int(hap2) > 3*(int(hap1)) and hap1 != 0:
        Hap2Only.write(str(line.strip("\t").split(" ")[0] + " " +str(hap1)+" "+str(hap2)))
    else:
        Both.write(str(line.strip("\t").split(" ")[0] + " " +str(hap1)+" "+str(hap2)))

Hap1Only = open("2Hap1.txt","w")
Hap2Only = open("2Hap2.txt","w")
Both = open("2Both.txt","w")

for line in joined2:
    try:
        hap1 = line.strip("\t").split(" ")[1]
    except:
        Hap1Only.write("Pas present dans Hap1 : "+str(line.strip("\t").split(" ")[0])+("\n"))
        hap1 = 0
    try:
        hap2 = line.strip("\t").split(" ")[2]
    except:
        Hap2Only.write("Pas present dans Hap2 : "+str(line.strip("\t").split(" ")[0])+("\n"))
        hap2 = 0
    if int(hap1) > 3*(int(hap2)) and hap2 != 0:
        Hap1Only.write(str(line.strip("\t").split(" ")[0] + " " +str(hap1)+" "+str(hap2)))
    elif int(hap2) > 3*(int(hap1)) and hap1 != 0:
        Hap2Only.write(str(line.strip("\t").split(" ")[0] + " " +str(hap1)+" "+str(hap2)))
    else:
        Both.write(str(line.strip("\t").split(" ")[0] + " " +str(hap1)+" "+str(hap2)))
