# koura_transcriptome
step 1 run bbduk
step 2 merge overlapping reads
step 3 add merged reads to r1 file (from bbduk trimming)
step 4 run trinity
step 5 calculate trinity abundances
step 6 calculate exp matrices
step 7 calculate n50 and exn50
step 8 run busco

plot_exn50_r is an R script used to plot the output of exn50 from step 7 in Rstudio

