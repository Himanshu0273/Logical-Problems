# time = input("Enter time in 24hr hh:mm format: ")
# # hours = time[:2]
# # minutes = time[3:]
# # h1 = ord(hours[0])-ord("0")
# # h2 = ord(hours[1])-ord("0")
# # hh = ((h1*10)+h2)%12
# # print("Hours: ", hh)
# # m1 = ord(minutes[0])-ord("0")
# # m2 = ord(minutes[1])-ord("0")
# # mm = (m1*10)+m2
# # print("Minutes: ",mm)
# hh,mm = map(int,time.split(':'))
# hh%=12
# print(hh, mm) 

# if hh>12 or mm>60:
#     print("Invalid Input")
# else:
#     from_12_hh = (hh*30)
#     from_12_mm = ((mm%5)*6) + ((mm//5)*30)
#     deg = abs(from_12_hh-from_12_mm)
#     mini = min(360-deg, deg)
#     print("Angle: ", deg)


# Python program to find angle 
# between hour and minute hands

# Function to Calculate angle b/w 
# hour hand and minute hand 
def calcAngle(h,m):
        
        # validate the input
        if (h < 0 or m < 0 or h > 12 or m > 60):
            print('Wrong input')
        
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            h += 1;
            if(h>12):
                   h = h-12;
        
        # Calculate the angles moved by 
        # hour and minute hands with 
        # reference to 12:00
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m
        
        # Find the difference between two angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller angle of two 
        # possible angles
        angle = min(360 - angle, angle)
        
        return angle

# Driver Code 
print(calcAngle(6,42))

# This code is contributed by Danish Raza