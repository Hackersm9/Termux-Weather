import os,sys

os.system("clear")
os.system("pkg install curl")
os.system("clear")
cast = input("City to find Weather Forecast: ")
os.system("curl wttr.in/{0}".format(cast))
