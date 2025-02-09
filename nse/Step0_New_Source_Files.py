import polars as pl
import re
import glob

pl.Config.set_tbl_cols(100)
pl.Config.set_tbl_width_chars(1000)

loadDate = '07022025'

filename= glob.glob("C://pythonprojects//nse//basedata//*")  #firstTime
# filename= "C:/pythonprojects/nse/cleanbase/" # When old value is to be appended

list1= ['ADANIPORTS','ASHOKLEY','BEL','BHARATFORG','HAL','HINDCOPPER','IRCTC','JSWSTEEL','NESTLEIND']

# for i in list1:
#     df =   pl.read_csv(f"C:/pythonprojects/nse/basedata/{i}.csv")
#     df = df.rename({col:col.replace(" ","") for col in df.columns})
#     df = df.with_columns(pl.col(col).str.replace_all(",","")  for col in df.columns if df[col].dtype == pl.Utf8)
#     df = df.with_columns(pl.col(col).str.replace_all("\\", "-") for col in df.columns if df[col].dtype == pl.Utf8)
#     df = df.with_columns(pl.col(col).str.replace_all("/", "-") for col in df.columns if df[col].dtype == pl.Utf8)
#     df.write_csv(f"C:/pythonprojects/nse/txtbase/{i}.txt")




for i in list1:
    res = None
    print(i)
    pattern = f'\D*-{i}[\D\d-]+'
    for j in filename:
        res = re.findall(pattern, j)
        if res:
            print(res[0])
            df= pl.read_csv(res[0])
            df = df.rename({col: col.replace(" ", "") for col in df.columns})
            df = df.with_columns(pl.col(col).str.replace_all(",","")  for col in df.columns if df[col].dtype == pl.Utf8)
            df = df.with_columns(pl.col(col).str.replace_all(" ", "") for col in df.columns if df[col].dtype == pl.Utf8)
            try:
                df = df.with_columns(pl.col('Date').str.strptime(pl.Date, format= '%d-%b-%y'))
            except:
                df = df.with_columns(pl.col('Date').str.strptime(pl.Date, format='%d-%b-%Y'))
            df = df.sort(by= 'Date', descending=False)
            df.write_csv(f"C:/pythonprojects/nse/cleanbase/{i}.csv")


for i in list1:
    dfbase=pl.read_csv(f"C:/pythonprojects/nse/cleanbase/{i}.csv")
    dfbase = dfbase.with_columns(pl.col('Date').str.strptime(pl.Date, format= '%Y-%m-%d'))
    dfbase = dfbase.with_columns((pl.col('vwap').cast(pl.Float64)))
    dfbase = dfbase.with_columns((pl.col('52WH').cast(pl.Float64)))
    dfbase = dfbase.with_columns((pl.col('52WL').cast(pl.Float64)))
    dfbase = dfbase.with_columns((pl.col('VALUE').cast(pl.Float64)))
    # print(i)
    # print(dfbase.head(2))
    # reading  fresh data of a scrip -- start
    df = pl.read_csv(f"C://pythonprojects//nse//source//sec_bhavdata_full_{loadDate}.csv", infer_schema_length=1)
    df_filtered_scrip = df.filter(pl.col('SYMBOL') == i)
    df_filtered_scrip = df_filtered_scrip.rename({col: col.replace(" ", "") for col in df.columns})
    df_filtered_scrip = df_filtered_scrip.with_columns(pl.col('DATE1').str.strptime(pl.Date, format='%d-%b-%Y'))


    # reading  fresh data of a scrip -- end
    print(df_filtered_scrip[0,'DATE1'])
    print(df_filtered_scrip[0,'CLOSE_PRICE'], type(df_filtered_scrip[0,'CLOSE_PRICE']))
    print(dfbase.dtypes)
    df_scrip_newValue = pl.DataFrame({"Date": df_filtered_scrip[0,'DATE1'],
                                      "series":"EQ",
                                      "OPEN": 0.0,
                                      "HIGH": 0.0,
                                      "LOW": 0.0,
                                      "PREV.CLOSE":0.0,
                                      "ltp":0.0,
                                      "close": float( df_filtered_scrip[0,'CLOSE_PRICE']),
                                      "vwap": 0.0,
                                      "52WH":0.0,
                                      "52WL":0.0,
                                      "VOLUME":0,
                                      "VALUE": 0.0,
                                      "Nooftrades":0
                             })

    dfbase = dfbase.vstack(df_scrip_newValue)
    dfbase.write_csv(f"C:/pythonprojects/nse/cleanbase/{i}.csv")


