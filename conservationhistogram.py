conservation_scores = [sum(data.values()) for data in consensus_aminoacid_score.values()]
import matplotlib.pyplot as plt


plt.hist(conservation_scores, bins=20, color='blue', edgecolor='black')
plt.xlabel('Conservation Score')
plt.ylabel('Number of positions')
plt.title('Conservation Score Histogram')
plt.show()