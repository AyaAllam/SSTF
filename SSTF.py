# Python program for SSTF disk scheduling algorithm

# Calculates difference of each
# track number with the head position
def calculateDifference(queue, head, diff):
	for i in range(len(diff)):
		diff[i][0] = abs(queue[i] - head)
	
# find unaccessed track which is
# at minimum distance from head
def findMin(diff):

	index = -1
	minimum = 999999999

	for i in range(len(diff)):
		if (not diff[i][1] and
				minimum > diff[i][0]):
			minimum = diff[i][0]
			index = i
	return index
	
def shortestSeekTimeFirst(request, size, head):			
		
        l = size
        diff = [0] * l
		
		# initialize array
        for i in range(l):
            diff[i] = [0, 0]
		
		# count total number of seek operation	
        seek_count = 0
		
		# stores sequence in which disk
		# access is done
        seek_sequence = [0] * (l + 1)
		
        for i in range(l):
            seek_sequence[i] = head
            calculateDifference(request, head, diff)
            index = findMin(diff)
			
            diff[index][1] = True
			
			# increase the total count
            seek_count += diff[index][0]
			
			# accessed track is now new head
            head = request[index]
	
		# for last accessed track
        seek_sequence[len(seek_sequence) - 1] = head
		
        print("Total number of seek tracks =",
									seek_count)
														
        print("Seek Sequence : ")
		
		# print the sequence
        for i in range(l + 1):
            print(seek_sequence[i])
            
        # calculate the average    
        average = seek_count / size;
        print("Average number of tracks travelled = ", average)
	
# Driver code
if __name__ =="__main__":
	
    # to get the initial head position
    head=int(input("Initial head position: "))
    
    # to get the size of the array
    size= int(input("Number of pathes: "))
    
	# request array
    print("Sequence: ")
    arr= []
    for i in range(size):
        arr.append(int(input()))
        
    shortestSeekTimeFirst(arr, size, head)

