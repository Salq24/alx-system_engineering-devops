#!/usr/bin/env ruby
#Textme log showing sender, receiver, flags

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
