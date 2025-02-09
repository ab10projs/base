import datetime
from datetime import date
import polars as pl
import re
import glob

pl.Config.set_tbl_cols(100)
pl.Config.set_tbl_width_chars(1000)

# loadDate = '03022025'
af =0.2

list1= ['ACC','ADANIPORTS','ASHOKLEY', 'ASIANPAINT','BAJAJ-AUTO','BANKBARODA','BEL', 'BHARTIARTL',
        'BHARATFORG','BHEL', 'GAIL', 'HAL', 'HCLTECH',
        'HDFCBANK','HEROMOTOCO','HINDALCO', 'HINDCOPPER', 'HINDUNILVR','ICICIBANK','INFY','IOC',
        'IRCTC','ITC', 'JSWSTEEL',
        'KOTAKBANK','LT', 'M&M','MARUTI', 'NESTLEIND', 'ONGC', 'PFC','PIDILITIND','POWERGRID', 'SAIL',
        'RELIANCE', 'SBIN','TATACHEM','TATAMOTORS','TATAPOWER', 'TATASTEEL', 'TCS']

f1 = open("C:/pythonprojects/nse/positions/newLong.txt", "a")
f2 = open("C:/pythonprojects/nse/positions/newShort.txt", "a")
f3 = open("C:/pythonprojects/nse/positions/oldLong.txt", "a")
f4 = open("C:/pythonprojects/nse/positions/oldShort.txt", "a")

f1.write(str( date.today()) )
f1.write(" \n")
f1.write("---------\n")

f2.write(str(date.today()))
f2.write(" \n")
f2.write("---------\n")

f3.write(str( date.today()) )
f3.write(" \n")
f3.write("---------\n")

f4.write(str(date.today()))
f4.write(" \n")
f4.write("---------\n")



# for i in list1:
#     df =   pl.read_csv(f"C:/pythonprojects/nse/target/{i}.csv")
#     lenOfBaseFile = len(df["Date"].to_list())
#     print(i)
#     print(df[lenOfBaseFile - 3, 'Rev'])
#     print(df[lenOfBaseFile - 2, 'Rev'])
#     print(df[lenOfBaseFile - 1, 'Rev'])
#     lates = df[lenOfBaseFile - 1, 'Rev']
#     oneOld = df[lenOfBaseFile - 2, 'Rev']
#     twoOld = df[lenOfBaseFile - 3, 'Rev']
#     threeOld = df[lenOfBaseFile - 4, 'Rev']
#     if ((lates==oneOld) and (lates!=twoOld)):
#         if lates==1:
#             f1.write(i)
#             f1.write(" ")
#             f1.write(str( lates) )
#             f1.write("\n")
#         else:
#             f2.write(i)
#             f2.write(" ")
#             f2.write(str( lates) )
#             f2.write("\n")
#
#
#
#
# f1.write("\n")
# f1.close()
#
# f2.write("\n")
# f2.close()


####

for i in list1:
    df =   pl.read_csv(f"C:/pythonprojects/nse/target/{i}.csv")
    lenOfBaseFile = len(df["Date"].to_list())
    oldPosition = 'long' # reset oldPosition at start of look for all scrips
    print(i, lenOfBaseFile) # ScripName
    for j in range(lenOfBaseFile):

        print(j,df[j, 'Rev'])
        if j>= 2:
            if ((df[j, 'Rev'] == df[j-1, 'Rev']) and ((df[j, 'Rev'] != df[j-2, 'Rev']))):
                if (df[j, 'Rev'] ==1 and oldPosition!='Long'):
                    print(j, f"old position was {oldPosition}")
                    newPosition = 'Long'
                    print(j, "New position changed to Long")
                    if j == lenOfBaseFile-1:
                        f1.write(i)
                        f1.write(" ")
                        f1.write("\n")


                if (df[j, 'Rev'] ==-1 and oldPosition!='Short'):
                    print(j, f"old position was {oldPosition}")
                    newPosition = 'Short'
                    print(j, "New position changed to Short")
                    if j == lenOfBaseFile-1:
                        f2.write(i)
                        f2.write(" ")
                        f2.write("\n")

            else:
                oldPosition = newPosition
                print(j, f"old position still is {oldPosition}")
                if j == lenOfBaseFile - 1:
                    if (oldPosition =='Long'):
                        f3.write(i)
                        f3.write(" ")
                        f3.write("\n")
                    if (oldPosition =='Short'):
                        f4.write(i)
                        f4.write(" ")
                        f4.write("\n")
