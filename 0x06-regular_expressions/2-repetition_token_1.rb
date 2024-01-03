#!/usr/bin/env ruby
# Author Bereket Dereje Mekonnen
# This script matches hbtn.
# It finds and matches htn, hbtn, hbn.

puts ARGV[0].scan(/hb?t?n/).join
