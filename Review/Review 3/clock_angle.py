time = input("Enter time in 24hr hh:mm format: ")
hours = time[:2]
minutes = time[3:]
h1 = ord(hours[0])-ord("0")
h2 = ord(hours[1])-ord("0")
hh = ((h1*10)+h2)%12
print("Hours: ", hh)
m1 = ord(minutes[0])-ord("0")
m2 = ord(minutes[1])-ord("0")
mm = (m1*10)+m2
print("Minutes: ",mm)

if hh>12 or mm>60:
    print("Invalid Input")
else:
    from_12_hh = (hh*30)
    from_12_mm = ((mm%5)*6) + ((mm/5)*30)
    deg = abs(from_12_hh-from_12_mm)
    # mini = min(360-deg, deg)
    print("Angle: ", deg)