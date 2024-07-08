# If there are more than 2 conditions, then we use elif for those extra conditions:

pak = 250

india = int(input("Enter India's score: "))

if (india > pak) :
    print("India won the match")
elif india == pak:
    print("Match tied")
elif india < pak and india >= 0:
    print("India lost match")
else:
    print("invalid score, cannot check")