import datetime #from time to string
import csv
import operator #sort the file
import itertools #calculate the avg
import matplotlib.pyplot as plt   #http://matplotlib.org/
import matplotlib.dates as dt #plor the data
import urllib #http request
#ATTENTION: please take a look to the readme/tutorial: https://github.com/ilbonte/RescueTime-efficiency
print("start")


############
##settings##
############
#API documentation: https://www.rescuetime.com/apidoc
pv="interval" #do not change this
rk = "efficiency" #do not change this
format = "csv" #do not change this
rs="hour" #hour or minute (tip:use minute if you are going to plot only few weeks of data)
rb="2014-10-16" #yyyy-mm-dd from
re="2014-11-16" #to
rtapi_key="PUT_YOUR_API_KEY_HERE" #your (looong) API key generated in the Embed and Data API -> Setup Data API
file_name="file" #the name of the file where the data will be downloaded
# get the file
urllib.request.urlretrieve("https://www.rescuetime.com/anapi/data/?pv=interval&rk=efficiency&rs="+rs+"&rb="+rb+"&re="+re+"&format="+format+"&rtapi_key="+rtapi_key+"", file_name+".csv")
print("download finished")

#The csv contains Date,Time Spent (seconds),Number of People,Efficiency
#I only need hour and efficiency
print("deleting useless values")
with open(file_name+".csv",'r',newline='') as inFile, open("edited.csv",'w', newline='') as outFile:
    inFile.readline()
    reader = csv.reader(inFile)
    for row in reader:
        tmp_h=row[0]
        hour=tmp_h[11:16]
        val=row[4]
        outFile.write(hour+","+val+"\n")

# sort the csv file to calculate the avg
print("sorting the data")
reader = csv.reader(open("edited.csv"), delimiter=",")
sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False)
with open('edited.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sortedlist)

# calculate the avg and print in the file
print("calculating avg")
with open('edited.csv') as input, open('avg.csv','w', newline='') as output:
    reader = csv.reader(input)
    writer = csv.writer(output)
    for time, row in itertools.groupby(reader, lambda x: x[0]):
        biaslist = [float(x[1]) for x in row]
        biasavg = round(float(sum(biaslist))/len(biaslist),1)
        writer.writerow([time,biasavg])

v_date=[]
v_val=[]
print("plotting the data,please wait")
with open('edited.csv') as input, open('avg.csv') as inavg:
    reader = csv.reader(input)
    avg_reader = csv.reader(inavg)
    for row in reader:
        dates = dt.date2num(datetime.datetime.strptime(row[0], '%H:%M')) #from custom string to datetime
        to_int=round(float(row[1]))
        plt.plot_date(dates, row[1],color=plt.cm.brg(to_int))
    #I need to put the date anc the value in a list to drow the line
    for arow in avg_reader:
        dates = dt.date2num(datetime.datetime.strptime(arow[0], '%H:%M'))
        v_date.append(dates)
        v_val.append(arow[1])

plt.plot_date(v_date, v_val,"^y-",label='Average')
plt.xlabel('Hours')
plt.ylabel('Efficiency')
plt.title('Data from '+rb+' to '+ re)
plt.legend()
plt.show()
#for infos: davide.bonte@gmail.com
