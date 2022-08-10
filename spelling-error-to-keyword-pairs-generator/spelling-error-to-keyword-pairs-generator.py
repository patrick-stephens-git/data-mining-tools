## Import Module Requirements:
import pandas as pd
import Levenshtein

## Import Variables via Files from Directory:
from configurationVariables import input_csv_filename

################### 
# Function Library:
def keyword_spelling_error_pair_generator(df):
    ## Use Levenshtein Distance to Return Keywords Sequences w/ Spelling Difference of <= 2 Characters:
    pair_id_df = df['ID']
    df = df.assign(levenshtein_difference=pair_id_df.drop_duplicates(keep='last').map(df.groupby(pair_id_df)['Keyword'].apply(lambda x: Levenshtein.distance(x.iloc[0], x.iloc[-1]))))
    df = df.fillna(method='bfill')
    df = df[df['levenshtein_difference'] <= 2.0]
    df = df[~df['Keyword'].str.contains(r'\d')] # Removes Keywords with Numbers (16, 17, 18 years old etc...)

    ## Pair Keywords per ID
    df = df.groupby('ID').apply(lambda g: g['Keyword'].values)
    df = df.to_frame().reset_index()

    ## Split Query Pairs into Separate Columns
    df = pd.DataFrame(df[0].tolist())
    df.insert(2, 2, 1)
    df.rename(columns={0:'Keyword Sequence 1', 
                       1:'Keyword Sequence 2', 
                       2:'Count'}, inplace=True)

    ## Group Duplicates Column Values, Sum Counts:
    df = df.groupby(['Keyword Sequence 1', 'Keyword Sequence 2'], as_index=False)['Count'].sum()
    df = df.sort_values(by='Count', ascending=True)

    ## Drop Rows with Duplicate Values between Keyword Sequence 1 and Keyword Sequence 2:
    duplicates_list = []
    for index, row in df.iterrows():
        q1 = row['Keyword Sequence 1']
        q2 = row['Keyword Sequence 2']
        if q1 == q2:
            value = 'True'
            duplicates_list.append(value)
        else:
            value = 'False'
            duplicates_list.append(value)
    duplicates_df = pd.DataFrame(duplicates_list, columns=['Duplicate?'])

    df = pd.concat([df, duplicates_df], axis=1)
    df = df[df['Duplicate?'].str.contains('True') == False] # Drops rows that have duplicates
    df = df.drop(columns='Duplicate?').sort_values(by=['Keyword Sequence 2','Count'], ascending=[False, False])
    return df

df = pd.read_csv(input_csv_filename)
df = keyword_spelling_error_pair_generator(df)

df.to_csv('output-spelling-error-keyword-pairs.csv', index=False)
