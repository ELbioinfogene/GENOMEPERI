#Demo Script for Genome Peri module
#Eric Larsen 8/29/2021

#import module
import GENOMEPERI

#define address of data files
MY_DNA_FILE = 'C:\\DOCUMENTS\\A_DNA.TXT'
#Define Subject Name
NAME_A = 'ADAM'
#23&Me type = 0
#Ancestry.com type = 1
A_TYPE = 0

A00 = GENOMEPERI.SNP_GENOME(NAME_A,MY_DNA_FILE,A_TYPE)

#perform sequence quality check
A00.SEQUENCEQC()
print(f'Subject {A00.NAME} depth score: {A00.READ_DEPTH}')

#input Additional Individual(s)
ANOTHER_DNA_FILE = 'C:\\DOCUMENTS\\S_DNA.TXT'
NAME_B = 'STEVEN'
B_TYPE = 1
S01 = GENOMEPERI.SNP_GENOME(NAME_B,ANOTHER_DNA_FILE,B_TYPE)
S01.SEQUENCEQC()
print(f'Subject {S01.NAME} depth score: {S01.READ_DEPTH}')

#make comparisons between individuals
COMPARE_A_S = GENOMEPERI.GENOME_COMPARE(A00,S01)
#output is a list where [0] is the subject names
#[1] is a score of genotype matches
#[2] is the number of SNPs both genomes have in common
#[3] is the identity score ([1]/[2])
#[4] is the match depth of subject A ([2]/subjectA.TOTAL_READS)
#[5] is the match depth of subject B ([2]/subjectB.TOTAL_READS)

print(f'{COMPARE_A_S[0]} has approximately {COMPARE_A_S[4]} overlap with {COMPARE_A_S[3]} identity')
