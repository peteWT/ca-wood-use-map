import pandas as pd
import sys

csv=sys.argv[1]
###csv='https://docs.google.com/spreadsheet/pub?key=0AnyNiqk9X8DmdDJneGxsNTB6cFFQamRMX0VuNjhPQ2c&output=csv'
df=pd.read_csv(csv)
toDb=df[['RecID','MapLabel','Status','longitude','latitude', 'Name_Current', 'Names_Prior','CIty','StAddr','State','Zip']]
toDb.to_csv('%s'%sys.argv[2])
