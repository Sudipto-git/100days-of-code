# old_price = {'milk': 2,'bread': 4,'cheese': 5}
# print("Old Price: ",old_price)
# doubled_price = {old_price: old_price*2 for(old_price,old_price) in old_price.items()}  
# print("doubled_price: ",doubled_price) 

# #for(index,row) in student_data.iterrows():
# #print(row.score)


# Generate squares lazily

gen = (x**2 for x in range(1000))
# Access via next() or iteration
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
