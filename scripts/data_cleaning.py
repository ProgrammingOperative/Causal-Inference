class DataClean:
    def __init__(self, df) -> None:
        self.df = df
    
    def fix_outliers(self, df, features):
        outlier_indices = []
        
        for c in features:
            # 1st quartile
            Q1 = np.percentile(df[c],25)
            # 3rd quartile
            Q3 = np.percentile(df[c],75)
            # IQR
            IQR = Q3 - Q1
            # Outlier step
            outlier_step = IQR * 1.5
            # detect outlier and their indeces
            outlier_list_col = df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
            # store indeces
            outlier_indices.extend(outlier_list_col)

        outlier_indices = Counter(outlier_indices)
    
        multiple_outliers = []
        for v in outlier_indices.items(): 
            if v[-1]>2:
                multiple_outliers.append(v[0])
            
        return multiple_outliers
