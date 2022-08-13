import re
outputFile = open('parsed_data.csv', 'w')
start = False
wires = ""
time = 0
numElements = 0

# use a map where the combination is the key and the time is value

with open('/home/chem3000/time_data.txt') as inputFile:
    for line in inputFile:
        if "These" in line:
            if start: # this will skip the last set :(
                outputFile.write(wires + ": " + str(time/numElements) + "\n")
            rawWire = next(inputFile)
            
            # a switch would be a pain since there are so many diffrent combinations 
            # (VL1 HL1, V/H L2, V/H L4, V/H L6, V/H L12, V/H L18, all semi-cardinal)
            
            # the way to go is to parse directly from the name
            # length 1s: (N|E|W|S)(R|L)(\d)
            # other lengths: (NN|EE|WW|SS|NE|NW|SE|SW)(\d)
            # I think we should keep NN SS for now (dont combine to vertical) just until we can make sure there aren't any unforeseen side affects
            wires = next(inputFile)
            start = False
            time = 0
            numElements = 0
        elif "timing" in line:
            start = True
        elif start and re.match("(FAST_MAX|FAST_MIN|SLOW_MAX|SLOW_MIN)(.*)", line):
            time += int(re.findall("\d+", line)[0])
            numElements += 1

outputFile.close
        # 1) parse to "These wires:"
        # 2) get wire names on next line
        # 3) convert wire names to a more readable format and save. 
        # 4) parse to next line "Have the following timing info:"
        # 5) collect ALL timing info and average (for now)
        # 6) continue collection until the next double newline (or until (1))