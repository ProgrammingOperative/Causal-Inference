from collections import Counter
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer  

class Preprocess:
    def __init__(self, df) -> None:
        self.df = df
    
    def fix_outliers(self):
        column_name=list(self.df.columns[2:])
        for col in column_name:
                lower_quartile, upper_quartile = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
                self.df[col]=np.where(self.df[col]>upper_quartile,self.df[col].median(),np.where(self.df[col]<lower_quartile,self.df[col].median(),self.df[col]))
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

        
    def save_clean(self, name):
      self.df.to_csv(f'../data/{name}.csv', index=False)
