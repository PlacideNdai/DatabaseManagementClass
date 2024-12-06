import pandas as pd  
from datetime import datetime 
file_loc = file_loc = r'/home/notplacide/Documents/GitHub/DatabaseManagementClass/Final_Lab/Data/poems.csv'



# cleaning the data
def cleanData(date):
    try:
        # Parse the date
        data_parse = pd.to_datetime(date, format='%m/%d/%Y', errors='coerce')
        
        # Check if the date is invalid or before 1678
        if pd.isna(data_parse) or (data_parse and data_parse.year < 1678):
            return datetime(1689, 1, 1)  # Default to January 1, 1689
        
        return data_parse
    except Exception as e:
        return pd.NaT 
    
    

    
# Reading the file
dataframe = pd.read_csv(file_loc)
replacementStrin = 'date'
# dataframe[replacementStrin] = dataframe[replacementStrin].apply(cleanData)
# dataframe['state'] = dataframe['state'].isnull()
# dataframe['state'].fillna("Texas", inplace=True)
dataframe['poem'] = dataframe['poem'].str.replace(',',"-")

# Save the file
dataframe.to_csv(file_loc, index=False)
