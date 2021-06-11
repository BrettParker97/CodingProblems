#finished in 22m
def swap_bits(num):
    for x in range(32):
        if x % 2 == 0:
            #mask with 1 only at bit we want
            mask1 = pow(2, x)
            mask2 = pow(2, x + 1)
            
            #push mask with num to get single bits
            bit1 = num and mask1
            bit2 = num and mask2
            
            #if theyre the same do nothing
            if bit1 << 1 == bit2:
                continue
            
            #if theyre different
            if bit1 == 0:
                #change bit 2
                mask2 = 0xffffffff ^ bit2
                num = num and mask2
                
                #change bit 1
                mask1 = bit2 >> 1
                num = num or mask1
            else:
                #change bit 1
                mask1 = 0xffffffff ^ bit1
                num = num and mask1
                
                #change bit 2
                mask2 = bit1 << 1
                num = num or mask2
    return num
    
print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101