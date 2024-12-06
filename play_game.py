
import time
import random 
import os
desktop_path = r"C:\Users\ASUS\Desktop\g2\records.txt"
if not os.path.exists(desktop_path):
    with open(desktop_path, "w") as file:
        file.write("")  
with open(desktop_path, "r") as file:
    lines = file.readlines()
# print(type(lines))
# print(len(lines))
# print(lines[0])
# print(type(lines[0]))
# print(eval(lines[0]))
# print(type(eval(lines[0])))
dictionaries=[]
for data in lines:
    #print(eval(data))
    dictionaries.append(eval(data))
# min_time = 100
# min_data = None  # برای ذخیره دیکشنری با کمترین زمان
# for data in dictionaries:
#     if data["time"] < min_time:
#         min_time = data["time"]
#         min_data = data  # ذخیره دیکشنری جدید با کمترین زمان

# if min_data:
#     print(min_data)
# print(min_time)
min_time = 100
dict_bestrecord = None
for data in dictionaries:
    if data["time"] < min_time:
        min_time = data["time"]
        dict_bestrecord = data
print(min_time)
print(dict_bestrecord)
print(f"the best record is belong to {dict_bestrecord["name"]} with {dict_bestrecord["time"]} seconds")
user_name = input("enter yr name: ")
random_num=random.randint(0,100)
print(random_num)
start_time = time.perf_counter()  
count = 0 

while True:
    count +=1
    try:
        num = int(input("enter a number in range limit:"))
        if num < random_num:
            print("the main number is bigger than yours,enter a number bigger than this")
        elif num > random_num:
            print("the main number is smaller than yours,enter a number smaller than this")
        else:
            print("u got it")
            break

    except ValueError:
        print("invalid input,pls enter an integer")
print(count)
end_time = time.perf_counter()
elapsed_time = round(end_time - start_time)
print(f"Elapsed time: {elapsed_time} seconds")
dict_1 ={"name":user_name, "time":elapsed_time, "counter":count}
desktop_path = r"C:\Users\ASUS\Desktop\g2\records.txt"
with open(desktop_path, "a") as file:
    file.write(f"{dict_1}\n")
print(f"Result saved to {desktop_path}")

