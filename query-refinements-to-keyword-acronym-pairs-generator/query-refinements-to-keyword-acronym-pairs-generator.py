## Import Module Requirements:
import pandas as pd
import csv
import re

## Import Variables via Files from Directory:
from configurationVariables import input_csv_filename

def format_dataframe(df):
    df = df.groupby(['SearchQuery1','SearchQuery2'], as_index=False)['Count'].sum() # Groups and Sums Counts of Query Pairs
    df['pair_ID'] = (df.index / 1 + 1000).astype(int) # Create Pair IDs
    df = df[['pair_ID','SearchQuery1','SearchQuery2','Count']]
    return df

df = pd.read_csv('{0}'.format(input_csv_filename), names=['SearchQuery1','SearchQuery2','Count'], header=None)
df = format_dataframe(df)

# Empty Lists:
pair_ID_list = []
SearchQuery1_list = []
SearchQuery2_list = []
count_list = []

##################################################
# Find 2 Letter and 2 Word Query / Acronyms Pairs:
query_2words_df = df[df['SearchQuery1'].str.contains(r'^\w{2}$')] # Query1 contains 2 Letters with no spaces
query_2words_df = df[df['SearchQuery2'].str.contains(r'^\w+\s\w+$')] # Query2 contains 2 Words with no spaces

# Query Pairs with 2 Letters and 2 Words:
for index, row in query_2words_df.iterrows():
    # SearchQuery1
    SearchQuery1_Letter1 = row['SearchQuery1'][0] # Get FIRST Letter in Row
    SearchQuery1_Letter2 = row['SearchQuery1'][1] # Get SECOND Letter in Row
    # SearchQuery2
    SearchQuery2_Letter1 = row['SearchQuery2'][0] # Get FIRST Letter in Row
    SearchQuery2_Letter2 = row['SearchQuery2'].split()[1:2] # Get SECOND Word in Row
    try:
        SearchQuery2_Letter2 = SearchQuery2_Letter2[0][0] # Get FIRST Letter in SECOND Word in Row
    except IndexError:
        pass

    if SearchQuery1_Letter1 == SearchQuery2_Letter1:
        if SearchQuery1_Letter2 == SearchQuery2_Letter2:
            pair_ID_value = row['pair_ID']
            pair_ID_list.append(pair_ID_value)
            SearchQuery1_value = row['SearchQuery1']
            SearchQuery1_list.append(SearchQuery1_value)
            SearchQuery2_value = row['SearchQuery2']
            SearchQuery2_list.append(SearchQuery2_value)
            count_value = row['Count']
            count_list.append(count_value)

##################################################
# Find 3 Letter and 3 Word Query / Acronyms Pairs:
query_3words_df = df[df['SearchQuery1'].str.contains(r'^\w{3}$')] # Query1 contains 3 Letters with no spaces
query_3words_df = df[df['SearchQuery2'].str.contains(r'^\w+\s\w+\s\w+$')] # Query2 contains 3 Words with no spaces

# Query Pairs with 3 Letters and 3 Words:
for index, row in query_3words_df.iterrows():
    # SearchQuery1
    SearchQuery1_Letter1 = row['SearchQuery1'][0] # Get FIRST Letter in Row
    SearchQuery1_Letter2 = row['SearchQuery1'][1] # Get SECOND Letter in Row
    SearchQuery1_Letter3 = row['SearchQuery1'][2] # Get THIRD Letter in Row
    # SearchQuery2
    SearchQuery2_Letter1 = row['SearchQuery2'][0] # Get FIRST Letter in Row
    SearchQuery2_Letter2 = row['SearchQuery2'].split()[1:2] # Get SECOND Word in Row
    SearchQuery2_Letter3 = row['SearchQuery2'].split()[2:3] # Get THIRD Word in Row
    try:
        SearchQuery2_Letter2 = SearchQuery2_Letter2[0][0] # Get FIRST Letter in SECOND Word in Row
    except IndexError:
        pass
    try:
        SearchQuery2_Letter3 = SearchQuery2_Letter3[0][0] # Get FIRST Letter in THIRD Word in Row
    except IndexError:
        pass

    if SearchQuery1_Letter1 == SearchQuery2_Letter1:
        if SearchQuery1_Letter2 == SearchQuery2_Letter2:
            if SearchQuery1_Letter3 == SearchQuery2_Letter3:
                pair_ID_value = row['pair_ID']
                pair_ID_list.append(pair_ID_value)
                SearchQuery1_value = row['SearchQuery1']
                SearchQuery1_list.append(SearchQuery1_value)
                SearchQuery2_value = row['SearchQuery2']
                SearchQuery2_list.append(SearchQuery2_value)
                count_value = row['Count']
                count_list.append(count_value)

