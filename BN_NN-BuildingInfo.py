import re
import pandas as pd
# don't forget to change the path!
path = r"C:\cqd"
df = pd.read_csv(path+r"\Building_YYYYMMDD_Present.tsv", sep='\t', header=None)
ndf = df.copy() #making a copy of original df JIC (yes, I don't care about memory ;) ) 
# NetworkName is only a 3 uppercase letters _probably it's a sitecode_
df1 = df[df[1].str.match(r'[A-Z]{3}$')==True]
print(df1.shape)
# BuildingName is only a 3 uppercase letters:
df2 = df[df[3].str.match(r'[A-Z]{3}$')==True]
print(df2.shape)
# df2-df1
df3 = pd.concat([df1,df2]).drop_duplicates(keep=False)
print(df3.shape)
# NetworkName does not contain BuildingName:
df4 = df3[df3.apply(lambda x: x[3] in x[1], axis=1)==False]
print(df4.shape)
# Add SiteCode in front of NetworkName
df4[1] = df4[3].astype(str) + '_' + df4[1]
# Replace NetworkName in origin dataframe with combined NetworkName from df4:
ndf.loc[df4.index, [1]] = df4[1]
ndf.to_csv(path+r"\Building_YYYYMMDD_Present_wSiteCodeInNN.tsv", sep='\t', header=None, index=None)
