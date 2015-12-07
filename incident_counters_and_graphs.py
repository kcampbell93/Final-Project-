import csv
import operator
from collections import Counter 
sample = "P:/Fall_2015/Python_Programing/Final_Project/incidents_w_month.csv" #PASTE CSV FILE HERE


typelist = [] #TYPECOUNTER
with open(sample, 'r') as csvfile: #OPENS AND READS CSV FILE
    data = csv.reader(csvfile)
    for line in data:
            if line[14] != '': #ONLY INCLUDES ROWS WITH INFORMATION
                typelist.append(line[4]) #LOCATES COLUMN TO ANALYIZE
    typelist.remove('Incident Type')#EXCLUDES COLUMN HEADER FROM BEING COUNTED
type_cnt = Counter()#DEFINES COUNTTER
incidenttype = [(0, 'Boat'), (1, 'PWC'), (2, 'Drowning'), (3, 'Tube'), 
                (4, 'Paddle Boat'),(5, 'Fly Fishing'), (6, 'Other')] #DEFINES INCIDENT TYPES
reverse_type = {}
for order, itype in incidenttype:
    reverse_type[itype] = order
for order, word in incidenttype: #ORDERS TYPES
    type_cnt[(order, word)] = 0
for word in typelist:
    type_cnt[(reverse_type[word], word)] += 1



monthlist = [] #MONTH COUNTER
with open(sample, 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        if line[14] != '':
            monthlist.append(line[13])
    monthlist.remove('Month')
month_cnt = Counter()
months = [(0, 'JAN'), (1, 'FEB'), (2, 'MAR'), (3, 'APR'), (4, 'MAY'), (5, 'JUN'), (6, 'JUL'),
         (7, 'AUG'), (8, 'SEP'), (9, 'OCT'), (10, 'NOV'), (11, 'DEC')]
reverse_months = {}
for order, month in months:
    reverse_months[month] = order
for order, word in months:
    month_cnt[(order, word)] = 0
for word in monthlist:
    month_cnt[(reverse_months[word], word)] += 1





countylist = [] #COUNTY COUNTER
with open(sample, 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        if line[14] != '':
            countylist.append(line[5])
    countylist.remove('County')
county_cnt = Counter()
county = [(0, 'Dawson'), (1, 'Forsyth'), (2, 'Hall'), (3, 'Lumpkin'), (4, 'Gwinnett')]
for order, word in county:
    county_cnt[(order, word)] = 0
for word in countylist:
    county_cnt[word] += 1



timelist = [] #TIME COUNTER
with open(sample, 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        if line[14] != '':
            timelist.append(line[14])
    timelist.remove('Hour')
time_cnt = Counter()
hours = [(0, '12AM'), (1, '1AM'), (2, '2AM'), (3, '3AM'), (4, '4AM'), (5, '5AM'), (6, '6AM'),
         (7, '7AM'), (8, '8AM'), (9, '9AM'), (10, '10AM'), (11, '11AM'), (12, '12PM'), (13, '1PM'),
         (14, '2PM'), (15, '3PM'), (16, '4PM'), (17, '5PM'), (18, '6PM'), (19, '7PM'), (20, '8PM'),
         (21, '9PM'), (22, '10PM'), (23, '11PM')]
reverse_hours = {} #CALLS KEY RATHER THAN INDEX
for order, hour in hours:
    reverse_hours[hour] = order
for order, word in hours:
    time_cnt[(order, word)] = 0
for word in timelist:
    time_cnt[(reverse_hours[word], word)] += 1


#PRINTS COUNTS
print county_cnt 
print type_cnt 
print month_cnt 
print time_cnt



#GRAPHS!
import matplotlib.pyplot as plt #IMPORTS MATPLOTLIB



#INCIDENTS BY TYPE
print(sorted(type_cnt.items()))#PRINTS CCOUNT
x = [order for order, incidenttype in sorted(type_cnt.keys())] #TYPES
y = [item[1] for item in sorted(type_cnt.items())]  #NUMBER OF INCIDENTS
my_xticks = [incidenttype for order, incidenttype in sorted(type_cnt.keys())] #PULLS TICKS FROM COUNTER
plt.xticks(x, my_xticks) #PLOTS X-TICKS
plt.bar(x, y, label='Incidents')#PLOTS BARS AND LABLES LEGEND 
plt.legend() #PLOTS LEGEND
plt.xlabel('Type') #PLOTS X-ASIS
plt.ylabel('Number of Incidents') #PLOTS Y-AXIS
plt.title('Incidents from October 2014 to October 2015\nBy Type') #PLOTS TITLE 
plt.savefig('P:/Fall_2015/Python_Programing/Final_Project/typegraph.png') #SAVES THE GRAPH
plt.show() #SHOWS THE GRAPH 

#INCIDENT BY MONTH
print(sorted(month_cnt.items()))
x = [order for order, month in sorted(month_cnt.keys())] 
y = [item[1] for item in sorted(month_cnt.items())]
print x
print y
my_xticks = [month for order, month in sorted(month_cnt.keys())] 
plt.xticks(x, my_xticks) 
plt.bar(x, y, label='Incidents') 
plt.legend()
plt.xlabel('Month') 
plt.ylabel('Number of Incidents')
plt.title('Incidents from October 2014 to October 2015\nBy Month') 
plt.savefig('P:/Fall_2015/Python_Programing/Final_Project/monthgraph.png')
plt.show() 


#Incidents by Time
print(sorted(time_cnt.items()))
x = [order for order, hour in sorted(time_cnt.keys())] 
y = [item[1] for item in sorted(time_cnt.items())]  
my_xticks = [hour for order, hour in sorted(time_cnt.keys())] 
plt.xticks(x, my_xticks) 
plt.bar(x, y, label='Incidents') 
plt.legend()
plt.xlabel('Time') 
plt.ylabel('Number of Incidents')
plt.title('Incidents from October 2014 to October 2015\nBy Time')
plt.savefig('P:/Fall_2015/Python_Programing/Final_Project/timegraph.png')
plt.show() 
