Index_list = [1,2,3,4,5,6,7,8,9,10,11,12]

Name_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

tuple_list = []
a=0
for i in range(12):
    tuple_list.append((Index_list[a],Name_list[a]))
    a=+1
print(tuple_list)