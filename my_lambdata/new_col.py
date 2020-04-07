import pandas as pd

def col_adder(df, list, name=None):
    """
    inputs: a dataframe, a list to be added to the dataframe \
        as a column, and an optional name for that column

    outputs: the dataframe with the list added as a column
    """
    new_col = pd.Series(list)
    
    if name == None:
        newname = str( len(df.columns) + 1) 

        df[newname] = new_col
        return df

    else:
        df[name] = new_col
        return df

def plus_one(number):
    return number + 1

if __name__ == "__main__":

    print('hello world')