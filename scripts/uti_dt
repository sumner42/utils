#!/usr/bin/perl
sub usage() { print STDERR
'########################################################################
# FILE: uti_dt
#
# PURPOSE: Print a series of month/day: lines to start a UTI log month
#
# USAGE: uti_dt [month] [last_day] [first_day]
#
# ARGUMENTS:
#   month       Month number. Default is current month.
#   last_day    Last day number. Default is 31.
#   first_day   First day number. Default is 1.
#
# MODIFICATION HISTORY:
#   2026/09/02, SK Hushing III. Original issue for darwin OS.
#   2026/09/02, SKH. Added optional first_day argument.
########################################################################
'; exit }

use strict;
use warnings;

#----[ Print usage if requested ]----#
usage() if scalar(@ARGV) > 0 && $ARGV[0] eq "help";

#----[ Use months, first_day, last_day passed or set defaults ]----#
my $month     = $ARGV[0] // 0;
my $last_day  = $ARGV[1] // 31;
my $first_day = $ARGV[2] // 1;

#----[ Enforce reasonable values ]----#
$month = ((localtime)[4] + 1) if ($month < 1 || $month > 12);
$last_day = 31 if $last_day > 31;
$first_day = 1 if $first_day < 1 || $first_day > 31;
$last_day = $first_day if $last_day < $first_day;

#----[ Print specified month/day lines ]----#
for (my $day = $first_day; $day <= $last_day; $day++) {
    print "$month/$day:\n\n";
}
