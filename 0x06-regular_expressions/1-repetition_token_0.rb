#!/usr/bin/env ruby
# This script matches hbtn.
# It finds and matches hbtn, t must be from 2 upto 5 number of times.

puts ARGV[0].scan(/hbt{2,5}n/).join
