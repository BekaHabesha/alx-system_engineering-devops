#!/usr/bin/env ruby
# Author Bereket Dereje Mekonnen
# This script matches hbtn.
# It finds and matches hbtn, hbn, t upto infinity number of times.
# The regex should not contain square brackets.

puts ARGV[0].scan(/hbt*n/).join
