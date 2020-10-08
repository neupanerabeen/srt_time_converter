#!
import os
import re
import datetime
from dateutil import parser
import sys



def usage():
	print(
		'''
			python runner.py input_file destination_path lag
				input_file:SRT file to add/substract time
				destination_path: non-existant file path to write the processed src file
				lag: seconds to add/substract
		'''
	)


try:
	fileName = sys.argv[0]
	dest_fileName = sys.argv[1]
	time_to_add = sys.argv[2]
except Exception as e:
	usage()
	exit()

# fileName="/home/rabeen/personal/tor/tor-browser_en-US/Browser/Desktop/Rescue Dawn (2006)/Rescue.Dawn.2006.720p.BluRay.x264.YIFY.srt"
# dest_fileName="/home/rabeen/personal/tor/tor-browser_en-US/Browser/Desktop/Rescue Dawn (2006)/New_Rescue.Dawn.2006.720p.BluRay.x264.YIFY.srt"
# time_to_add=11

pattern_to_replace=r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]*.*[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]*'

def calculate(line):
	_t = re.match(pattern_to_replace, line)
	if _t ==None:
		return line
	_line = _t.group()
	[start_ts, end_ts] = _line.split("-->")
	_sts = parser.parse(start_ts.strip()) + datetime.timedelta(0,time_to_add)
	_ets = parser.parse(end_ts.strip()) + datetime.timedelta(0,time_to_add)
	_sts = _sts.strftime('%H:%M:%S,%f')
	_ets = _ets.strftime('%H:%M:%S,%f')
	line = line.replace(start_ts, _sts).replace(end_ts, _ets).replace("000", "").replace("-->", " --> ")
	print(line)
	return line

allLines= ""
with open(fileName, 'rb') as f:
	allLines = f.read()

allLines= allLines.decode('ISO-8859-1').split("\n")
allLines = [calculate(line) for line in allLines]
with open(dest_fileName, 'wb') as file:
	file.write(bytes("\n".join(allLines), encoding='ISO-8859-1'))
