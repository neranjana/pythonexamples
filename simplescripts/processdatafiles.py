# if not installed, install glob2 and pandas with pip install glob2 and pip install pandas
import pandas
import glob2

filelist=glob2.glob("./datafiles/*.txt")
print(filelist)

for file in filelist:
    df=pandas.read_csv(file)
    m=df.mean()
    m=float(m) #convert m to float datatype
    print(m)
