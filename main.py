import pandas as pd
def find_n_largest_nodes(dataframe, n):
    node1 = []
    node2 = []
    similarity = []
    for index in range(1, len(dataframe)-1):
        for second_index in range(index, len(dataframe)):
            similarity.append(dataframe[index][second_index])
            node1.append(dataframe.columns[index])
            node2.append(dataframe.columns[second_index])

    return pd.DataFrame({'Node1': node1, 'Node2': node2, 'Similarity':similarity}).nlargest(10,'Similarity')