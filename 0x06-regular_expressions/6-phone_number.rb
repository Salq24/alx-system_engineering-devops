#!/usr/bin/env ruby
#must match a 10 digit phone num

puts ARGV[0].scan(/^\d{10}/).join
