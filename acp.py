def reverse_bits(num):
    # Find the bit length of the number
    bit_length = num.bit_length()

    reversed_num = 0
    for i in range(bit_length):
        # Shift left to make room for the next bit
        reversed_num <<= 1
        # Get the least significant bit of num and add to reversed_num
        reversed_num |= (num & 1)
        # Shift num right to process the next bit
        num >>= 1

    return reversed_num

# Input from user
original = int(input("Enter your original number: "))
reversed_number = reverse_bits(original)

# Print in both decimal and binary for clarity
print(f"Reversed Number: {reversed_number} ({bin(reversed_number)[2:]})")