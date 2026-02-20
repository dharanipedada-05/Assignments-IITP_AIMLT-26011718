total_seats = 350
tickets_sold = 0
total_bookings = 0
rejected_bookings = 0
while total_seats > 0:
    required_seats=int(input("Enter number of tickets: "))
    if required_seats == 0:                                          #Exit Condition
        break
    if required_seats <1 or required_seats > 15:                     #Validating Range of required seats
        print("Invalid number of seats. 1-15 only")
        continue
    if required_seats > total_seats:                                 #Check seat availability
        print("Not enough seats available")
        rejected_bookings += 1
        continue
    ages = []
    age_rejected = False 
    for i in range(required_seats):                      #Taking ages
        age = int(input(f"Enter age of seat {i + 1}: "))
        ages.append(age)
        if age < 12:
            age_rejected = True
    if age_rejected:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1
        continue
    print(f"BOOKING CONFIRMED - {required_seats} tickets")
    total_bookings += 1
    tickets_sold += required_seats
    total_seats -= required_seats

print("\nFINAL REPORT")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {total_seats}")