#dataset source: https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization





import pandas as pd




filename = "netflix1.csv"




df = pd.read_csv(filename)

#pd.set_option('display.max_columns', None)
#print(df.head(10))

#no of missing values in each columns.
missing_value_number = df.isnull().sum()
#print(missing_value_number) = 0, no missing values

#print(df[df.duplicated()])
#no duplicated data as well
