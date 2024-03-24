import random  
list = [1,2,5] 
list.append(random.randrange(len(list))) 
print("The original list : " + str(list)) 
list.pop(random.randrange(len(list))) 
print("List after removal of random number : " + str(list)) 
