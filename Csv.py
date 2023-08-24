from os import chdir, listdir, getcwd, mkdir, path
from shutil import rmtree
from FileHandler import file_handler as file

def csv():
    maindir = getcwd()

    files = listdir(f"{maindir}\\data")

    file("report.csv","w","year,month,day,time")
    for log in files:
        data=file(f"{maindir}\\data\\{log}")
        file("report.csv","a+",f"\n{log[0:2]},{log[3:5]},{log[6:8]},{data}")

    return "ok"

csv()



