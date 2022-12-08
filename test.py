import pandas as pd

def ext_df(station):
    if int(station) < 10:
        filename = 'Data\TG_STAID00000' + station + '.txt'
    elif int(station) < 100:
        filename = 'Data\TG_STAID0000' + station + '.txt'
    else:
        filename = 'Data\TG_STAID000' + station + '.txt'
    
    return filename

filename =  ext_df("10")

df = pd.read_csv(filename, skiprows=20)

date = "19981025"

temperature = df.loc[df['    DATE'] == int(date)]['   TG'].squeeze()/10

print()
print(type(temperature))

