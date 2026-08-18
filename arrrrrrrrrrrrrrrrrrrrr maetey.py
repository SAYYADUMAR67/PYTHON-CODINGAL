import array as arr
array_num = arr.array('i',[1,3,5,3,7,9,3])
print("orignal array:"+str(array_num))
print("number of occurances of the number 3 :"+ str(array_num.count(3)))

array_num.reverse()
print("the reverse order of the items")
print(str(array_num))