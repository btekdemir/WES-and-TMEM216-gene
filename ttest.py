from scipy import stats as st
import pandas as pd 


outputList=["classification_output.csv","classification_output2.csv","classification_output3.csv"]
for i in outputList:
    df = pd.read_csv(i)

    a = df.loc[df['isPathogenic'] == True, 'Allele_frequency'].to_numpy()
    b = df.loc[df['isPathogenic'] == False, 'Allele_frequency'].to_numpy()

    pvalue = st.ttest_ind(a=a, b=b, equal_var = True).pvalue

    print(f"P-value for {i}: {pvalue}")
    