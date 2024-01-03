#!/usr/bin/env ruby
# Author Bereket Dereje Mekonnen
# This script matches hbtn.
# It finds and matches hbtn, t upto infinity number of times.

puts ARGV[0].scan(/hbt+n/).join
