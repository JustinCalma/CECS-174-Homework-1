#Main
def main():
    menu()

#Cost of Fuel Function
def cost_Fuel():
#Car 1's first input
    while True:
        try:
            car_1_kW = float(input("Enter Car 1's kW-h/mi: "))     
            if car_1_kW <= 0:
                print("ERROR: Enter a positive integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")
    
#Car 1's second input
    while True:
        try:
            car_1_cost = float(input("Car 1's cost per kilowatt-hour: "))
            if car_1_cost <= 0:
                print("ERROR: Enter a positive integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")

#Car 2's first input
    while True:
        try:
            car_2_MPG = float(input("Car 2's miles-per-gallon: "))
            if car_2_MPG <= 0:
                print("ERROR: Enter a positive integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")

#Car 2's second input
    while True:
        try:
            car_2_cost = float(input("Car 2's cost per gallon: "))
            if car_2_cost <= 0:
                print("ERROR: Enter a positive integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")

#Average distance driven each month in miles
    avg_Dist = input("Average distance driven: ")         
    run = False
    counter = 0
    while run == False:     
        for char in avg_Dist:
            if char.isdigit() == False:
                print("ERROR: Enter a positive integer")
                avg_Dist = input("Re-enter the Average distance: ")
                break
            counter = counter + 1
        if counter == len(avg_Dist):
            run = True
    avg_Dist = int(avg_Dist)

#Calculate the amount of money to drive each car for a year
    car_1_Cost_per_Year = (avg_Dist * 12) * (car_1_kW * car_1_cost)
    car_2_Cost_per_Year = (avg_Dist * 12) / ((car_2_MPG / car_2_cost))

#Printing outputs
    if car_1_Cost_per_Year > car_2_Cost_per_Year:
        cost_Diff = car_1_Cost_per_Year - car_2_Cost_per_Year
        print("Car 2 will save you $", format(cost_Diff, ".2f"), "in a year")
        
    elif car_2_Cost_per_Year > car_1_Cost_per_Year:
        cost_Diff = car_2_Cost_per_Year - car_1_Cost_per_Year
        print("Car 1 will save you $", format(cost_Diff, ".2f"), "in a year")
        
    elif car_1_Cost_per_Year == car_2_Cost_per_Year:
        print("The two cars cost the same.")

#Used Value Function
def used_Value():

#Get the car's original price
    while True:
        try:
            car_Orig_Price = float(input("Car's original price: "))
            if car_Orig_Price <= 0:
                print("ERROR: Enter a positive integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")

#Get how many years to track
    while True:
        try:
            year_to_Track = int(input("Enter how many yeaars to track: "))
            if year_to_Track <= 0:
                print("ERROR: Enter a positve integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")

#Calculate car's worth each year
    for i in range(year_to_Track + 1):
        if i != 0:
            print("Year %d value: $%.2f" % (i, car_Orig_Price))
        car_Orig_Price = car_Orig_Price * 0.82 #Depreciation rate of 18%

#Calculate Stopping Distance function
def calc_Stopping_Dist():

#Get car's velocity
    while True:
        try:
            car_Speed = float(input("Enter the car's velocity: "))
            if car_Speed <= 0:
                print("ERROR: Enter a positive integer")
                continue
            break
        except ValueError:
            print("ERROR: Enter a positive integer")

#Converting miles/hr to ft/s
    car_Velocity = car_Speed * (5280 / 3600)

#Check tire's condition
    while True:
        try:
            tire_Condition = int(input("1.- New Tires\n2.- Good Tires\n3.- Poor Tires\nEnter the tire's condition: "))
            if tire_Condition <= 0 or tire_Condition >= 4:
                print("ERROR: Enter a valid choice")
                continue
            break
        except ValueError:
            print("ERROR: Enter a valid choice")

#Setting Constant Variable
    NEW_TIRES = 0.8
    GOOD_TIRES = 0.6
    POOR_TIRES = 0.4
    GRAVITY_ACCEL = 32.174

#Setting friction coeffiction and Calculating Stopping Distance
    if tire_Condition == 1:
        tire_Condition = NEW_TIRES
        stopping_Dist = ((car_Velocity) ** 2) / (2*(tire_Condition) * (GRAVITY_ACCEL))
        print("At",car_Speed, "mi/hr, with new tires, the car will stop in", format(stopping_Dist, ".2f"), "feet")
    elif tire_Condition == 2:
        tire_Condition = GOOD_TIRES
        stopping_Dist = ((car_Velocity) ** 2) / (2*(tire_Condition) * (GRAVITY_ACCEL))
        print("At",car_Speed, "mi/hr, with good tires, the car will stop in", format(stopping_Dist, ".2f"), "feet")
    elif tire_Condition == 3:
        tire_Condition = POOR_TIRES
        stopping_Dist = ((car_Velocity) ** 2) / (2*(tire_Condition) * (GRAVITY_ACCEL))
        print("At",car_Speed, "mi/hr, with poor tires, the car will stop in", format(stopping_Dist, ".2f"), "feet")
          
#Menu
def menu():
    print("\n1.- Cost of Fuel")
    print("2.- Used Value")
    print("3.- Stopping Distance")
    print("4.- Quit")
  
    a = input("Select a function: ")
    run = False
    counter = 0
    while run == False:     
        for char in a:
            if char.isdigit() == False:
                print("ERROR: Enter a number between 1 and 4")
                a = input("Enter a number: ")
                break
            counter = counter + 1
        if counter == len(a):
            run = True
    decision = int(a)

    if decision == 1:
        cost_Fuel()
        menu()
    elif decision == 2:
        used_Value()
        menu()
    elif decision == 3:
        calc_Stopping_Dist()
        menu()
    elif decision == 4:
        quit()
    else:
        print("ERROR: Select a number from 1 to 4")
        menu()
  
main()


