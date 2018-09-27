# koura_transcriptome

step 1 run bbduk

step 2 merge overlapping reads

step 3 add merged reads to r1 file (from bbduk trimming)

step 4 run trinity

step 5 calculate trinity abundances

step 6 calculate exp matrices

step 7 calculate n50 and exn50

step 8 run busco

step 9 run trinotate for annotation

step 10 run 1st clustalo to creat aligned all hox genes file

step 11 get fasta records of transcript IDed from 1st clustalo

Step 12 run second culstalo aligning hox genes to transcripts

step 13 run trimal to trim alignment

step 14 make phylogenetic tree of aligned things

step 15 obtian stats form trinotate txt file


plot_exn50_r is an R script used to plot the output of exn50 from step 7 in Rstudio

