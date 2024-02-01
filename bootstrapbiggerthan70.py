
import re


def parse_nwk_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content



def process_nwk_file(file_path, min_bootstrap=0.7, pattern=r'[XN]P_\d+\.\d+'):
    # Regular expression to match species codes and bootstrap values
    regex = re.compile(r'\[&Bootstrap=(\d+\.\d+|\d+\.\d+|\d+)\]|([XN]P_\d+\.\d+)')

    with open(file_path, 'r') as file:
        input_nwk = file.read()

    matches = regex.finditer(input_nwk)
    current_bootstrap = None
    current_species_code = None
    output_nwk = input_nwk
    uneliminated_species = set()

    for match in matches:
        groups = match.groups()
        if groups[0] is not None:
            # Found a bootstrap value
            current_bootstrap = float(groups[0])
        elif groups[1] is not None:
            # Found a species code
            current_species_code = groups[1]
            uneliminated_species.add(current_species_code)
            if current_bootstrap is not None and current_bootstrap < min_bootstrap:
                # Remove clade if bootstrap is less than 0.7
                uneliminated_species.remove(current_species_code)

    return list(uneliminated_species)


# Example usage:

uneliminated_species_list = process_nwk_file("subtree_pruned1.nwk")


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




extract_sequences_from_fasta()

