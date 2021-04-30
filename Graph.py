import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates


solarData = pd.read_csv('25112020.csv')

print("SUMMARY")
print("Solar power used is : " + str(solarData['Site - PV Power'].sum()))
print("Grid power used is : " + str(solarData['Site - Grid Power'].sum()))
print("Battery power used is : " + str(solarData['Site - Battery Power'].sum()))
solarData.Timestamp = pd.to_datetime(solarData.Timestamp)
tim = solarData.Timestamp
plt.plot(tim, solarData['Site - PV Power'], label="PV")
plt.plot(tim, solarData['Site - Load Power'], label="Load")
plt.plot(tim, solarData['Site - Grid Power'], label="Grid")
plt.plot(tim, solarData['Site - Battery Power'], label="Battery")
plt.title('Site Power')
plt.xlabel('Date Time')
plt.ylabel('Power')
plt.legend()
plt.xticks(rotation=45)

plt.show()
