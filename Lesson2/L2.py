import pandas as pd

employment_data = pd.read_csv('employment_above_15.csv')

year = '2007'
country = employment_data['Country']
employment = employment_data[year]

n = 10
for k in range(n):
	print('{} has {:.1f} employment in {}'.format(country[k],employment[k],year))