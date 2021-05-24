# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:04:10 2021

@author: uia76912
"""
# Function for missing values
def missing_values(df):
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mz_table = pd.concat([ mis_val, mis_val_percent], axis=1)
        mz_table = mz_table.rename(
        columns = {0 :  'Missing Values', 1 : '% of Total Values'})
        mz_table['Data Type'] = df.dtypes
        mz_table = mz_table[
            mz_table.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"      
            "There are " + str(mz_table.shape[0]) +
              " columns that have missing values. \n")
#         mz_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
        #top_missing_columns_df = mz_table[mz_table["% of Total Values"] > 50]
        
        return mz_table


## Missing values in training dataset
train_missing_values  = missing_values(X_full)
print(train_missing_values)


# Function to identify the top missing values in a dataset 
def top_missing_values(df):
    top_missing_columns_df = df[df["% of Total Values"] > 50]
    top_missing_columns = top_missing_columns_df["% of Total Values"].index
    return (top_missing_columns.tolist())
    

#top missing values
list_of_top_missing_values = top_missing_values(train_missing_values)
print(list_of_top_missing_values)
