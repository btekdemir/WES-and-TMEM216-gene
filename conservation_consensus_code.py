def fastareader(filename):
    seqDict = {}
    with open(filename,'r') as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                sequence = line[1:]
                seqDict[sequence] = ""
            else:
                seqDict[sequence] += line
    return seqDict



def fastareader(filename):
    seq_dict = {}
    with open(filename, 'r') as file:
        current_sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_sequence = line[1:]
                seq_dict[current_sequence] = ""
            else:
                seq_dict[current_sequence] += line
    return seq_dict

filename = 
sequence_dict = fastareader(filename)
alignment_sequences = list(sequence_dict.values())
amino_acids = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]

consensus_sequence = ""
consensus_scores = {}
for position in range(len(alignment_sequences[0])):
    amino_acid_percentages = dict.fromkeys(amino_acids, 0)
    amino_acids_at_position = ""
    for seq in alignment_sequences:
        amino_acids_at_position += seq[position]
    for amino_acid in amino_acids:
        count_amino_acid = amino_acids_at_position.count(amino_acid)
        amino_acid_percentages[amino_acid] = count_amino_acid / len(alignment_sequences)
    amino_acid_percentages = dict(sorted(amino_acid_percentages.items(), key=lambda x: x[1], reverse=True))
    consensus_amino_acid = list(amino_acid_percentages.keys())[0]
    max_amino_acid_score = list(amino_acid_percentages.values())[0]
    consensus_sequence += consensus_amino_acid
    consensus_scores[position] = {consensus_amino_acid: max_amino_acid_score}

print("Consensus Sequence:", consensus_sequence)
print("\nAmino Acid Scores:")
for pos, data in consensus_scores.items():
    print(f"Position {pos + 1}: {data}")




conservation_scores = [sum(data.values()) for data in consensus_scores.values()]
import matplotlib.pyplot as plt


plt.hist(conservation_scores, bins=20, color='blue', edgecolor='black')
plt.xlabel('Conservation Score')
plt.ylabel('Number of positions')
plt.title('Conservation Score Histogram')
plt.show()


