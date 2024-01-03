#!/usr/bin/env ruby
# Author Bereket Dereje Mekonnen
# This script matches match a 10 digit phone number.

puts ARGV[0].scan(/^\d{10,10}$/).join
