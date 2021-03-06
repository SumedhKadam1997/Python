import pandas as pd
d = {'year': [2012], 'month': [1],'day': [15]}
df = pd.DataFrame(d)
print(pd.to_datetime(df))