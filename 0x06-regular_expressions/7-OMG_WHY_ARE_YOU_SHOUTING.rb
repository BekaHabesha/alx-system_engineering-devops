#!/usr/bin/env ruby
# Author Bereket Dereje Mekonnen
# This script only matching: capital letters.

puts ARGV[0].scan(/[A-Z]*/).join
