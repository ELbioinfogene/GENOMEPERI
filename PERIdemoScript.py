#Demo Script for Genome Peri module
#Eric Larsen 8/28/2021

#import module
import GENOMEPERI

#define address of data files
MY_DNA_FILE = 'C:\\DOCUMENTS\\A_DNA.TXT'
#Define Subject Name
NAME_1 = 'ADAM'
#23&Me type = 0
#Ancestry.com type = 1
TYPE_1 = 0

A00 = GENOMEPERI.SNP_GENOME(NAME_1,MY_DNA_FILE,TYPE_1)

#perform sequence quality checks
A00.SEQUENCEQC()
print(f'Subject {A00.NAME} depth score: {A00.READ_DEPTH}')

#input Additional Individual(s)
ANOTHER_DNA_FILE = 'C:\\DOCUMENTS\\S_DNA.TXT'
NAME_2 = 'STEVEN'
TYPE_2 = 1
S01 = GENOMEPERI.SNP_GENOME(NAME_2,ANOTHER_DNA_FILE,TYPE_2)
S01.SEQUENCEQC()
print(f'Subject {S01.NAME} depth score: {S01.READ_DEPTH}')

#make comparisons between individuals
COMPARE_A_S = GENOMEPERI.GENOME_COMPARE(A00,S01)
