# GP2009TR-Python
Python script that allows you to transmit messages with a GP2009TR from any platform.
## Usage

python .\testsend.py 0000100 C 'Testing 123' 1200 N A 1 COM3

.\testsend.py [Pager ID, should be 7 digits] [tone (A/B/C/D)] [message(Up to 300 characters allegedly)] [baud(512/1200/2400), not working right] [Normal or Invert (N/I), May not be working right] [Alpha/Numeric (A/N)] [Long Preamble (Not working yet, but 1/0] [Serial device, Windows: COM#, Linux '/dev/ttyUSB#']

## Notes
I still have some work to go, something is acting strange on the bitarray, might be endianness.
