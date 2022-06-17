# Needed features in VTR to represent Xilinx architecture description

#### Proposed Behaviour
The following is a list of functionality that would need to be supported in VTR in order to obtain an approximate capture of the xilinx architecture:

- [x] Support for different distributions of wires in the vertical/horizontal.
    - Most of the functionality for this was brought in with PR #1883 although porting the functionality to work with custom SB's remains as an action item.

- [x] Support for non-uniform chanel widths 
    - As above, PR #1883 has allowed for this functionality but work still needs to be done with custom SBs.

- [] Support for the two points above for custom SB.

- [] Support for different shaped wires (diagonals/T shaped in particular).
    - PR #2067 will make the necessary changes to allow for this feature although diagonal wires will need to be modeled through custom SB.

- [] In the xilinx arch switch blocks and connection blocks are combined into one (improving space and routablitiy). The island style FPGA supported by VTR currently separates the two. 

- [] Support for tile layouts beyond that currently supported by VTR.
    - Following the island style, VTR currently has a pattern of CB, Logic, CB, ...
    - Xilinx has a pattern of SB/CB, SB/CB, Logic, Logic, SB/CB, SB/CB, ... (see images in following post).

- [] Xilinx has sets of wires that leave a connection block, enter an SB, and then bounce back into the same connection block (termed as a bounce pip in Xilinx). Although this is not technically supported by VTR the same affect can be modeled using internal crossbars.

- [] Support for both bi-directional and uni-directional segments in the same arch. VTR currently only supports one or the other. This item is not too important since only the longest wire segments in the xilinx arch are bi-directional (L12 and L18).

