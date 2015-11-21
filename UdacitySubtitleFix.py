# Copyright (C) 2015 AungThiha
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fnmatch
import os
import sys
import re

patched = 'is patched'
pat = r'(\d:\d\d:\d\d\.\d\d\d),(\d:\d\d:\d\d\.\d\d\d)'
repl = r'\1 --> \2'
addr = '''\n%s file/files in total.\n
Aung Thiha
mr.aungthiha@gmail.com
https://www.twitter.com/AungThiha3
https://www.linkedin.com/in/aung-thiha-a4990b106\n
Press Enter/Return to exit.'''

def main(filedir):
	print ''
	total = 0
	for root, dirnames, filenames in os.walk(filedir):
	    for filename in fnmatch.filter(filenames, '*.srt'):
	    	abs_path = os.path.join(root, filename)
	    	f = open(abs_path, 'r')
	    	text = re.sub(pat,repl, f.read())
	    	f.close()
	    	f = open(abs_path, 'w')
	    	f.write(text)
	    	f.close()
	        print filename, patched
	        total += 1
	print addr % total
	raw_input()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		main('.')
