from pyteal import Int


class DataInfor:
    def __init__(self, df) -> Int:
        self.df = df

    def null_percentage(self):
        '''
        Display Total Null percentage of the Data Frame
        '''

        number_of_rows, number_of_columns = self.df.shape
        df_size = number_of_rows * number_of_columns
        
        null_size = (self.df.isnull().sum()).sum()
        percentage = round((null_size / df_size) * 100, 2)
        return f"Data Frame contain null values of { percentage }"
    