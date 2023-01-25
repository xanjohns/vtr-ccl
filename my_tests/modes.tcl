################## model info #########################

# name of model
pre-add_25x18

# input ports
A B D

# output ports
P

# combinational sync? name of port/n (for no)
P



################ mode info ########################

# name of mode
pre-add_25x18

# name of pb or s for same
s

# name of parent PB
DSP48E1


# Now give a list of the input ports, their size,
# and the name of the top PB port they connect to.
# s signals the end of the Iports.
A 30 A
B 18 B
D 25 D
s


# same for the Oports
P 48 P
s



# 1) Fixed point Arithmetic:

#    - 18 x18 independent
#    - 18x19 independent
#    - 2 18x18
#    - 2 18x19
#    - one 27x27 multiplier

# ^^ This is for intel FYI