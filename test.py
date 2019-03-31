file = open("test.cmd","w")
file.write("stepsize 100 \n")
file.write("l vss\n")
file.write("vector c left_right sh2 sh1 sh0 LR X shift_adder\n")
file.write("vector a A7 A6 A5 A4 A3 A2 A1 A0\n")
file.write("vector b B7 B6 B5 B4 B3 B2 B1 B0\n")
file.write("vector result res8 res7 res6 res5 res4 res3 res2 res1 res0\n")
for i in range(0,128,4):
	for j in range(0,256,4):
		for k in range(0,256,4):
			file.write("setvector c 0d"+str(i)+'\n'+"setvector a 0d"+str(j)+'\n'+"setvector b 0d"+str(k)+'\n'+'s'+'\n')
file.write("analyzer c a b result\n")
file.close()
