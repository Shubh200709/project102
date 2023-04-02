#to find an old file using time module
import os, time

class Find():
    def Time(self, month_days, year, attribute,):#time in seconds
        self.atr = attribute
        self.month = month_days
        self.year = year

        time_in_sec = 0

        if(self.atr == 'month'):
            time_in_sec = self.month * 24 * 60 * 60
            ctime = time.time() - time_in_sec
        elif(self.atr == 'year' and self.year % 4 == 0):
            totalLeapYear = 366
            time_in_sec = 12 * totalLeapYear * 24 * 60 * 60
            ctime = time.time() - time_in_sec
        elif(self.atr == 'year' and self.year % 4 != 0):
            totalLeapYear = 365
            time_in_sec = totalLeapYear * 12 * 24 * 60 * 60
            ctime = time.time() - time_in_sec
        else:
            print('invalid input')

        return ctime
    def find(self, name, path, timee):
        self.time = timee
        self.filename = name
        self.folderPath = path
        temp_list = []
        currentTime = time.ctime(self.time)
        
        if(currentTime[9:11].isdigit == False):
            ctime = currentTime[9]

        for files, roots, dir in os.walk(self.folderPath):
            file_name = os.path.basename(files)
            fileName = os.path.splitext(file_name)[0]

            if(fileName == self.filename and ctime <= self.time):
                temp_list.append(file_name)
        
        return temp_list
    
    def printFile(self, list):
        self.list = list
        for i in self.list:
            print(i)

find = Find()
Case = True
start = False

if Case == True or start == True:
    tim = input("enter how old the file is(month/year): ")
    mon_yea_time = 0
    if(tim == 'year'):
        year = input('Is the file formed in a leap year(y/n)')
        if(year == 'y'):
            year_data = int(input('Enter the year'))
            mon_yea_time = find.Time(0,year_data,'year')#here
        elif(year == 'n'):
            year_data = int(input('Enter the year'))
            mon_yea_time = find.Time(0,year_data,'year')#here
    elif(tim == 'month'):
        month_days = int(input('Enter the month number'))
        y31 =[1,3,5,7,8,10,12]
        y30 = [4,6,9,11]
        y28 = 2

        if(month_days in y31):
            day = 31
            mon_yea_time = find.Time(day,0,'month')#here
        elif(month_days in y30):
            day = 30
            mon_yea_time = find.Time(day,0,'month')#here
        elif(month_days is y28):
            day = 28
            mon_yea_time = find.Time(day,0,'month')#here
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')
        Case = False

filename = input("enter filename: ")
path = input('enter folder path: ')

if(Case == True):
    file = find.find(filename, path, mon_yea_time)
    print(find.printFile(file))
else:
    start = True
