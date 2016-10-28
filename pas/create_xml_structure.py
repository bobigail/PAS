# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 22:11:48 2016

@author: bobigail
"""
"""
Create XML files. Input is a dictionary of Uniprot IDs and the list of associated PDB files.

"""
from xml.etree.ElementTree import *


PAS_DATABASE = Element('PAS_DATABASE')

PAS = SubElement(PAS_DATABASE, 'PAS')
PAS.text = "{**UNIPROT_ID_GOES_HERE}"

pdb_id = SubElement(PAS, 'pdb_id')
pdb_id.text = "{**PDB_ID_GOES_HERE}"

entity_src_gen = SubElement(pdb_id, 'entity_src_gen')
entity_src_gen.text = "{**ENTITY_ID_GOES_HERE}"

gene_src_genus = SubElement(entity_src_gen, 'gene_src_genus')
gene_src_genus.text = "{**GENUS}"

gene_src_scientific_name = SubElement(entity_src_gen, 'gene_src_scientific_name')


gene_src_ncbi_taxonomy_id = SubElement(entity_src_gen, 'gene_src_ncbi_taxonomy_id')
host_org_genus = SubElement(entity_src_gen, 'host_org_genus')
host_org_scientific_name = SubElement(entity_src_gen, 'host_org_scientific_name')
host_org_ncbi_taxonomy_id = SubElement(entity_src_gen, 'host_org_ncbi_taxonomy_id')
host_org_vector = SubElement(entity_src_gen, 'host_org_vector')


protein_type = SubElement(pdb_id, 'protein_type')

type_of_protein = SubElement(protein_type, 'type_of_protein')
other_type_keywords = SubElement(protein_type, 'other_type_keywords')

protein_structure = SubElement(pdb_id, 'protein_structure')

atom_site = SubElement(protein_structure, 'atom_site')

B_iso_or_equiv = SubElement(atom_site, 'B_iso_or_equiv')
Cartn_x = SubElement(atom_site, 'Cartn_x')
Cartn_y = SubElement(atom_site, 'Cartn_y')
Cartn_z = SubElement(atom_site, 'Cartn_z')

auth_asym_id = SubElement(atom_site, 'auth_asym_id')
auth_atom_id = SubElement(atom_site, 'auth_atom_id')
auth_comp_id = SubElement(atom_site, 'auth_comp_id')
auth_seq_id = SubElement(atom_site, 'auth_seq_id')

label_asym_id = SubElement(atom_site, 'label_asym_id')
label_atom_id = SubElement(atom_site, 'label_atom_id')
label_comp_id = SubElement(atom_site, 'label_comp_id')
label_entity_id = SubElement(atom_site, 'label_entity_id')


seq_one_letter_code = SubElement(protein_structure, 'seq_one_letter_code')
seq_one_letter_code_can = SubElement(protein_structure, 'seq_one_letter_code_can')

mutation = SubElement(protein_structure, 'mutation')

binding_details = SubElement(pdb_id, 'binding_details')

residue_id = SubElement(binding_details, 'residue_id')
author_seq_id = SubElement(binding_details, 'author_seq_id')
residue_name = SubElement(binding_details, 'residue_name')
label_seq_id = SubElement(binding_details, 'label_seq_id')

number_of_chains = SubElement(pdb_id, 'number_of_chains')

ligand_info = SubElement(pdb_id, 'ligand_info')

entity_nonpoly = SubElement(ligand_info, 'entity_nonpoly')
comp_id = SubElement(ligand_info, 'comp_id')
name = SubElement(ligand_info, 'name')

other_ligand = SubElement(ligand_info, 'other_ligand')

struct_connCategory = SubElement(pdb_id, 'struct_connCategory')

struct_conn = SubElement(struct_connCategory, 'struct_conn')

dist_value = SubElement(struct_conn, 'dist_value')
ptnr1_auth_comp_id = SubElement(struct_conn, 'ptnr1_auth_comp_id')
ptnr1_auth_seq_id = SubElement(struct_conn, 'ptnr1_auth_seq_id')
ptnr1_label_asym_id = SubElement(struct_conn, 'ptnr1_label_asym_id')
ptnr1_label_atom_id = SubElement(struct_conn, 'ptnr1_label_atom_id')
ptnr1_label_comp_id = SubElement(struct_conn, 'ptnr1_label_comp_id')

ptnr2_auth_comp_id = SubElement(struct_conn, 'ptnr2_auth_comp_id')
ptnr2_auth_seq_id = SubElement(struct_conn, 'ptnr2_auth_seq_id')
ptnr2_label_asym_id = SubElement(struct_conn, 'ptnr2_label_asym_id')
ptnr2_label_atom_id = SubElement(struct_conn, 'ptnr2_label_atom_id')
ptnr2_label_comp_id = SubElement(struct_conn, 'ptnr2_label_comp_id')

ElementTree(PAS_DATABASE).write(sys.stdout)




