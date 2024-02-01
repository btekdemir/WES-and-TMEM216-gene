import re

def extract_xp_words_from_file(filename):
    try:
        with open(filename, 'r') as file:
            
            newick_string = file.read()

           
            pattern = r'[XN]P_\d+\.\d+'


            
            xp_matches = re.findall(pattern, newick_string)

            return xp_matches
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


filename = "input.nwk"  

xp_words = extract_xp_words_from_file(filename)


def extract_sequences_from_fasta(input_fasta, xp_identifiers, output_fasta):
    try:
        with open(input_fasta, 'r') as input_file, open(output_fasta, 'w') as output_file:
            
            in_xp_list = False

            for line in input_file:
                
                if line.startswith('>'):
                   
                    identifier = line.strip()[1:]
                    index=identifier.find(" ")
                    aa=identifier[0:index]
                    in_xp_list = identifier[0:index] in xp_identifiers
                    

                    
                    if in_xp_list:
                        output_file.write(line)
                elif in_xp_list:
                   
                    output_file.write(line)

    except FileNotFoundError:
        print(f"Error: File '{input_fasta}' not found.")


input_fasta = "input.fasta"  
output_fasta = "output.fasta"  




extract_sequences_from_fasta("500.fas", xp_words, "output2.fasta")
