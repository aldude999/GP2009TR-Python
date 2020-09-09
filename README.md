# GP2009TR-Python
Python script that allows you to transmit messages with a GP2009TR from any platform.
## Usage

python .\testsend.py 0000100 C 'Testing 123' 1200 N A 1 COM3

.\testsend.py [Pager ID, should be 7 digits] [tone] [message] [baud] [Normal or Invert (N/I)] [Alpha/Numeric (A/N)] [Long Preamble (Not working yet, but 1/0] [Serial device, Windows: COM#, Linux '/dev/ttyUSB#']

## Notes
I still have some work to go, something is acting strange on the bitarray, might be endianness.
