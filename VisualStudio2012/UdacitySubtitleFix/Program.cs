/*
 * Copyright (C) 2015 AungThiha
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace UdacitySubtitleFix
{
    class Program
    {
        static void Main(string[] args)
        {
            string patched = " is patched";
            string pattern = @"(\d:\d\d:\d\d\.\d\d\d),(\d:\d\d:\d\d\.\d\d\d)";
            string text = "";
            string[] files = Directory.GetFiles(".", "*.srt");
            foreach (string file in files)
            {
                text = Regex.Replace(File.ReadAllText(file), pattern, "$1 --> $2");
                File.WriteAllText(file, text);
                Console.WriteLine(file.Remove(0,2) + patched);
            }
            Console.WriteLine("\n{0} file/files in total.\n\nAung Thiha mr.aungthiha@gmail.com twitter.com/AungThiha3 Myanmar(Burma)\n\nPress Any Key to exit.", files.Count());
            Console.ReadKey();  
        }
    }
}
