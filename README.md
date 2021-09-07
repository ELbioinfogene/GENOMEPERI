# GENOMEPERI
Python Module for handling SNP txt data
This module can read txt files created by either 23&Me or Ancestry.com

The resulting SNP_GENOME object has a list RSINDEX which can be used to call SNP data from the dictionary GENOME
SNP_GENOME objects have two dictionaries: .GENOME and .CHROMOSOME_COUNT_LOG
.GENOME is searcheable by RSID string and gives a SNP result if there is no KeyError
.CHROMOSOME_COUNT_LOG is searchable by Chromosome ID integer (see below) - if gives the total number of SNPs that reside on that chromosome

The object method SEQUENCEQC() evaluates the SNP_GENOME and gives a score of how many SNPS have both alleles properly read (A,T,C,or G)

The function GENOME_COMPARE looks at two SNP_GENOMEs and scores the identity of matched RSIDs

Note on Chromosome ID number: All reads on Chromsome X are marked as Chromosome 23, Y is 24 and Mitochondria is 26
The 23&Me data I have uses strings 'X', 'Y', and 'MT' - however my datasets are both from males
My Ancestry.com dataset uses integers 23 AND 25 for X - this is my female dataset
SNP_GENOME objects use integers to harmonize these different formats, however all 
Chromosome X reads are consolidated - a future feature could be separate X identities to determine multigeneration inheritance. 
If you are using 23&Me data from a female and have more information feel free to contact me so I can have the code handle this.
