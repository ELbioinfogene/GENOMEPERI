# GENOMEPERI
Python Module for handling SNP txt data
This module can read txt files created by either 23&Me or Ancestry.com

The resulting SNP_GENOME object has a list RSINDEX which can be used to call SNP data from the dictionary GENOME

The object method SEQUENCEQC() evaluates the SNP_GENOME and gives a score of how many SNPS have both alleles properly read (A,T,C,or G)

The function GENOME_COMPARE looks at two SNP_GENOMEs and scores the identity of matched RSIDs
