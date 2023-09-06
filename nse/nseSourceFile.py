import pandas as pd
import requests

dt = '06092023'

#f= 'https://archives.nseindia.com/products/content/sec_bhavdata_full_01092023.csv'
f= 'https://archives.nseindia.com/products/content/sec_bhavdata_full_{}.csv'.format(dt)


req = requests.get(f, stream=True, timeout=5)
url_content = req.content
csv_file = open("C:\\anupam\\nse_daily_sourcefiles\\sec_bhavdata_full_{}.csv".format(dt), 'wb')
csv_file.write(url_content)
csv_file.close()
print("EQ done")


#f= 'https://archives.nseindia.com/content/fo/NSE_FO_bhavcopy_31082023.csv'
f= 'https://archives.nseindia.com/content/fo/NSE_FO_bhavcopy_{}.csv'.format(dt)
req = requests.get(f, stream=True, timeout=10)
filename = f.split('/')[-1]

with open("C:\\anupam\\nse_daily_sourcefiles\\{}".format(filename), 'wb') as output_file:
    output_file.write(req.content)

print("FO done")