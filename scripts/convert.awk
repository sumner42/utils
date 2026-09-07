# 1. Match the date line (e.g., "8/24:"). 
# Strip the trailing colon and append the current year (2026).
/^[0-9]+\/[0-9]+:$/ {
    gsub(/:$/, "", $1)
    current_date = $1 "/2026"
    next
}

# 2. Match the data rows (lines starting with a timestamp like "8:12" or "11:17")
/^[0-9]+:[0-9]+/ {
    # Print the saved date, the time, and the am/pm modifier
    printf "%s %s %s", current_date, $1, $2
    
    # Print the 4 columns separated by tabs
    for (i = 3; i <= 6; i++) {
        printf "\t%s", $i
    }
    
    # If there is a trailing comment, print it out as well
    if (NF > 6) {
        printf "\t"
        for (i = 7; i <= NF; i++) {
            printf "%s%s", $i, (i == NF ? "" : " ")
        }
    }
    print "" # Print a newline
}
