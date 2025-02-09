import polars as pl
import re
import glob

pl.Config.set_tbl_cols(100)
pl.Config.set_tbl_width_chars(1000)

af =0.2

list1= ['ACC','ADANIPORTS','ASHOKLEY', 'ASIANPAINT','BAJAJ-AUTO','BANKBARODA','BEL', 'BHARTIARTL',
        'BHARATFORG','BHEL', 'GAIL', 'HAL', 'HCLTECH',
        'HDFCBANK','HEROMOTOCO','HINDALCO', 'HINDCOPPER', 'HINDUNILVR','ICICIBANK','INFY','IOC',
        'IRCTC','ITC', 'JSWSTEEL',
        'KOTAKBANK','LT', 'M&M','MARUTI', 'NESTLEIND', 'ONGC', 'PFC','PIDILITIND','POWERGRID', 'SAIL',
        'RELIANCE', 'SBIN','TATACHEM','TATAMOTORS','TATAPOWER', 'TATASTEEL', 'TCS']


for i in list1:
    df =   pl.read_csv(f"C:/pythonprojects/nse/cleanbase/{i}.csv")
    lenOfBaseFile = len(df["Date"].to_list())
    print(lenOfBaseFile)
    print(i)
    print(df.tail(6))

    for j in range(lenOfBaseFile):
        if j==0:
            df_scrip = pl.DataFrame({"Date": df[0, "Date"],
                             "Close_Price": df[0, "close"],
                             "Flg": 1,
                             "p": df[0, "close"],
                             "EP": df[0, "close"],
                             "EP-Pt-1": .1,
                             "XAF": .1,
                             "Rev": 1
                             })
        else:
            df_scrip_next= pl.DataFrame({"Date": df[j, "Date"],
                             "Close_Price": df[j, "close"],
                             "Flg": 1,
                             "p": df[j, "close"],
                             "EP": df[j, "close"],
                             "EP-Pt-1": .1,
                             "XAF": .1,
                             "Rev": 1
                             })
            df_scrip= df_scrip.vstack(df_scrip_next)

    df_scrip.write_csv(f"C:/pythonprojects/nse/target/{i}.csv")


    # Update correct values as per formula ..below start
    for j in range(1,lenOfBaseFile):
        df_scrip[j,'Flg']= df_scrip[j-1,'Rev']
        if (df_scrip[j,'Flg']==1):
            if (df_scrip[j,'Close_Price'] >df_scrip[j-1,'EP']):
                df_scrip[j, 'EP'] = df_scrip[j,'Close_Price']
            else:
                df_scrip[j, 'EP'] = df_scrip[j-1, 'EP']
        else:
            if (df_scrip[j, 'Close_Price'] < df_scrip[j - 1, 'Close_Price']):
                df_scrip[j, 'EP'] = df_scrip[j, 'Close_Price']
            else:
                df_scrip[j, 'EP'] = df_scrip[j-1, 'Close_Price']

        df_scrip[j, 'EP-Pt-1'] = df_scrip[j, 'EP'] - df_scrip[j-1, 'p']
        df_scrip[j, 'XAF'] = df_scrip[j, 'EP-Pt-1']*af
        df_scrip[j, 'p'] = df_scrip[j-1, 'p'] +   df_scrip[j, 'XAF']

        if(df_scrip[j, 'p'] < df_scrip[j,'Close_Price']):
            df_scrip[j, 'Rev'] = 1
        else:
            df_scrip[j, 'Rev'] = -1

    # Update correct values as per formula ..below ends
    df_scrip.write_csv(f"C:/pythonprojects/nse/target/{i}.csv")

