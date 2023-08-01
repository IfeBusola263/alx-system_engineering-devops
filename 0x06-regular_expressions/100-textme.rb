#!/usr/bin/env ruby

# puts ARGV[0].scan(/\[from:(.*?)\]\[to:(.*?)\]\[flags:(.*?)\]/).join(',')

input_string = ARGV[0]

from_value = input_string.scan(/\[from:([^]]*)\]/).flatten.first
to_value = input_string.scan(/\[to:([^]]*)\]/).flatten.first
flags_value = input_string.scan(/\[flags:([^]]*)\]/).flatten.first

result = [from_value, to_value, flags_value].join(',')
puts result
