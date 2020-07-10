# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)


#Code starts here
census=np.concatenate((new_record,data))
census.shape
age=census[0:,0:1]
max_age=np.max(age)
min_age=np.min(age)
print("maximum age is=" ,max_age)
print("minimum age is=",min_age)
age_mean=np.mean(age)
print("mean age is=",age_mean)
age_std=np.std(age)
print("std deviation is=",age_std)
caste=census[0:,2:3]
race=np.array(census[0:,2:3],dtype=int)

race_a=[]
race_b=[]
race_c=[]
race_d=[]
race_e=[]
for i in range(0,len(race)):
    if race[i]==0:
        a=census[i]
        race_a.append(a)
        race_0=np.array(race_a)
    elif race[i]==1:
        b=census[i]
        race_b.append(b)
        race_1=np.array(race_b,dtype=int)
    elif race[i]==2:
        c=census[i]
        race_c.append(c)
        race_2=np.array(race_c,dtype=int)
    elif race[i]==3:
        d=census[i]
        race_d.append(d)
        race_3=np.array(race_d,dtype=int)
    else:
        e=census[i]
        race_e.append(e)
        race_4=np.array(race_e,dtype=int)

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

minority_race=3
senior_citizen_1=[]
for i in range(0,len(age)):
    if age[i]>60:
        a=census[i]
        senior_citizen_1.append(a)
senior_citizens=np.array(senior_citizen_1,dtype=int)

hours=senior_citizens[0:,6:7]
working_hours_sum=np.sum(hours)
print("total no of working hours of senior citizens=",working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print("average of working hours of senior citizens=",avg_working_hours)

income=census[0:,7:]
high_p=[]
high_inc=[]
low_p=[]
low_inc=[]
education_num=census[0:,1:2]
for i in range(0,len(education_num)):
    if education_num[i]>10:
        a=census[i]
        c=income[i]
        high_p.append(a)
        high=np.array(high_p,dtype=int)
        high_inc.append(c)
        y=np.array(high_inc,dtype=int)
        avg_pay_high=np.mean(y)
        print()
    else:
        b=census[i]
        d=income[i]
        low_p.append(b)
        low=np.array(low_p,dtype=int)
        low_inc.append(d)
        z=np.array(low_inc,dtype=int)

avg_pay_high=np.mean(y)
print("average high pay=",avg_pay_high)
avg_pay_low=np.mean(z)
print("average low pay=",avg_pay_low)
    




