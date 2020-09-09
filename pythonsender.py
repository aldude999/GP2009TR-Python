from bitarray import bitarray
import sys
import serial

data_byte_array = bitarray(7)

device = sys.argv[8]

start_char = chr(25)
end_char = chr(24)

msg = sys.argv[3]
msgBytes = msg.encode('ascii')
msg_bit_array = bitarray()
msg_bit_array.frombytes(msgBytes)

addr = sys.argv[1]
s0 = bytes(start_char.encode())
s1 = 'R'.encode('ascii')
addr_bit_array = bytearray(7)
addr_bit_array = addr.encode('ascii')
data_byte_array.append(addr_bit_array)

polarit = sys.argv[5]

if polarit == 'N':
 data_byte_array[7] = 0
elif polarit == 'I':
 data_byte_array[7] = 1
else:
 print("Command is: testsend ADDRESS TONE MSG RATE polarit ALPHA/NUM PREAMBLE DEVICE")
 exit()
 
rate = sys.argv[4]

if rate == '512':
 data_byte_array[5] = 0
 data_byte_array[6] = 0
elif rate == '1200':
 data_byte_array[5] = 0
 data_byte_array[6] = 1
elif rate == '2400':
 data_byte_array[5] = 1
 data_byte_array[6] = 0
else:
 print("Command is: testsend ADDRESS TONE MSG RATE polarit ALPHA/NUM PREAMBLE DEVICE")
 exit()

alpha_num = sys.argv[6]

if alpha_num == 'N':
 data_byte_array[4] = 0
elif alpha_num == 'A':
 data_byte_array[4] = 1
 
tone = sys.argv[2]
if tone == 'A':
 data_byte_array[2] = 0
 data_byte_array[3] = 0
elif tone == 'B':
 data_byte_array[2] = 0
 data_byte_array[3] = 1
elif tone == 'C':
 data_byte_array[2] = 1
 data_byte_array[3] = 0
elif tone == 'D':
 data_byte_array[2] = 1
 data_byte_array[3] = 1
else:
 print("Command is: testsend ADDRESS TONE MSG RATE polarit ALPHA/NUM PREAMBLE DEVICE")
 exit()
 
preamble = sys.argv[7]

data_byte_array[1] = 0
data_byte_array[0] = 1

s3 = msgBytes
s4 = bytes(end_char.encode())

fullmessage = s0 + s1 + addr_bit_array + data_byte_array.tobytes() + s3 + s4
 
ser = serial.Serial(device)

ser.write(fullmessage)

print(fullmessage)

