#define a function
def flow_control (k):
	#define a string based on the value of k
	if(k==0):
		s = "Variable k = %d equals 0." % k
	elif(k==1):
		s = "Variable k = %d equals 0." % k
	else:
		s = "Variable k = %d doesn't equal 0 or 1." % k

	#print the variable
	print(s)

#define a main function
def main():
	
	#declare an integer
	i = 0

	#try flow_control fo 0, 1, 2
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2

#run the program
if __name__ == "__main__":
	main()
#Works