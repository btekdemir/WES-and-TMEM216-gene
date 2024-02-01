- Step 1:
  
scp /data/patientX_1.fq.gz /group5/workingDir
scp /data/patientX_2.fq.gz /group5/workingDir
gunzip -k patientX_1.fq.gz
gunzip -k patientX_2.fq.gz

Explanation: "PatientX_1.fq.gz" and "PatientX_2.fq.gz" files were transferred using the "scp" command and subsequently extracted with the "gunzip" command.

- Step 2:
  
mv patientX_2.fastq FastQC/
./fastqc patientX_1.fastq
mv patientX_1.fastq FastQC/
./fastqc patientX_2.fastq

Explanation: For quality control of data, FastQC tool is used. Quality check is done.

- Step 3:
  
cutadapt -a AAGTCGGAGGCCAAGCGGTCTTAGGAAGACAA -AAAGTCGGATCGTAGCCATGTCGTTCTGTGAGCCAAGGAGTTGV -o cutted.1.fastq -p cutted.2.fastq patientX_1.fastq patientX_2.fastq

Explanation: The “cutadpt” command is used for trimming adaptor in sequence data.

- Step 4:
  
wget ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/

Explanation: Reference genom data is uploaded to server.

- Step 5:
  
bwa index refrence3.fasta

Explanation: The reference file is indexed.

- Step 6:
  
bwa mem -t 16 refrence3.fasta cutted.1.fastq cutted.2.fastq > aligned.sam

Explanation: This command is used for alignment. "16" represents the number of core that is used in the allignment.

- Step 7:
  
bwa mem -t 16 GRCh38.primary_assembly.genome.fa cutted.1.fastq cutted.2.fastq > aligned_new.sam

samtools view -bS -@ 16 aligned_new.sam -o aligned_new.bam

samtools sort -@ 16 -o sorted.bam aligned_new.bam

samtools index -@ 16 sorted.bam

samtools rmdup sorted.bam deduplicated_new.bam

samtools sort -@ 16 -o sorted_deduplicated.bam deduplicated_new.bam

samtools index -@ 16 sorted_deduplicated.bam

samtools faidx GRCh38.primary_assembly.genome.fa

gatk CreateSequenceDictionary -R GRCh38.primary_assembly.genome.fa -O GRCh38.primary_assembly.genome.dict

samtools addreplacerg -r ‘@RG \tID:samplename\tSM:samplename’ -@ 8 -o OUT.bam sorted_deduplicated.bam

samtools index --threads 8 /disk2/ens210/group5/workingDir/OUT.bam

gatk --java-options "-Xmx50g" HaplotypeCaller -R GRCh38.primary_assembly.genome.fa -I OUT.bam -O output.vcf

Explanation: In order, first, sam is converted to bam. Then, bam file is sorted. After that, the sorted bam is indexed. Then, duplicates are removed from the sorted bam. After that, the bam whose duplicates are removed is sorted. Finally, the sorted bam whose duplicates are removed is indexed. Then, the reference is indexed by samtool. A dictionary for sequence is created. After that, read groups are changed with add and replace command of the read groups. Output file indexed again. Lastly, variant calling performed.

- Step 8:
  
java -jar snpEff.jar -v -classic -lof -stats output.html GRCh38.105 /disk2/ens210/group5/workingDir/filteredvariants.vcf > annotated_output_new.vcf

Explanation:  Annotation of variants performed with snpEfff tool’s classic and lof tag annotation model.

- Step 9:
  
awk -F'\t' 'NR==1 || $5 != 0' output.genes.txt > highimpactdata.txt

Explanation: If variant_impact_high column is different than 0, and as it increases, it is assumed that the variant is high impacted variant.

awk -F'\t' '$14 != 0' highimpactdata.txt > filtered_data_frame_shift.txt

Explanation:  If variant is associated to frame shift, they collected to a new file.

awk -F'\t' 'NR==1; NR>1 {print $0 | "sort -t'\t' -k18,18nr"}' filtered_data_frame_shift.txt > sortedframeshiftWITHnonsynm.txt

Explanation: According to variants_effect_NON_SYNONYMOUS_CODING column, non-synonymous variants collected to a new file, and it is observed that this file has 148 unique genes, which have variants. 
