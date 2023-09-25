

# dbquery = session.query
#     (tableC.id.label('c.id),
#       tablec.data
#       tableb.id.label('b_id'),
#       tableb.data
#       table.id.label('a_id'),
#       tableA.data
# ). join( tableB, tableC.b.id  = tableB.id 
# ).join ( tableA, tableB.a.id == tableA.id))

# dbquery.all()

# # 

# list = [{'name': 'pan', 'price': 40}, {'name': 'glass', 'price':60}, {'name': 'lass', 'price': 100}, {'name': 'gla', 'price': 10}]
 
 
# sorteddata = sorted( list, key =lambda y: y['price'])
# print(sorteddata)


# for(int i = 1 ; i <= 100 ; i*2){

#     for(int j = 1 ; j <= n ; j++){

# print(i + j);

# }

# }

# data = [1,5,40,96,52,93,100,120,9]


# max_number = data[0]
# for i in data:
#     if i> max_number:
#         second_max = max_number 
#         max_number = i

        
# print(second_max)
# sorteddata = data[-5:]

# # write to a program to find the difference between sum of elements till ith index and sum of elements after ith index
# # k=5

# index = 5 

# sum_before_index = sum(data[:index])
# sum_after_index = sum(data[index +1:])
# print(sum_after_index)
# print(sum_before_index)
# result = sum_after_index - sum_before_index

# print("result = ", result)


#write a program to find the 1st non-repeating element in the list [1,2,3,1,2,4,5,5,6,1,2]

# list = [1,2,3,1,2,4,5,5,6,1,2]

# element_count = {}


# for element in list:
#     if element in element_count:
#         element_count[element] +=1
#     else:
#         element_count[element] = 1


# for element in list:
#     if element_count[element] == 1:
#         print(element)
#         break
    
    

# def myDecorator(hello):
#     def wrapper():
#         print("myDecorator function called")
#         hello()
#         print("myDecorator function called")
        
#     return wrapper
    
    
# @myDecorator
# def hello():
#     print("hello world")
    
    
 

a = [2, 3]
b = a
b.append(5)
# print(id(a))
print(a,b)
# print(id(b))