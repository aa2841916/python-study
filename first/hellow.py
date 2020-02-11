# import os
#
# print(os.path.abspath('hellow.py'))
#
# # st = open("yellow.txt","w")
# # st.write("hellow world")
# # st.close()
# my_list = []
# with open('yellow.txt', 'w') as t:
#     t.write('yellow1')
#
# with open('yellow.txt','r') as f:
#     my_list.append(f.read())
#
# print(my_list)


# import csv
# with open('st.csv','w') as f:
#     w = csv.writer(f,delimiter = ',')
#     w.writerow(['one','two','three'])
#     w.writerow(['four','five','six'])
# with open('st.csv','r') as t:
#     r = csv.reader(t,delimiter = ',')
#     for row in r:
#         print(','.join(row))

# with open("yellow_nice.txt", 'r') as f:
#     w = f.read()
#
# print(w)

# str = ['yes']
# str_1 = input('please enter yes or no:')
# if str_1 in str:
#     yes = 'niubi'
# else:
#     yes = 'sb'
# with open('txte.txt','w') as d:
#     d.write(yes)
# # with open('txte.txt','r') as f:
# #     print(f.read())



import csv
str_c = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"],
       ["Training Day", "Man on Fire", "Flight"]]

n = 0

with open('stt.csv','w') as f:
    w = csv.writer(f,delimiter = ',')
    while n < len(str_c):
        w.writerow(str_c[n])
        n += 1







