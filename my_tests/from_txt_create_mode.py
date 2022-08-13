# def collectLine(num):


def main():
    with open("/home/chem3000/GitClones/xan-vtr/my_tests/modes.tcl") as file:
        fileLines = file.readlines()

    lineCoolection = []
    for line in fileLines:
        if "#" in line or line == "\n":
            continue
        lineCoolection.append(line)
    
    #collect the info
    modelName = lineCoolection[0].replace("\n", "")
    Iports = lineCoolection[1].replace("\n", "")
    Oports = lineCoolection[2].replace("\n", "")
    combSync = lineCoolection[3].replace("\n", "")

    modeName = lineCoolection[4].replace("\n", "")
    pbname = lineCoolection[5].replace("\n", "")
    topPB = lineCoolection[6].replace("\n", "")

    # get the I list:
    Icount = 7
    IList = []
    while lineCoolection[Icount].strip() != "s":
        IList.append(lineCoolection[Icount].replace("\n", ""))
        Icount += 1

    
    # get the O list
    Ocount = Icount + 1
    OList = []
    while lineCoolection[Ocount].strip() != "s":
        OList.append(lineCoolection[Ocount].replace("\n", ""))
        Ocount += 1

    

    ##############################################
    print("#################### Model ##############################\n")

    print("<model name=\"" + modelName + "\">")
    print("\t<input_ports>")
    for port in Iports.split(" "):
        print("\t\t<port name=\"" + port + "\"", end="")
        if combSync == "n":
            print("/>")
        else:
            print(" combinational_sink_ports=\"" + combSync +"\"" + "/>")
    print("\t</input_ports>\n")


    print("\t<output_ports>")
    for port in Oports.split(" "):
        print("\t\t<port name=\"" + port + "\"", end="")
        print("/>")

    print("\t</output_ports>")

    print("</model>\n")


    print("#################### Mode ##############################\n")
    print("<mode name=" + "\"" + modeName + "\">")
    print("\t<pb_type name=\"", end="")
    if pbname == "s":
        pbname = modeName
        print(modeName + "\" blif_model=\".subckt " + modelName + "\" num_pb=\"1\">")
    else:
        print(pbname + "\">")
    # do all the inputs with the number of pins they have
    for i in IList:
        print("\t\t<input name=\"" + i.split(" ")[0]  + "\" " + "num_pins=\"" + i.split(" ")[1] + "\"" + "/>")
    
    for o in OList:
        print("\t\t<output name=\"" + o.split(" ")[0]  + "\" " + "num_pins=\"" + o.split(" ")[1] + "\"" + "/>")

    # dont forget dealy constants /////////////////////////////////
    for i in IList:
        if combSync != "n":
            print("\t<delay_constant max=\"2.14e-9\" in_port=\"" + pbname + "." + i.split(" ")[0] + "\" out_port=\"" + pbname + "." + combSync + "\"/>")

    # same for outputs

    print("\t</pb_type>\n")
    # then do intercon and use the top module name
    print("\t<interconnect>")
    for i in IList:
        print("\t\t<direct name=\"" + i.split(" ")[2] + "to"+ i.split(" ")[0] + "\" input=\"" + topPB  + "." + i.split(" ")[2] + "\" output=\"" + pbname + "." + i.split(" ")[0] + "\"/>")
    for o in OList:
        print("\t\t<direct name=\"" + o.split(" ")[0] + "to" + o.split(" ")[2] + "\" input=\"" + pbname + "." + o.split(" ")[0] + "\" output=\"" + topPB  + "." + o.split(" ")[2] + "\"/>")

    print("\t</interconnect>")
    print("</mode>\n")




if __name__=="__main__":
    main()