from collections import Counter
import numpy as np

class DataClean:
    def __init__(self, df) -> None:
        self.df = df
    
    def fix_outliers(self):
        column_name=list(self.df.columns[2:])
        for col in column_name:
                lower_quartile, upper_quartile = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
                self.df[col]=np.where(self.df[col]>upper_quartile,self.df[col].median(),np.where(self.df[col]<lower_quartile,self.df[col].median(),self.df[col]))
        return self.df

        
    def save_clean(self, name):
      self.df.to_csv(f'../data/{name}.csv', index=False)
