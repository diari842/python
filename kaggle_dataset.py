import pandas as pd

df = pd.read_csv('avgIQpercountry')

print(df.info())

first_row = df.head()
print(first_row)

country_data = df('Country')
print(country_data)

subset = df[['Country', 'Average IQ']]
print (subset)


filtered_df = subset[subset['Average IQ']>100]
print(filtered_df)

#Handling Missing and Duplicate Data
null_mask = df.isnull()
null_count = null_mask.sum()

print("/nCount of null values in each column:")
print(null_count)

df.dropna(inplace=True)
print("/nDataset information after removing null values:")
print(df.info())

duplicated_count = df.duplicated().sum()
print("/nCount of duplicated rows:")
print(duplicated_count)


df.drop_duplicates(keep='first', inplace=True)
#df.drop_duplicates(keep='last', inplace ="True") 

average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)



sorted_average_iq_per_continent = average_iq_per_continent.sort_values(ascending=False)
print(sorted_average_iq_per_continent)