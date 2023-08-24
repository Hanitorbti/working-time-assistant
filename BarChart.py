import pandas as pd
import matplotlib.pyplot as plt
from os import getcwd, mkdir, path, _exit

from Csv import csv
csv_chek = csv()
if not csv_chek == "ok":
    input("CSV ERR\npress enter to exit!")
    _exit(0)


def BarChart(user_y,user_m):
    if not path.exists(f"{getcwd()}\\report"):
        mkdir(f"{getcwd()}\\report")
    if not path.exists(f"{getcwd()}\\report\\{user_y},{user_m}"):
        mkdir(f"{getcwd()}\\report\\{user_y},{user_m}")

    data = pd.read_csv("report.csv", header=0, sep=',')

    data.hist(bins=50, figsize=(10,7.5))
    plt.savefig(f"{getcwd()}\\report\\{user_y},{user_m}\\total.png")

    try:
        nd = pd.DataFrame(data["day"][data['month']==user_m][data['year']==user_y] , columns=['day'])
        nd['time'] = data["time"][data['month']==user_m][data['year']==user_y]

        nd.plot(kind='bar',x='day',
            y = 'time',
            title = f"20{user_y}/{user_m}")

        plt.savefig(f"{getcwd()}\\report\\{user_y},{user_m}\\{user_y},{user_m}.png")
        return "done"

    except:
        return "NOT EXIST"

user_y = int(input("year: "))
user_m = int(input("month: "))
BarChart(user_y,user_m)
