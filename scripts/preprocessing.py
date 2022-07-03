from collections import Counter
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer  
import pandas as pd


class Preprocess:
    def __init__(self) -> None:
        pass
    
    def fix_outliers(self, df):
        column_name=list(df.columns[2:])
        for col in column_name:
                lower_quartile, upper_quartile = df[col].quantile(0.25), df[col].quantile(0.75)
                self.df[col]=np.where(df[col]>upper_quartile,df[col].median(),np.where(df[col]<lower_quartile, df[col].median(), df[col]))
        return self.df


    def scaler(self, df, columns, mode="minmax"):
        if (mode == "minmax"):
            minmax_scaler = MinMaxScaler()
            return pd.DataFrame(minmax_scaler.fit_transform(df), columns=columns)

        elif (mode == "standard"):
            scaler = StandardScaler()

        return pd.DataFrame(scaler.fit_transform(df), columns=columns)


    def normalizer(self, df, columns):
        norm = Normalizer()
        return pd.DataFrame(norm.fit_transform(df), columns=columns)


    def scale_and_normalize(self, df, scaler="minmax"):
        columns = df.columns
        return self.normalizer(self.scaler(df, columns, scaler), columns)

        
    def save_clean(self,df, name):
        df.to_csv(f'../data/{name}.csv', index=False)
