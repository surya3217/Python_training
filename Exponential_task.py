'''
Suraj Kumar Saini
www.linkedin.com/in/suraj-saini-8a1027143/
https://github.com/surya3217
'''

# my generic solution to update dictionary
def recurse_dict(dd, d2):

    for key in d2.keys():  # finding the key from d2 dict to update
        print(key)
        if type(d2[key])==dict:   # checking the data type of dict val
            dd[key]= recurse_dict(dd[key], d2[key])    # moving to next inside key of dict using recursion
        else:
            dd[key]= d2[key]         # if dict val is normal than just updating the val
    return dd


###### input 1
# d1= {'address': {"city": "Delhi", "pincode": "11111", "country": "India"},
#     'personal_info': {'first_name': "Suraj", 'last_name': "Saini"}
#     }
# d2= {'address': {"pincode": "10001"}}

d1= {
    'personal_info': {'first_name': "Suraj", 'last_name': "Saini"},'address': {"city": "Delhi", "pincode": "11111", "country": "India"}
    }
d2= {'address': {"pincode": "10001"},'personal_info':{'first_name': "Sai"}}

###### input 2
d3= {'patient_info': {'contact': {'email': "abc@gmail.com", 'phone': 9824627820},
                      'name': "Jonny", "DOB": "19-09-1999"}}
d4= {'patient_info': {'contact': {'email': "xyz@yahoo.com"},
                      }}

update_dic= recurse_dict(d1, d2)
print(update_dic)

'''  Pincode has changed
output 1
{'address': {'city': 'Delhi', 'pincode': '10001', 'country': 'India'}, 
'personal_info': {'first_name': 'Suraj', 'last_name': 'Saini'}}
'''

update_dic= recurse_dict(d3, d4)
print(update_dic)

'''   Email has changed
output 2
{'patient_info': {'contact': {'email': 'xyz@yahoo.com', 'phone': 9824627820}, 
'name': 'Jonny', 'DOB': '19-09-1999'}}
'''

#################################

# print first n prime no., update the function
def prime(num):
    for i in range(2,num//2+1):
        if num% i==0:
            return False
    return True


n= int(input('enter num.:'))
count= 0
num= 2
while count!=n:
    if prime(num):
        print('prime', num)
        count+=1
    num+=1

