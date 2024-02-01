# ens210-2023-group-project-group5
Reports:
- Project 2 Final Report in .docx format: ENS210-Group5-Final_Report.docx
- Project 2 Final Report in .pdf format: ENS210-Group5-Final_Report.pdf
- Project 2 Final Report Revised in .pdf format: ENS 210_Group5_Final_Report_Revisedversion.pdf
- Project 2 Final Report Revised in .docx format: ENS 210_Group5_Final_Report_Revisedversion.docx
- Project 1 Report in .pdf format: ens210-report.pdf

Methods File:
- method.md (for Project 2)
- group_commands.md (for Project 1)

File Informations:

Python and R Codes:
- Changing Subtree from nwk format to fasta: subtreetofastasequences.py
- Conservation score information to histogram table: conservationhistogram.py
- Calculating conservation score and determining the consensus sequence: conservation_consensus_code.py
- Obtaining FASTA file for construction of last tree (If Bootstrap value is >= 0.7): bootstrapbiggerthan70.py
- Obtaining output.tsv file: txtTOtsvfileforFirst.py
- Obtaining output2.tsv file: txtTOtsvfileforSecond.py
- Obtaining output3.tsv file: txtTOtsvfileforThird.py
- Mapping original sequence to aligned sequence: map_mutations_positions.py
- Getting threshold values for classification: known_mutations.py
- Obtaining variant analyses for the data in the gnomAD to classify all of the variants for Pathogenicity: gnomadVarAnalysis.py
- Getting p-values with t-test statistical analysis: ttest.py
- Creating Conservation Scores per position scatter plot with a line plot overlaid code: cons_per_position.py
- Creating Conservation Scores and Allele Frequency scatter plot of mutations for 500 hits data: output.R
- Creating Conservation Scores and Allele Frequency scatter plot of mutations for subtree data: output2.R
- Creating Conservation Scores and Allele Frequency scatter plot of mutations for pruned subtree data: output3.R

Tables:
- Histogram table of the First tree: conservationFirsthistogram.jpg
- Histogram table of the Second tree: conservationSecondhistogram.jpg
- Histogram table of the Third tree: conservationThirdhistogram.jpg
- Conservation Scores and Allele Frequency scatter plot of mutations for 500 hits: output.csv.pdf
- Conservation Scores and Allele Frequency scatter plot of mutations for subtree: output2.csv.pdf
- Conservation Scores and Allele Frequency scatter plot of mutations for pruned subtree: output3.csv.pdf
- Conservation Scores per position scatter plot with a line plot overlaid for First Tree: conservation_scores_s=500.pdf
- Conservation Scores per position scatter plot with a line plot overlaid for Second Tree: conservation_scores_subtree_s=500.pdf
- Conservation Scores per position scatter plot with a line plot overlaid for Third Tree: conservation_scores_pruned_s=500.pdf

Conservation Scores and Consensus Sequences:
- Scores for the First Tree: output.tsv
- Scores and Sequence for the First Tree: conservationFirst.txt
- Scores for the Second Tree: output2.tsv
- Scores and Sequence for the Second Tree: conservationSecond.txt
- Scores for the Third Tree: output3.tsv
- Scores and Sequence for the Third Tree: conservationThird.txt

p-values:
- p-values obtained with t-test: results_ttest.txt

Threshold Values:
- Threshold values obtained with known_mutations.py code: conservation_thresholds.txt

After the Classification of Data:
- Classification of gnomAD data according to conservation scores of First Tree: classification_output.tsv
- Classification of gnomAD data according to conservation scores of Second Tree: classification_output2.tsv
- Classification of gnomAD data according to conservation scores of Third Tree: classification_output3.tsv
  
Data for Variants:
- gnomAD all variants data: gnomAD_all.csv
- gnomAD Pathogenic and Likely Pathogenic variants: gnomADonlyPathogenic.csv
- Known variants from the papers: paper_mutations.txt

TMEM216 .faa File Obtained From UniProt:
- TMEM216 Homo Sapiens file which then used in BLASTP: protein.faa

First Tree Construction Step:
- 500 Hits FASTA file which obtained from BLASTP: 500.fas
- 500 file which aligned in MEGA for MEG format: 500_aligned.meg
- 500 file which aligned in MEGA for FASTA format: 500_aligned.fas
- 500 tree made in MEGA: 500_MEGA_newicktree.nwk
- PDF file of tree in MEGA: 500_MEGA_tree.pdf
- 500 constructed tree in Figtree version: 500_FigTree_unrooted.nwk
- PDF file of tree in Figtree: 500_FigTree_unrooted_tree.pdf
- 500 constructed tree in Figtree version(midpoint rooted): 500_FigTree_rooted_tree.nwk
- PDF file of tree in Figtree: 500_FigTree_rooted_tree.pdf

Second Tree Construction Step:
- Subtree decided from the previous tree in Newick format to obtain new fasta file of sequences: subtree.nwk
- 500 Hits subtree FASTA file: 500subtree.fas
- 500 subtree file which aligned in MEGA for MEG format: 500subtree_aligned.meg
- 500 subtree file which aligned in MEGA for FASTA format: 500subtree_aligned_fasta.fas
- 500 subtree made in MEGA: 500subtree_aligned_tree.nwk
- PDF file of tree in MEGA: 500subtree_aligned_tree_pdf.pdf
- 500 subtree constructed tree in Figtree version(midpoint rooted): 500subtree_aligned_tree_Figtree.nwk
- PDF file of tree in Figtree: 500subtree_aligned_tree_Figtree_pdf.pdf

Third Tree Construction Step:
- Subtree decided from the previous tree in Newick format to obtain new fasta file of sequences: subtree_pruned1.nwk
- 500 Hits pruned subtree FASTA file: 500subtree_pruned.fasta
- 500 pruned subtree file which aligned in MEGA for MEG format: 500subtree_pruned_aligned.meg
- 500 pruned subtree file which aligned in MEGA for FASTA format: 500subtree_pruned_aligned.fas
- 500 pruned subtree made in MEGA: 500subtree_pruned_tree.nwk
- 500 pruned subtree constructed tree in Figtree version(midpoint rooted): 500subtree_pruned_Figtree.nwk
- PDF file of tree in Figtree: 500subtree_pruned_Figtree_pdf.pdf
