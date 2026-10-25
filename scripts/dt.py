#!/usr/bin/env python3
########################################################################
# FILE: dt.py
#
# PURPOSE: Print a series of month/day: lines to start a UTI log month
#
# USAGE: uti_dt month last_day
#
# ARGUMENTS:
#   month       Month number. Default is current month.
#   last_day    Last day number. Default is 31.
#
# OUTPUT:
#   A series of m/d: lines separated by blank lines. 
#
# MODIFICATION HISTORY:
#   2026/09/02, SK Hushing III. Original issue for darwin OS.
########################################################################
import sys

#----[ How Python processes arguments ]----#
# sys.argv is a list containing the script name and arguments
# sys.argv[0] is the script name itself (like $0 in Perl)
# sys.argv[1] is the first argument, sys.argv[2] is the second, etc.

#----[ Verify at least two arguments specified ]----#
if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <month_num> <total_days>")
    sys.exit(1)

#----[ Get month and days arguments ]----#
month = sys.argv[1]
days = int(sys.argv[2])

#----[ print the desired output ]----#
output = '\n\n'.join(f"{month}/{day}:" for day in range(1, days + 1))
print(output)
