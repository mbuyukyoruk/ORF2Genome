# ORF2Genome

Author: Murat Buyukyoruk

        ORF2Genome help:

This script is developed to fetch genome sequences from prodigal accessions. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        python ORF2Genome.py -i demo.fasta -l demo_sub_list.txt -o demo_sub_list.fasta

ORF2Genome dependencies:

Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download

tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file. FASTA file requires headers starting with accession number. (i.e. >NZ_CP006019 [fullname])

	-l/--list		List			Specify a list of ORF accession from PRODIGAL run (Accession only). Each accession should be included in a new line (i.e. generated with Excel spreadsheet).

	-o/--output		output file		Specify a output file name that should contain fetched genome.
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.
	
