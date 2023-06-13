f = open("job_history.txt")
s = open("job_history_2.txt", "w")
for l in f:
    if "TO_DATE" in l:
        a = l.replace("      , TO_DATE('", "").replace("', 'dd-MM-yyyy')\n", "").split("-")
        b = "-".join((a[2],a[1],a[0]))
        s.writelines("      , '"+b+"'\n")
    else:
        s.writelines(l)
    