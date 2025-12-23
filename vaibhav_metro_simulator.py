# input data from metro_data.txt file and convert it into list form.
file = open('metro_data.txt','r')
all_line = file.readlines()
file.close()
lst = [] # stores all data in list form

for line in all_line :  
    line=line.strip()
    lst.append(line.split(','))
# index_finder finds all stations's index as same as in list.
def index_finder(station):
    for elements in lst:
        if station.lower() == 'vaishali':     # special case because vaishali and anand vihar has same index
            return 39
        elif station.lower() == 'noida electronic city': # special case because noida electronic city and noida sector 62 has same index
            return 55
        elif station.lower() == 'botanical garden' and line == 'blue': # special case because it has multiple indexes with respect to lines
            return 48
        elif station.lower() == 'botanical garden' and line == 'magenta': # special case because it has multiple indexes with respect to lines
            return 79

        elif elements[1].lower().strip() == station.lower().strip():  # convert list items into lower case and matching

            return (lst.index(elements))


def is_valid_color(color):     # check if color or line exist in our data list without giving any error
    color = color.lower().strip()

    if color == 'blue' or color == 'red' or color =='magenta':
        return True
    return False
       
# finding if station exists or not in our data list
def is_valid_station(name):
    name = name.lower().strip()
    for row in lst:
        if row[1].lower().strip() == name or row[2].lower().strip() == name:
            return True
    
    return False
        
# inputs with respect to different phases . this is for phase 1
try:
    input1 = int(input(f"1. metro timings\n2. journey planner\nenter 1 or 2 for the information:"))
    if input1 == 1 or input1 == 2:
        pass
except:
    print('Enter either 1 or 2')
    exit()
if input1 == 1:
    line = input(f'enter line colour(blue,magenta,red):').lower().strip()
    if not is_valid_color(line):   
        print('Enter valid color')
        exit()
    is_valid_color(line)
    i1 = input('source:').lower().strip() 
    is_valid_station(i1)
    if not is_valid_station(i1):       # checking , if not exist then exit the program without giving any error.
        print("Enter valid station")
        exit()
    initial_index = index_finder(i1)

    
    time = input('Enter time (hh:mm):').strip().split(':')
    
 # this is for phase 2   
elif input1 == 2:
    line = input('enter line colour(blue,magenta,red):').lower().strip()
    if not is_valid_color(line):   
        print('Enter valid color')
        exit()
    is_valid_color(line)
    i1 = input('Source:').lower().strip()
    is_valid_station(i1)
    if not is_valid_station(i1):       # checking , if not exist then exit the program without giving any error.
        print("Enter valid station")
        exit()

    i2 = input('Destination:').lower().strip() 
    is_valid_station(i2)
    if not is_valid_station(i2):
        print("Enter valid station")
        exit()
    initial_index = index_finder(i1)
    final_index = index_finder(i2)

    if i1 == i2 :
        print('You are already at that station')
        exit()
    
    time = input('Enter time (hh:mm):').strip().split(':')

try:      # checking the time format if it is wrong , then exit the program without giving any error
    hh, mm = time  
    hh = int(hh)                    
    mm = int(mm)
    if not (0 <= hh < 24 and 0 <= mm < 60):
        raise Exception
except:
    print("Enter valid time according to format (hh:mm)")
    exit()

def initial_time():       # create a list  [time[0],time[1]] to make next process easier
    time2 = []
    for time1 in time:
        time1 = time1.replace(' ','')
        time2.append(time1)
    return time2

def final_initial_time():      # make a proper output in standard format
    final = initial_time()
    return f'{final[0]}:{final[1]}'

#    if station is in red or another station in different lines or vice versa , there is no interchange exists.
if input1==2:
    if initial_index>=80 and final_index >=0 and final_index < 80 :
        print('There is no interchange between red line and other two colors.')
        exit()
    elif final_index >= 80 and initial_index >=0 and initial_index <80 :
        print('There is no interchange between red line and other two colors.')
        exit()

#    according to instructions , after 23:00 servies close , assume metro not available after 23;00 but if traveller already pick his train before 23:00 , then it will reach his destination and then close.
# if int(initial_time()[0])>=23 or int(initial_time()[0])<5:
#     print('services are closed')
#     exit()

