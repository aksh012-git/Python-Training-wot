# Slice list into 3 equal chunks and reverse each chunk
# Sample:  [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Result: [[8, 45, 11], [12, 14, 23], [89, 45, 78]]

list_num =  [11, 45, 8, 23, 14, 12, 78, 45, 89]
number_of_chunks = 3
chunksCounter = 0
final_array = []

for i in range(len(list_num)):
    chunks = list_num[int(len(list_num)/number_of_chunks*chunksCounter) : int(len(list_num)/number_of_chunks*(chunksCounter+1))]
    chunks.reverse()
    final_array.append(chunks)
    chunksCounter += 1
    if  chunksCounter == number_of_chunks:
        break
        
print(final_array)






# q1 = list_num[0:int(len(list_num)/3)]
# q1.reverse()
# q2 = list_num[int(len(list_num)/3):int(len(list_num)/3)*2]
# q2.reverse()
# q3 = list_num[int(len(list_num)/3)*2:len(list_num)]
# q3.reverse()
# print(q1,q2,q3)