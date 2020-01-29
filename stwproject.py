import pandas as pd
import numpy as np
import csv
from abc import ABC, abstractmethod 

df = pd.read_csv("gene_table.csv", delimiter=",")
#print(df)
#to read the dataset use read (Pandas)

class Project(ABC):

	@abstractmethod 	#part 2 needs abstract methods
	def record(self):	#remember to define the method everytime you implement a new class
		pass

class Number(Project):
#recording the numerical metadata consisting of the number of rows and columns of the dataset

	def record(self):
		return(df.shape)

class Semantics(Project):
#recording the general semantics of the dataset, i.e. the labels of the columns
	
	def record(self):
		return df.columns.values		#to get the labels of the rows --> df.index.values

#recording the number of genes for each biotype. The list should be sorted in ascending order;
#class Genes(Project):
	
	#def record(self):
		#return df.loc[:,'gene_biotype']
		#return df.groupby('gene_biotype').count()			#same as df.groupby(by='gene_biotype')
		#return df.loc[:,'gene_biotype'].sort_values(['count'], ascending=False)						
		#df.sort_values(by='gene_biotype', ascending=False)
	

#recording, given a certain biotype as input, the list of associated genes
class AssociatedGenes(Project):

	def record(self):
		return df.groupby('gene_biotype')['gene_name'].apply(lambda group_series:group_series.tolist())		#.reset_index()???
	
		
#recording the number of chromosomes in the dataset
#class Chromosomes(Project):

	#def record(self):
		#chm= set() 		#contains unique objects
		#unique=[]
		#for item in df:
			#if item not in chm:
			#	unique.append(item)
			#	chm.add(item)
		#return chm
		
		
		
		
		#df_c=df.loc[:,'chromosome']
		#for item in df_c:
		#	if item==df_c[:,:]:
		#		pass
		#	else:
		#		return 
		#return df_c

#recording the number of genes for each chromosome. The list should be sorted in ascending order
#class NumberOfGenes(Project):

	#def record(self):
		#return df.loc[:,'gene_name']
		

#recording, for each chromosome, the percentage of genes located on the + strand;
#class PlusStrand(Project):
#	def record(self):
#		return

#recording, for each chromosome, the percentage of genes located on the - strand
#class MinusStrand(Project):
#	def record(self):
#		return


#part1 has to manage these prints
#a=Number()					#instance:specific obj created from the class Number()
#print(a.record())
#a=Semantics()
#print(a.record())
#a=Genes()
#print(a.record())
#a=AssociatedGenes()
#print(a.record())
#a=Chromosomes()
#print(a.record())
#a=NumberOfGenes()
#print(a.record())

	
#groupby and sort_values
#filtering
		


