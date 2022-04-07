# Get all signal nets
set nets [get_nets -filter {TYPE == SIGNAL}]
set final_nets [list]
set final_list [list]
foreach net $nets {
  set output_pin [get_pins -of $net -filter {DIRECTION == OUT}]
  if {$output_pin != ""} {
    set ref_name [get_property REF_NAME $output_pin]
  }
  set lut "LUT"
  set is_lut [expr {[string first $lut $ref_name] != -1}]
  if {$is_lut} {
    set output_pin ""
  }
  if {$output_pin != ""} {
    set output_site [get_property LOC [get_property PARENT_CELL $output_pin]]
    set input_pins [get_pins -of $net -filter {DIRECTION == IN}]
    if {$input_pins != "" && $output_site != ""} {
      foreach pin $input_pins {
        set input_site [get_property LOC [get_property PARENT_CELL $pin]]
        # Add to list if input pin site and output pin site are equal
        if {$input_site == $output_site} {
          lappend final_nets $net
          set input_BEL [get_property BEL [get_property PARENT_CELL $pin]]
          set output_BEL [get_property BEL [get_property PARENT_CELL $output_pin]]
          set temp_string "$input_site:$input_BEL to $output_BEL \n"
          lappend final_list $temp_string
        }
      } 
    }
  }
}
#puts [lsort -dictionary $final_list]
puts [lsort -dictionary $final_nets]

select_objects $final_nets
