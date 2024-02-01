import pandas as pd
import plotly.express as px

df = pd.read_csv('output3.tsv', sep='\t')

df.columns = ["Position", "ConsensusAminoAcid", "ConservationScore"]

fig = px.scatter(df, x='Position', y='ConservationScore', color='ConservationScore',
                 title='Conservation Scores', labels={'Position': 'Position', 'ConservationScore': 'Conservation Score'},
                 color_continuous_scale='Viridis')

fig.add_trace(px.line(df, x='Position', y='ConservationScore').data[0])
fig.write_html("conservation_scores_pruned_s=500.html")