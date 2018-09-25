#!/usr/bin/env python3

from Bio import SeqIO

id_file = 'clustalo_input/phmmer_clustalo_trinity_IDs'
fasta_file = 'output/TransDecoder/Trinity.fasta.transdecoder.pep'
output_fasta = 'output/phmmer_clustalo_peptids.fasta'

def main():
    # read the id file
    with open(id_file, 'rt') as f:
        trinity_ids = [x.strip('\n') for x in f.readlines()]

    # filter the transdecoder peptides
    fasta_generator = SeqIO.parse(fasta_file, 'fasta')
    kept_records = [x for x in fasta_generator
                    if x.id in trinity_ids]

    # write the output
    SeqIO.write(kept_records, output_fasta, 'fasta')

if __name__ == '__main__':
    main()
