########################################################################
# FILE: Makefile
#
# PURPOSE: Make specifications for C crc
#
# USAGE: make
#
# PARAMETERS:
#   all       Build known targets
#   clean     Remove target program and temporary object files
#
# MODIFICATION HISTORY:
#   2018/02/23 SK Hushing III. Original issue for Ubunto under Windows.
########################################################################
PGM	= crc

all: $(PGM)

$(PGM): $(PGM).c
	cc -o $@ $<
	
clean:
	rm -f $(PGM)
