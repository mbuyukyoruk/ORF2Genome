import argparse
import sys
import os
import subprocess
import re
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python seq_fetch.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

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

	-o/--output		output file	    Specify a output file name that should contain fetched genome.
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.
	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a original fasta file.\n')
parser.add_argument('-l', '--list', required=True, type=str, dest='list',
                    help='Specify a list of accession numbers to fetch.\n')
parser.add_argument('-o', '--output', required=True, dest='out',
                    help='Specify a output fasta file name.\n')

results = parser.parse_args()
filename = results.filename
list = results.list
out = results.out

seq_id_list = []
seq_list = []
seq_description_list = []

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Reading...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        seq_id_list.append(record.id)
        seq_list.append(record.seq)
        seq_description_list.append(record.description)

proc = subprocess.Popen("wc -l < " + list, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length+1)) as pbar:
    pbar.set_description('Writing...')
    with open(list, 'r') as file:
        for line in file:
            pbar.update()
            if "accession" not in line:
                if len(line.split()) != 0:
                    acc = line.split('\n')[0]
                    genome_acc = line.rsplit('_',1)[0].split("\n")[0]
                try:
                    ind = seq_id_list.index(genome_acc)
                    f = open(out, 'a')
                    sys.stdout = f
                    print(">" + genome_acc + " | " + seq_description_list[ind])
                    print(re.sub("(.{60})", "\\1\n", str(seq_list[ind]), 0, re.DOTALL))
                except:
                    # print acc
                    continue