##################################################
# Find 4 Letter and 4 Word Query / Acronyms Pairs:
query_4words_df = df[df['SearchQuery1'].str.contains(r'^\w{4}$')] # Query1 contains 4 Letters with no spaces
query_4words_df = df[df['SearchQuery2'].str.contains(r'^\w+\s\w+\s\w+\s\w+$')] # Query2 contains 4 Words with no spaces

# Query Pairs with 4 Letters and 4 Words:
for index, row in query_4words_df.iterrows():
    # SearchQuery1
    SearchQuery1_Letter1 = row['SearchQuery1'][0] # Get FIRST Letter in Row
    SearchQuery1_Letter2 = row['SearchQuery1'][1] # Get SECOND Letter in Row
    SearchQuery1_Letter3 = row['SearchQuery1'][2] # Get THIRD Letter in Row
    SearchQuery1_Letter4 = row['SearchQuery1'][3] # Get FOURTH Letter in Row
    # SearchQuery2
    SearchQuery2_Letter1 = row['SearchQuery2'][0] # Get FIRST Letter in Row
    SearchQuery2_Letter2 = row['SearchQuery2'].split()[1:2] # Get SECOND Word in Row
    SearchQuery2_Letter3 = row['SearchQuery2'].split()[2:3] # Get THIRD Word in Row
    SearchQuery2_Letter4 = row['SearchQuery2'].split()[3:4] # Get THIRD Word in Row
    try:
        SearchQuery2_Letter2 = SearchQuery2_Letter2[0][0] # Get FIRST Letter in SECOND Word in Row
    except IndexError:
        pass
    try:
        SearchQuery2_Letter3 = SearchQuery2_Letter3[0][0] # Get FIRST Letter in THIRD Word in Row
    except IndexError:
        pass
    try:
        SearchQuery2_Letter4 = SearchQuery2_Letter4[0][0] # Get FIRST Letter in FOURTH Word in Row
    except IndexError:
        pass

    if SearchQuery1_Letter1 == SearchQuery2_Letter1:
        if SearchQuery1_Letter2 == SearchQuery2_Letter2:
            if SearchQuery1_Letter3 == SearchQuery2_Letter3:
                if SearchQuery1_Letter4 == SearchQuery2_Letter4:
                    pair_ID_value = row['pair_ID']
                    pair_ID_list.append(pair_ID_value)
                    SearchQuery1_value = row['SearchQuery1']
                    SearchQuery1_list.append(SearchQuery1_value)
                    SearchQuery2_value = row['SearchQuery2']
                    SearchQuery2_list.append(SearchQuery2_value)
                    count_value = row['Count']
                    count_list.append(count_value)

###############################################
## Build Export DataFrame() with Keyword Pairs:
pair_ID_df = pd.DataFrame(pair_ID_list, columns=['pair_ID'])
SearchQuery1_df = pd.DataFrame(SearchQuery1_list, columns=['SearchQuery1'])
SearchQuery2_df = pd.DataFrame(SearchQuery2_list, columns=['SearchQuery2'])
count_df = pd.DataFrame(count_list, columns=['Count'])
result_df = pd.concat([pair_ID_df, SearchQuery1_df, SearchQuery2_df, count_df], axis=1)
result_df = result_df.sort_values(by='Count', ascending=False)

result_df.to_csv('output-query1-query2-acronym-pairs.csv', index=False)
