# metro_simulator.pyy
I made a metro journey planner that tells about the costs, timings, shortest routes, interchanges. It is ment to help people who are new in India (Delhi) to find metro routes.
This is Metro Simulator works based on approx real data. It returns informations which need in travelling by Metro.
the Simulation needs your initial information and it returns (Final destination time) , (Total travelling time) , (next Metro Time) , (Subsequent Metro's Time) , (Interchange If any between Stations) , (Delay at initial Station) .


Data Sources
- [For Blue Line](https://delhimetrorail.com/line/LN3)
- [For Blue Line branch towards Vaishali](https://delhimetrorail.com/line/LN4)
- [For Magenta Line](https://delhimetrorail.com/line/LN8)
- [For Red Line](https://delhimetrorail.com/line/LN1)
- [For Time between stations](https://delhimetrorail.com/map)


PHASE 1: (Metro Timings)
If user select option 1 :
It will ask Line , Initial Station and Time .
after Run the program , Program shows 
1. next metro time
2. next to next metro time
Handling - 1. It handles off-peak hours 
           2. peak hours ,
           3. If metro servies availabe after 23:00 or before 6:00 ,
           4. add station delays at initial stations and frequency 

PHASE 2: (Journey Planner)
If user select option 2:
It will ask Line , Initial Station , Final Station and Time .
after Run the program , It shows
1. Metro stating time considering delay
2. delay at initial station
3. next metro timings
4. gives list of interchange stations and their arrival times at that stations
5. Calculates  final arrival time
6. Shows on which line user should move
7. Total travel time including interchange delay at interchange stations
8. fare calculation between stations



Data file format : (line color , station , next station , time interval , if interchange)

Steps to run the Program (metro_simulator):
step 1 : select mode (either 1 or 2)
step 2 : Inputs of mode 1 -  Line(red,magenta,blue)
                          -  source (initial-metro-station)
                          - Time (hh:mm)
         Inputs of mode 2 - Line (red,magenta,blue)
                          - source (initial-metro-station)
                          - destination (final-metro-station)
                          - Time (hh:00)


FUNCTIONS in this code :
1. is_valid_colour(color)
2. index_finder(station)
3. is_valid_station()
4. is_valid_color()
5. initial_time()
6. final_initial_time()
7. if_interchange(initial_index,final_index)
8. identifier()
9. travel_time()
10. list_interchange_stations(initial_index,final_index)
11. arrival_at_station(mid_station_name)
12. delay_interchange()
13. time_conversion(time)
14. frequency(initial_index)
15. station_delay()
16. next_metro_time()
17. final_hour()
18. travelling_time()
19. inter_stations



sample inputs:

How to Run
1. Keep `metro_data.txt` in the same folder.
2. Run the script:
3. Choose:
  1 - next metro timing  
  2 - route planner  

example 1 :
1. metro timings
2. journey planner
enter 1 or 2 for the information:1 (INPUT)
enter line colour(blue,magenta,red):blue (INPUT)
source:mandi house (INPUT)
Enter time (hh:mm):12:03 (INPUT)

(OUTPUT)

--------------------------------------------------------------------------------------------------------------------

Subsequent metros at: 12:07 , 12:15....

--------------------------------------------------------------------------------------------------------------------

example 2 :

1. metro timings
2. journey planner
enter 1 or 2 for the information:2 (INPUT)
enter line colour(blue,magenta,red):magenta (INPUT)
Source:hauz khas (INPUT)
Destination:golf course (INPUT)
Enter time (hh:mm):12:45 (INPUT)

(OUTPUT)
------------------------------------------------------:Journey plan:--------------------------------------------------


Start at Hauz Khas (Magenta) line 

Delay at initial station: 0 

Next metro at: 12:45 

interchange stations is: ['Botanical Garden'] 

Botanical Garden (Arrival at 13:12)

Arrive at golf course at 13:19 

Transfer to blue line

Total travel time: 34 minutes 

Your total fare is: Rs50     [ EXTRA FUNCTIONALITY ]


----------------------------------------------------------------------------------------------------------------------


Algorithms Used

 
make a index finder function and calculate travel time by making all possibilities
for calculating next metro timings , used mathematical formulas

Train Frequency  
1.Peak hours (8–10 AM, 5–7 PM): every (4 minutes)
2.Other times: every (8 minutes)
3.services off after 23:00 except last metro departs

ASSUMPTIONS: 
1. Time must be in (HH:MM) format.
2. Line and station names are automatically converted to lowercase.
3. Program handles invalid inputs gracefully.
4. Red line metro has no any interchange with blue or magenta line.
5. if user picked a metro before yamuna bank , I assume He pick the right metro where he wants to go.
   for ex-  if user wants to go at laxmi nagar , then he picked 'VAISHALI' metro 
            or if user wants to go at botanical garden , then he picked 'NOIDA ELECTRONIC CITY' metro.
6. in the morning after 6 am , metro may take more time because there is only two metros starts just after 6:00 from both directions
