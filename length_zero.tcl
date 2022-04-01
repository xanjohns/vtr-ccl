# Get all signal nets
set nets [get_nets -filter {TYPE == SIGNAL}]
set final_list [list ""]
foreach net $nets {
  set output_pin [get_pins -of $net -filter {DIRECTION == OUT}]
  if {$output_pin != ""} {
    set output_site [get_property LOC [get_property PARENT_CELL $output_pin]]
    set input_pins [get_pins -of $net -filter {DIRECTION == IN}]
    if {$input_pins != "" && $output_site != ""} {
      foreach pin $input_pins {
        set input_site [get_property LOC [get_property PARENT_CELL $pin]]
        # Add to list if input pin site and output pin site are equal
        if {$input_site == $output_site} {
          set input_BEL [get_property BEL [get_property PARENT_CELL $pin]]
          set output_BEL [get_property BEL [get_property PARENT_CELL $output_pin]]
          set temp_string "$input_site:$input_BEL to $output_BEL \n"
          lappend final_list $temp_string
        }
      } 
    }
  }
}
puts [lsort -dictionary $final_list]
