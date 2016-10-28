# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:04:35 2016

@author: bobigail
"""
""" Takes input of a uniprot table with tab separated values. returns a folder
containing pdb files
"""

# deals woith text in tab separated values
import csv

with open("uniprot_data.tab") as tsv: #tab separated value
    for line in csv.reader(tsv, dialect="excel-tab"):
        uniprot_id = line[0]
        pdb_list = line[1][:-1].split(";")
        #print uniprot_id + " has " + str(len(pdb_list)) + " pdbs"
        
    
uniprot_pdb = {}
with open("uniprot_data.tab") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        uniprot_pdb[line[0]] = line[1][:-1].split(";")
print(uniprot_pdb)

print len(uniprot_pdb)


from prody import *
from pylab import *

pathPDBFolder("../PDBs")
pdbs_to_get_listoflists = uniprot_pdb.values()
pdbids = [item for sublist in pdbs_to_get_listoflists for item in sublist]
print (pdbids)
print len(pdbids)

pdbfiles = fetchPDB(*pdbids, copy=False)