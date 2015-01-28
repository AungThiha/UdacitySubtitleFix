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

patched = ' is patched'
pattern = /(\d:\d\d:\d\d\.\d\d\d),(\d:\d\d:\d\d\.\d\d\d)/
text = ''
files = Dir["*.srt"]
files.each do |file|
  text = File.read(file)
  text = text.gsub(pattern, '\1 --> \2')
  File.write(file, text)
  puts file + patched
end
puts "\n#{files.length} file/files in total.\n\nAung Thiha mr.aungthiha@gmail.com twitter.com/AungThiha3 Myanmar(Burma)\n\nPress Any Key to exit."
gets
