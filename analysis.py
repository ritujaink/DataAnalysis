import pandas as pd
import xlrd

df = pd.read_excel('fulldata.xlsx')
df.dropna()
#print(df)

def fullanalysis():
    print(df[['CCTOTAL', 'CGTOTAL', 'DSTOTAL', 'ISTOTAL', 'OSTOTAL', 'SWSTOTAL']])



def fulldatamean():
    mean = (df[['CCTOTAL', 'CGTOTAL', 'DSTOTAL', 'ISTOTAL', 'OSTOTAL', 'SWSTOTAL']]).mean()
    print(mean)



def fulldatamax():
    wholemax = (df[['CCTOTAL', 'CGTOTAL', 'DSTOTAL', 'ISTOTAL', 'OSTOTAL', 'SWSTOTAL']]).max()
    print(wholemax)


def fulldatamin():
    wholemin = (df[['CCTOTAL', 'CGTOTAL', 'DSTOTAL', 'ISTOTAL', 'OSTOTAL', 'SWSTOTAL']]).min()
    print(wholemin)
    


def inddataanna():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['CCTOTAL', 'CGTOTAL', 'DSTOTAL', 'ISTOTAL', 'OSTOTAL', 'SWSTOTAL']])
    
def indmodcc():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['CCQ1', 'CCQ2', 'CCQ3']])


def indmodcg():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['CGQ1', 'CGQ2', 'CGQ3']])


def indmodds():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['DSQ1', 'DSQ2', 'DSQ3']])


def indmodos():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['OSQ1', 'OSQ2', 'OSQ3']])



def indmodis():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['ISQ1', 'ISQ2', 'ISQ3']])


def indmodsws():
    df.set_index('Student Name', inplace=True)
    print(df.loc['Jessica John Joseph Mala'][['SWSQ1', 'SWSQ2', 'SWSQ3']])




    
    
