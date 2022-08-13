from pydoc import doc
import sys

def main():
    print("Model info:\n")
    modelName = input("Enter the name of the model: ")
    Iports = input("Enter all input ports separated by spaces: ")
    Oports = input("Enter all output ports separated by spaces: ")
    # Oclk = input("Are Oports tied to a clk? n/name")
    combSync = input("Computational sync between input and output? n/port: ")

    print("Mode info\n")
    modeName = input("Enter the name of the mode: ")
    pbname = input("Enter pb name or type s for same: ")
    topPB = input("enter the name of the parent PB: ")
    # topIport = input("Top PB input ports: ")
    # topOport = input("Top PB output ports: ")
    print("\nNow enter each input port of the new pb_tpe\n\
    and which top level input port it connects to.\n\
    When you are ready to stop type s")

    IList = []
    IList.append(input("Enter Iport followed by number followed by top port "))

    while(IList[len(IList) - 1] != "s" and IList[len(IList) - 1] != "S"):
        IList.append(input("Enter Iport followed by number followed by top port "))
    
    IList.pop() # remove the last empty entry

    print("\nNow do the same for the outputs")

    OList = []
    OList.append(input("Enter Oport followed by number followed by top port "))

    while(OList[len(OList) - 1] != "s" and OList[len(OList) - 1] != "S"):
        OList.append(input("Enter Oport followed by number followed by top port "))
    
    OList.pop() # remove the last empty entry

    print("Here is the mode and model info:\n")

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







if __name__ == "__main__":
    main()