# finding if there is any interchange or not by making all situations
if input1 == 2:       
    def if_interchange(initial_index,final_index):
        if initial_index >= 80 and final_index >=80:
            return 'No interchange'

        elif initial_index >= 40 and initial_index <=55 and final_index >=33 and final_index <= 39 :
            return 'There is interchange in blue line'
        elif final_index >= 40 and final_index <=55 and initial_index >=33 and initial_index <= 39 :
            return 'There is interchange in blue line'
        elif lst[initial_index][0] == lst[final_index][0]:
            return 'No interchange'
        # elif initial_index < final_index and line == 'blue':
        #     return 'no interchange'
        else :
            return 'There is interchange'

      
if input1 == 2:      # it is in phase 2 , so nested in specific condition. it tell's which line traveller have to go to reach his destination.
    def identifier():
        if lst[initial_index][0] == lst[final_index][0]:
            return f'Continue to same {lst[initial_index][0]} line'
        elif lst[initial_index][0]=='Blue' and lst[final_index][0]=='Magenta':
            return f'Transfer to magenta line'
        elif lst[initial_index][0].lower().strip()=='magenta' and lst[final_index][0].lower().strip()=='blue':
            return f'Transfer to blue line'


# this function calculates the shortest travel time by making all situations . I cannot think any algorithm or make proper function (sorry for making a long function) 
if input1 == 2:
    def travel_time(initial_index,final_index):
        interval_sum = 0
        sum12 = 0
        sum13=0
        if initial_index < final_index :
            if initial_index >=0 and initial_index <= 13 and final_index >= 56 :
                for i in range(initial_index,14):
                    
                    sum12 += int(lst[i][3])
                for i in range(56,final_index):
                    
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum

            elif initial_index >= 0 and initial_index <= 33 and final_index >= 40 and final_index <= 55:
                for i in range(initial_index,33):
                    sum12 += int(lst[i][3])
                for i in range(40,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 
                return interval_sum
            elif initial_index >= 33 and initial_index <= 39 and final_index >= 40 and final_index <= 55 :
                for i in range(33,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(40,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum
            elif initial_index >= 33 and initial_index <= 39 and final_index >= 67 and final_index <= 79 :
                for i in range(33,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(final_index,79):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 + 21

                return interval_sum
            elif initial_index >= 40 and initial_index <= 48 and final_index >= 56 and final_index <= 79 :
                for i in range(initial_index,49):
                    sum12 += int(lst[i][3])
                for i in range(final_index,80):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum
            elif initial_index >= 48 and initial_index <= 55 and final_index >= 56 and final_index <= 79 :
                for i in range(48,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(final_index,80):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum
            elif initial_index >=23 and initial_index <=33 and final_index >= 68 and final_index <= 79:
                for i in range(initial_index,34):
                    sum12 += int(lst[i][3])
                for i in range(final_index,80):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum

            
            
            elif initial_index < final_index :
                for i in range(initial_index,final_index):
                    sum12 += int(lst[i][3])
                interval_sum= sum12

                
                return interval_sum
        elif initial_index == final_index and lst[initial_index][1] != lst[initial_index][2]:
            interval_sum =  int(lst[initial_index][3])
            return interval_sum
        
        elif initial_index > final_index :
            if initial_index>= 56 and initial_index <= 79 and final_index >=0 and final_index <= 13:
                for i in range(56,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(final_index,13):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum
            elif initial_index >=56 and initial_index <= 60 and final_index >= 33 and final_index <= 39:
                for i in range(56,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(13,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 
                return interval_sum
            elif initial_index >=61 and initial_index <= 79 and final_index >= 33 and final_index <= 39:
                for i in range(initial_index,80):
                    sum12 += int(lst[i][3])
                for i in range(33,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 + 21
                return interval_sum
            elif initial_index >=56 and initial_index <= 79 and final_index >= 40 and final_index <=48 :
                for i in range(initial_index,80):
                    sum12 += int(lst[i][3])
                for i in range(40,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 
                return interval_sum
            elif initial_index >=56 and initial_index <= 79 and final_index >= 49 and final_index <= 55:
                for i in range(initial_index,80):
                    sum12 += int(lst[i][3])
                for i in range(50,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 
                return interval_sum
            elif initial_index>= 56 and initial_index <= 79 and final_index >= 13 and final_index <= 39:
                for i in range(56,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(13,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum
            elif initial_index>= 56 and initial_index <= 79 and final_index >= 13 and final_index <= 55:
                for i in range(56,initial_index):
                    sum12 += int(lst[i][3])
                for i in range(13,final_index):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13 - 18
                return interval_sum
            elif initial_index >=68 and initial_index <=79 and final_index >= 23 and final_index <= 33:
                for i in range(initial_index,80):
                    sum12 += int(lst[i][3])
                for i in range(final_index,34):
                    sum13 += int(lst[i][3])
                interval_sum = sum12 + sum13
                return interval_sum
            else :
                if initial_index >=40 and initial_index <=55 and final_index >=0 and final_index<=33: 
                    for i in range(initial_index -1,final_index -1,-1):
                        interval_sum += int(lst[i][3]) 
                    return interval_sum - 18
                elif initial_index >=40 and initial_index <=55 and final_index >= 34 and final_index <= 39 :
                    for i in range(40,initial_index):
                        sum12 += int(lst[i][3])
                    for i in range(33,final_index):
                        sum13 += int(lst[i][3])
                    return sum12 + sum13

                
                else :

                    for i in range(initial_index -1,final_index-1,-1):
                        interval_sum += int(lst[i][3])
                    return interval_sum

def list_interchange_stations(initial_index, final_index):
    inter_list = []

    if initial_index >= 40 and initial_index <= 55 and final_index >= 33 and final_index <= 39:
        inter_list.append("Yamuna Bank")

    elif initial_index >= 33 and initial_index <= 39 and final_index >= 40 and final_index <= 55:
        inter_list.append("Yamuna Bank")

    elif initial_index >= 40 and initial_index <= 55 and final_index >= 56 and final_index <= 79:
        inter_list.append("Botanical Garden")

    elif initial_index >= 56 and initial_index <= 79 and final_index >= 40 and final_index <= 55:
        inter_list.append("Botanical Garden")

    elif initial_index >= 56 and initial_index <= 79 and final_index >= 0 and final_index <= 13:
        inter_list.append("janakpuri west")

    elif initial_index > 61 and initial_index <= 79 and final_index > 13  and final_index <= 39:
        inter_list.append("Botanical Garden")
        inter_list.append('yamuna bank')
    elif initial_index >= 56 and initial_index <= 61 and final_index > 13  and final_index <= 33:
        inter_list.append("janakpuri west")
    elif initial_index >= 0 and initial_index <= 13 and final_index >= 56 and final_index <= 79:
        inter_list.append("janakpuri west")
    elif initial_index > 13 and initial_index <= 39 and final_index > 61  and final_index <= 79:
        inter_list.append("Botanical Garden")
        inter_list.append('yamuna bank')
    elif initial_index >= 13 and initial_index <= 33 and final_index >= 56   and final_index <= 61:
        inter_list.append("janakpuri west")
    

    elif initial_index >= 80 and final_index <= 79:
        inter_list.append("No Interchange (Red line isolated)")

    elif final_index >= 80 and initial_index <= 79:
        inter_list.append("No Interchange (Red line isolated)")

    return inter_list
if input1 == 2:
    inter_stations = list_interchange_stations(initial_index, final_index) 

def arrival_at_station(mid_station_name):
    mid_index = index_finder(mid_station_name)
    t = travel_time(initial_index, mid_index)
    total = station_delay(initial_index) + t
    base = time_conversion(final_initial_time())
    final_minutes = base + total
    time_h1 = int(final_minutes /60)
    time_m1 = final_minutes % 60


    if len(str(time_m1)) == 1 and len(str(time_h1)) == 2:    # fixing standard time format by adding 0 . ( 12:1 == 12:01 )
        return f'{time_h1}:0{time_m1}'
    elif len(str(time_m1)) == 1 and len(str(time_h1)) == 1:    # ( 2:3 == 02:03 )
        return f'0{time_h1}:0{time_m1}'
    elif len(str(time_m1)) == 2 and len(str(time_h1)) == 1:     # ( 2:30 == 02:30 )
        return f'0{time_h1}:{time_m1}'

    return f'{time_h1}:{time_m1}' 


delay = 0      # if there is interchange , then the function adds extra 5 minutes in travel time.
if input1 == 2: 
    def delay_interchange(delay = 0):
        if if_interchange(initial_index,final_index)=='There is interchange' or if_interchange(initial_index,final_index)=='There is interchange in blue line':
            delay = 5
            return delay
        elif len(inter_stations) >1 :
            delay = 10
            return delay
        else :
            return 0
    
def time_conversion(time):     # function : convert time format into minutes
    if ':' in str(time):
        hours, minutes = time.split(':')
    else:
        hours = time[0]
        minutes = time[1]
    return int(hours)*60 + int(minutes)
# this is time intervals between their starting station to at current station, in phase 1 : assuming metro goes only in one direction
if input1 == 1 and line=='red':       # this is for red line
    def frequency(initial_index):
        interval_sum = 0
        for i in range(80,initial_index):
            interval_sum += int(lst[i][3])                              
        return interval_sum

    

    
if input1 == 1 and line=='blue' :       # this is for blue line
    def frequency(initial_index):
        interval_sum = 0
        for i in range(0,initial_index):
            interval_sum += int(lst[i][3])                             
        return interval_sum


    
if input1 == 1 and line=='magenta':       # this is for magenta line
    def frequency(initial_index):
        interval_sum = 0
        for i in range(56,initial_index):
            interval_sum += int(lst[i][3])                              
        return interval_sum


elif input1 == 2:      # in phase 2 : i consider metro moving in both direction . here are time intervals according to all cases
    def frequency(initial_index):
        interval_sum = 0
        if initial_index < final_index and line =='blue':    # metro moving from dwarka sec 21 to either vaishali or noida
            for i in range(0,initial_index):
                interval_sum += int(lst[i][3])
        elif initial_index < final_index and line == 'magenta':     # metro moving from janakpuri west to botanical garden
            for i in range(56,initial_index):
                interval_sum += int(lst[i][3])
        elif initial_index > final_index and initial_index >= 33 and initial_index <=39 :    # metro moving from vaishali to dwarka sec 21
            for i in range(initial_index,40):
                interval_sum += int(lst[i][3])
        elif initial_index > final_index and initial_index >= 40 and initial_index <=55 :     # metro moving from noida electronic city to dwarka sec 21
            for i in range(initial_index,56):
                interval_sum += int(lst[i][3])
        elif initial_index > final_index and initial_index >=56 and initial_index <=79:   # metro moving from botanical garden to janakpuri west
            for i in range(initial_index,80):
                interval_sum += int(lst[i][3])
        elif initial_index < final_index and initial_index >=80:       # metro moving from saheed sthal to rithala
            for i in range(80,initial_index):
                interval_sum += int(lst[i][3])
        elif initial_index > final_index and initial_index >=80:        # metro moving from rithala to saheed sthal
            for i in range(initial_index,108):
                interval_sum += int(lst[i][3])
        return interval_sum




def station_delay(initial_index):                           # i am calculating the delay time (metro not arrived at station yet) traveller should face while travelling
    metro_time = 360+frequency(initial_index)

    if int(initial_time()[0]) >= 8 and int(initial_time()[0]) < 10 : 
        while metro_time < int(time_conversion(initial_time())):
           metro_time +=  4                                                  # increment by 4 on peak hours
        station_delay = metro_time - int(time_conversion(initial_time()))
        return station_delay
    
    elif int(initial_time()[0]) >= 17 and int(initial_time()[0]) <19 :
        while metro_time < int(time_conversion(initial_time())):
           metro_time +=   4                                                # increment by 4 on peak hours
        station_delay = metro_time - int(time_conversion(initial_time()))    
        return station_delay
    else :
        while metro_time < int(time_conversion(initial_time())):
            metro_time +=    8                                              # increment by 8 on offpeak hours
        station_delay = metro_time - int(time_conversion(initial_time()))
        return station_delay



def next_metro_time():                      # i am calculating the time of next metro arrival at the same station
    time = time_conversion(initial_time()) + station_delay(initial_index)
    time_h= int((time-(time%60))/60)
    time_m = time%60
    if time_conversion(initial_time()) > 1376 + frequency(initial_index) or time_conversion(initial_time()) < 360  :
            print('services are closed')
            exit()
    elif len(str(time_m)) == 1 and len(str(time_h)) == 2:
        return f'{time_h}:0{time_m}'
    elif len(str(time_m)) == 1 and len(str(time_h)) == 1:
        return f'0{time_h}:0{time_m}'
    elif len(str(time_m)) == 2 and len(str(time_h)) == 1:
        return f'0{time_h}:{time_m}'

    return f'{time_h}:{time_m}'






if input1==1:                           # for phase 1: time calculation of next to next metro at the same station
    def next_metro_time1():
        if int(initial_time()[0])>=8 and int(initial_time()[0]) < 10 :          # peak hours , increment by 4
            time = time_conversion(initial_time()) + station_delay(initial_index) +4
        elif int(initial_time()[0])>=17 and int(initial_time()[0]) < 19:        # peak hours , increment by 4
            time = time_conversion(initial_time()) + station_delay(initial_index) +4
        else :                                                                  # offpeak hours , increment by 8
            time = time_conversion(initial_time()) + station_delay(initial_index) +8
        time_h1= int((time-(time%60))/60)
        time_m1 = time%60
    
        if int(time_conversion(initial_time())) > 1376 + frequency(initial_index)  or int(time_conversion(initial_time())) < 360:  #  metro cannot  arrived after 23:00 or before 6:00 at the initial station 
            print('Services are closed')
            exit()

        elif len(str(time_m1)) == 1 and len(str(time_h1)) == 2:    # fixing standard time format by adding 0 . ( 12:1 == 12:01 )
            return f'{time_h1}:0{time_m1}'
        elif len(str(time_m1)) == 1 and len(str(time_h1)) == 1:    # ( 2:3 == 02:03 )
            return f'0{time_h1}:0{time_m1}'
        elif len(str(time_m1)) == 2 and len(str(time_h1)) == 1:     # ( 2:30 == 02:30 )
            return f'0{time_h1}:{time_m1}'

        return f'{time_h1}:{time_m1}'

if input1 == 2:
    def final_hour():                   # calculating arrival time of the final station
        final_time = int(station_delay(initial_index)) + int(travel_time(initial_index,final_index)) + int(time_conversion(initial_time())) + int(delay_interchange(delay=0))
        final_time_h= int((final_time - (final_time%60))/60)
        final_time_m = int(final_time%60)
        if int(time_conversion(initial_time())) > 1376 + frequency(initial_index)  or int(time_conversion(initial_time())) < 360:
            print('Services are closed')
            exit()
        elif len(str(final_time_h))==1 and len(str(final_time_m))==1:
            return f'0{final_time_h}:0{final_time_m}'
        elif len(str(final_time_h))==1 and len(str(final_time_m))==2:
            return f'0{final_time_h}:{final_time_m}'
        elif len(str(final_time_h))==2 and len(str(final_time_m))==1:
            return f'{final_time_h}:0{final_time_m}'
        return f'{final_time_h}:{final_time_m}'

def travelling_time():              # total travel time including delay at initial station because of delay
    time = time_conversion(final_hour()) - time_conversion(final_initial_time())
    return time

def fare_calculation():       # fare calculating according to how much time traveller took
    net = travelling_time() 
    if net >=0 and net <= 5 :
        return 10
    elif net > 5 and net <= 10:
        return 20
    elif net >10 and net <= 20 :
        return 30
    elif net > 20 and net <= 30:
        return 40
    elif net > 30 and net <= 50 :
        return 50
    elif net >50 :          # maximum fare is 64 in blue,magenta or red line
        return 64

if input1 == 1:
    print()
    print('--------------------------------------------------------------------------------------------------------------------')
    print()
    print(f'Subsequent metros at: {next_metro_time()} , {next_metro_time1()} ....')
    print()
    print('--------------------------------------------------------------------------------------------------------------------')
    

if input1 == 2:
    print()
    print()
    print('------------------------------------------------------:Journey plan:--------------------------------------------------\n')
    print()
    print(f'Start at {lst[initial_index][1]} ({lst[initial_index][0]}) line \n')
    print(f'Delay at initial station: {station_delay(initial_index)} \n')
    print(f'Next metro at: {next_metro_time()} \n')
    print(f'interchange stations is: {inter_stations} \n')
    if len(inter_stations) == 0:
        print("No interchange")
    else:
        for st in inter_stations:
            print(f"{st} (Arrival at {arrival_at_station(st)})")


    print(f'\nArrive at {i2} at {final_hour()} \n')
    print(identifier())
    print()
    print(f'Total travel time: {travelling_time()} minutes \n')


    print(f'Your total fare is: Rs{fare_calculation()} \n')
    print()
    print('----------------------------------------------------------------------------------------------------------------------')


    
    



    






        









            
        









    
    





        


            



    




            
        














