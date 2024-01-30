"""
Refer to the Pseudocode File (Task_14_Pseudocode.txt) for details on the program's functionality
Task 14.1 Programming with User-defined Functions (holiday.py)
Program starts: Define the functions for: City, Single or Couple (No. of travellers), Hotel Cost, Plane Cost, Hire Car Cost, Total Trip Quote Cost
State the variables and store the parameter placeholders (relevant to each def) to call and take in the actual values from the user, who should input a valid option from the list provided.
Checks included for: Negative value, illogical combination and symbols checks are in place, they will not break the program but the user will likely need to re-run and input valid inputs to get a complete trip quote
"""
# Initialise variables: 
import math
# Use of lists to store values for City and number of people options
city_list = ['amsterdam', 'dubai', 'dublin', 'lisbon', 'limassol', 'madrid', 'mumbai', 'paris', 'sydney', 'tokyo']
travellers_list = [1, 2]
# Define and obtain City user inputs, from the options in 'city_list'
def user_input_city(city_list):
    while True: # While Loop entered until user provides a valid option
        city_flight = input(f"\nEnter the city you will fly to (Amsterdam, Dubai, Dublin, Lisbon, Limassol, Madrid, Mumbai, Paris, Sydney, Tokyo): ")
        if city_flight.lower() in city_list:    # Use of conditional If/Else statements
               return city_flight.lower()
        else:   # If invalid option is entered the function prints an error message and prompts user again
            print("Error: Please enter a valid City Option: Amsterdam, Dubai, Dublin, Lisbon, Limassol, Madrid, Mumbai, Paris, Sydney, Tokyo.")
# Define and obtain the number of travellers, can be 1 or 2 (i.e. Single or Sharing couple, not built for > 2 persons group bookings)
def get_num_people(travellers_list):
    while True:
        try:
            num_people = int(input(f"\nAre you traveling on your own or sharing a room? Please enter 1 or 2 only: "))
            if num_people in travellers_list:
                return num_people
            else:
                print("Error: Please enter 1 or 2 only.")
        except ValueError:  # Use of try-except blocks to make the program error-tolerant and able to handle exceptions
            print("Error: Please enter a valid number.")
# Costs: Hotel, Flights, Hire Car
# HOTEL COSTS
def hotel_cost(num_nights, city_flight):
    try:
        # Number of nights input by user must be a positive whole number integer
        if not isinstance(num_nights, int) or num_nights < 0:  # Use of 'isinstance(object, classinfo)', where object is the variable to check, and classinfo of the integer class. If user enters 0 for no hotel nights, output will be £0
            raise ValueError("Error: Please enter a valid number of nights that you wish to stay at the hotel.")    # Use of 'raise' statement for exception handling where the 'if' statement condition is not true
        # Use of dictionaries containing the key-value pair items: Hotel Costs in chosen City
        hotel_costs = {
            'amsterdam': 100,
            'dubai': 300,
            'dublin': 150,
            'lisbon': 275,
            'limassol': 350,
            'madrid': 400,
            'mumbai': 200,
            'paris': 450,
            'sydney': 300,
            'tokyo': 555
        }
        # Use of the 'get()' method for dictionaries to retrieve values from a specific key: Hotel Cost for City selected
        hotel_cost_per_night = hotel_costs.get(city_flight.lower())
        if hotel_cost_per_night is None:    # If value is not found, default to 'None' and 'raise ValueError'.
            raise ValueError("Error: City entered not valid. Hotel Cost not available.")
        # Calculation Hotel Cost: Always 1 Room: Calculation is same for single (1 person) or sharing (2 people) a room
        return num_nights * hotel_cost_per_night
    except ValueError as Verror:    # Descriptive vairable 'Verror' for ValueError
        print(f"Error: {Verror}")
        return 0
