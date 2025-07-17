import pandas as pd

try:
    df = pd.read_csv('/home/ubuntu/upload/FM2023.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('/home/ubuntu/upload/FM2023.csv', encoding='latin1')

print('Informações do DataFrame:')
df.info()

print('\nValores únicos da coluna Posição:')
print(df['Position'].unique())

print('\nValores únicos da coluna Nationality (top 10):')
print(df['Nationality'].value_counts().head(10))

print('\nValores únicos da coluna Club (top 10):')
print(df['Club'].value_counts().head(10))

print('\nVerificando valores não numéricos na coluna "Values":')
print(pd.to_numeric(df['Values'], errors='coerce').isnull().sum())

print('\nVerificando valores não numéricos na coluna "Salary":')
print(pd.to_numeric(df['Salary'], errors='coerce').isnull().sum())

print('\nVerificando valores não numéricos na coluna "ca":')
print(pd.to_numeric(df['ca'], errors='coerce').isnull().sum())

print('\nVerificando valores não numéricos na coluna "pa":')
print(pd.to_numeric(df['pa'], errors='coerce').isnull().sum())

print('\nVerificando valores não numéricos na coluna "Age":')
print(pd.to_numeric(df['Age'], errors='coerce').isnull().sum())



