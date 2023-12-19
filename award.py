
"""
Task 4.1 Logical Programming - Operators file award.py

Start
1. Determine the award triathlete will receive.
2. Read times (in minutes) for all three events: swimming, cycling, and running.
3. Calculate and print the total time taken to complete the triathlon.
4. Award: Ranked by total time taken to complete triathlon.
5. The qualifying time for awards is 100 minutes.
6. Qualifying time range.                           0 - 100 minutes.    Award == Provincial Colours.
7. Qualifying time range 100 + >=1 and <=5 minutes. 101 - 105 minutes.  Award == Provincial Half Colours.
8. Qualifying time range 100 + >=6 and <=10.        106 - 110 minutes.  Award == Provincial Scroll. 
9. Qualifying time range 100 + >=11.                111+ minutes.       Award == No award.
End

"""

# Initialise variables. Request user times for all three events. Award: Ranked by total time taken to complete triathlon. 

triathlete_time_swim = float(input("Please enter your swim time that you were given in minutes here : "))
triathlete_time_cycle = float(input("Please enter your cycle time that you were given in minutes here : "))
triathlete_time_run = float(input("Please enter your run time that you were given in minutes here : "))

# Sum the three time events and convert to an integer.

triathlete_time = int(triathlete_time_swim + triathlete_time_cycle + triathlete_time_run)

# Qualifying time range. 0 - 100 minutes. Award == Provincial Colours.

if  triathlete_time >=0 and triathlete_time <=100:
        
    print(f"\nCongratulations, you completed the triathlon in {triathlete_time} minutes, as such you have been awarded: Provincial Colours!")

# Qualifying time range 100 + >=1 and <=5 minutes. 101 - 105 minutes. Award == Provincial Half Colours.

elif    triathlete_time >=101 and triathlete_time <=105:

    print(f"\nGood effort, you completed the triathlon in {triathlete_time} minutes, as such you have been awarded the second tier: Provincial Half Colours!")

# Qualifying time range 100 + >=6 and <=10. 106 - 110 minutes. Award == Provincial Scroll. 

elif    triathlete_time >=106 and triathlete_time <=110:

    print(f"\nYou completed the triathlon in {triathlete_time} minutes, as such you have been awarded the third tier: Provincial Scroll")

# Qualifying time range 100 + >=11. 111+ minutes. Award == No award.

elif    triathlete_time >=111:

    print(f"\nBetter luck next time, you completed the triathlon in {triathlete_time} minutes, as such on this occasion you have not qualified for an award.")

# User entered a number of minutes below 0.

elif    triathlete_time < 0: 

    print(f"\nUser error, it is not possible that your triathlon time is {triathlete_time} minutes as this is a negative number.") 

# User has entered a time that is not recognised.

else:

    print(f"\nThe time you have recorded does not qualify for an award.") 



# Program ends