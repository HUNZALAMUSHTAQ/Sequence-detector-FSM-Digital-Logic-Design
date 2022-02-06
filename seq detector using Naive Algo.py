#Pattern Matching Algorithm 
#Naive Algorithm
#By Assuming that the input data is Stored in Register and it's each bit is passed one by one to D -flipflop and when code is detected light will brighten up
# So Bassically it was Hardware Model using differend IC's tried Code it using Algorithm well it will be an version on the Verilog 
# All design and Problem statement is Mentioned pdf and Electronic Workbench (ewb)
# Will be updating Verilog part soon 
# Bit Detector Hardware
# well Hardware part is more Efficient as its working bit logic

def detect(pat, input_data):
    M = len(pat)
    N = len(input_data)
 
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
        k=0
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (input_data[i + j] != pat[j]):
                break
            j += 1
     
 
 
        if (j == M):
            print("Pattern",pat," found at --> ", i,"'th Input")
detect("0110","00110110001101")
detect("1101","00110110001101")