# FLIGHT COSTS
def plane_cost(city_flight, num_people):
    try:
        # City input by user must be a string
        if not isinstance(city_flight, str):
            raise ValueError("Error: The City must be typed as seen in the list of options provided.")
        # Use of dictionaries containing the key-value pair items: Flight Costs to chosen City
        flight_costs = {
            'amsterdam': 75,
            'dubai': 700,
            'dublin': 50,
            'lisbon': 250,
            'limassol': 350,
            'madrid': 200,
            'mumbai': 1100,
            'paris': 150,
            'sydney': 1800,
            'tokyo': 1050
        }
        # Use of the 'get()' method for dictionaries to retrieve values from a specific key: Flight Cost for City selected
        flight_cost = flight_costs.get(city_flight.lower())
        if flight_cost is None:
            raise ValueError("Error: City entered not valid. Flight Cost not available.")
        # Calculation Hotel Cost: Flight cost total, multiplied by the number of people (either 1 or 2)
        return flight_cost * num_people
    except ValueError as Verror:
        print(f"Error: {Verror}")
        return 0
# HIRE CAR COSTS
def car_rental(city_flight, rental_days):
    try:
        # Number of days input by user must be a positive whole number integer
        if not isinstance(rental_days, int) or rental_days < 0:
            raise ValueError("Error: Please enter a valid number of days that you wish to rent the hire car for.")
        # Use of dictionaries containing the key-value pair items: Hire Car Costs in chosen City
        city_car_costs = {
            'amsterdam': 25,
            'dubai': 75,
            'dublin': 27,
            'lisbon': 35,
            'limassol': 40,
            'madrid': 60,
            'mumbai': 15,
            'paris': 45,
            'sydney': 35,
            'tokyo': 55
        }
        # Use of the 'get()' method for dictionaries to retrieve values from a specific key: Hire Car Cost for City selected
        perday_car_cost = city_car_costs.get(city_flight.lower())
        if perday_car_cost is None:
            raise ValueError("Error: City entered not valid. Hire Car Cost not available.")
        # Calculation Hire Car Cost: Always 1 Car: Calculation is same for single (1 person) or sharing (2 people) a car
        return rental_days * perday_car_cost
    except ValueError as Verror:
        print(f"Error: {Verror}")
        return 0
# CALCULATION TRIP QUOTE
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental
# OBTAIN USER INPUTS AND OUTPUT TRIP QUOTE RESULTS
def main(): # Define as a main function
    while True:
        try:
            print("\nWelcome to QuickTrips Quote Generator!")
            city_flight = user_input_city(city_list)
            num_people = get_num_people(travellers_list)
            num_nights = int(input(f"\nState the number of nights you wish to stay at the hotel: "))
            rental_days = int(input(f"\nState the number of days you need a hire car for (if you do not need a hire car please enter 0): "))
            # Calculate the cost of each element of the trip
            total_hotel = hotel_cost(num_nights, city_flight)
            total_flight = plane_cost(city_flight, num_people)
            total_car = car_rental(city_flight, rental_days)
            # Calculate the total cost of the trip quoted
            total_cost = holiday_cost(total_hotel, total_flight, total_car)
            # Print out the quote for the user
            print(f"\n{city_flight.capitalize()} Trip Quote Breakdown:")
            print("----------------------------------")
            print(f"\nTotal Flights : £{total_flight}")
            print(f"Total Hotel ({num_nights}) Nights : £{total_hotel}")
            print(f"Total Hire Car ({rental_days}) Days : £{total_car}")
            print("\n----------------------------------")
            print(f"Total Trip Quote : £{total_cost}")
            print("----------------------------------")
            # Does the user want to build a quote for a different trip?
            another_holiday = input("\nWould you like to build a quote for a different trip? (please enter yes or no): ")
            if another_holiday.lower() != 'yes':    # Use of '!=' not equal operator to end program if anything other than 'yes' is input
                print("Thank you, for using QuickTrips. We hope to see you again soon!")
                break  # Exit the loop if the user does not wish to build another quote            
        except ValueError as Verror:
            print(f"Error: {Verror}")
        except Exception as exce:   # Descriptive variable 'exce' for exception
            print(f"An unexpected error occurred: {exce}")
# This is a script, use this idiom to run every script. (i.e. this is a script to be run and not just a library file to be imported)
if __name__ == "__main__":          
    main()
# Program ends