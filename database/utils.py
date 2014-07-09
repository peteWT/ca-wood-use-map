import pandas as pd


def getCSVGdoc(url,filename,fields=None):
    df=pd.read_csv(url)
    if fields !=None:
        out=df[fields]
        out.to_csv('%s'%filename)
        print 'saved to: '+filename
    else:
        df.to_csv(filename)
        print 'saved to: '+filename

