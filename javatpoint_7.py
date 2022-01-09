import math
train1_length = int(input("Enter the length of train 1:"))
train2_length = int(input("Enter the length of train 2:"))
train1_speed = int(input("Enter the speed of train 1:"))
train2_speed = int(input("Enter the speed of train 2:"))
relative_speed = train1_speed + train2_speed
r_s = relative_speed * 5/18
distance = train1_length + train2_length
time = distance / r_s
print("The time taken for crossing:", time)
exit (0)
