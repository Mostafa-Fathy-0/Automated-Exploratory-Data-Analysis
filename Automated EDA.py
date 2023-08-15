import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#####################################
def clean_missing_data(df):
    missing_columns_values = df.columns[df.isnull().any()]
    for column in missing_columns_values:
        if df[column].dtype == 'object':
            df[column] = df[column].fillna('Unknown')
        elif df[column].dtype == 'bool':
            df[column] = df[column].fillna(False)
        else:
            df[column] = df[column].fillna(df[column].mean())
#####################################
def get_file_types(file_type):
    while True :
        file_path = input('Please enter your file path : ')
        if file_path.endswith(tuple(file_type)):
            return file_path
        else :
            print('Please enter a valid path from this range {}'.format(file_type))
#####################################
def check_file_path(file_path):
    
    if file_path.endswith('csv'):
        df = pd.read_csv(file_path.strip())
        
    elif file_path.endswith('xlsx'):
        df = pd.read_excel(file_path.strip())
        
    elif file_path.endswith('sql'):
        df = pd.read_sql(file_path.strip())
        
    return df    
#####################################
def visuliaze(df):
    for column_name in df.columns:
        column_data = df[column_name]
        column_type = column_data.dtype
        
        fig, axs = plt.subplots()
        
        if column_type in['object' , 'bool'] :
            value_counts = column_data.value_counts()
            labels = value_counts.index
            colors = ['cadetblue', 'coral', 'limegreen', 'mediumpurple']
            sns.barplot(x=labels, y=value_counts, palette=colors, ax=axs)
        elif column_type in ['int64', 'float64']:
            sns.histplot(column_data, bins='auto', color='skyblue', ax=axs)
            axs.axvline(column_data.mean(), color='red', linestyle='dashed', linewidth=1)
            axs.axvline(column_data.median(), color='green', linestyle='dashed', linewidth=1)
            axs.legend(['Mean', 'Median'])
        
        axs.set_title(column_name)
        
        plt.show()
    
#####################################
def main():
    file_type = ['.csv','.xlsx','.sql']
    file_path = get_file_types(file_type)
    df = check_file_path(file_path)
    clean_missing_data(df)
    visuliaze(df)
    drop_column(df)
if __name__ == "__main__":
    main()
