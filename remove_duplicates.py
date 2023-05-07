import pandas as pd

def remove_duplicates(data):
    df = pd.read_csv(data)
    df.drop_duplicates(inplace=True)
    csv_data = df.to_csv(index=False)
    return csv_data
