# Gets a list of all 0 length wires wires in a INT block
set diag_pips [get_pips -of_object [get_selected_objects] -regexp -filter {NAME =~ ".*LOGIC_OUTS_L([0-9]+)->>IMUX.*"}] 
# Final return list
set internals [list]
foreach test_pip $diag_pips {
  # Select pin number of FF output (INT input)
  regexp {LOGIC_OUT.*([0-9]+)->>} $test_pip logic_out_num
  regexp {[0-9]+} $logic_out_num logic_out_num
  select_objects $test_pip
  # Get tile number that covers the PIPs
  regexp {X([0-9]+)Y([0-9]+)} $test_pip tile_num
  # Select pin number of LUT input (INT output)
  regexp {([0-9]+)$} $test_pip matched
  set tile [get_tiles -regexp -filter "NAME =~ CLB.*$tile_num"]
  # The rest is for getting the actual FF, LUTs that we want to see, instead of just the PIPs
  set crossbar_output_pip [get_pips -of_object $tile -regexp -filter "NAME =~ .*LOGIC_OUT.*$logic_out_num"]
  regexp {/.*\->} $crossbar_output_pip input
  set crossbar_pip [get_pips -of_object $tile -regexp -filter "NAME =~ .*$match.*IMUX$matched.*"]
  regexp {\->.*} $crossbar_pip output
  lappend internals "$tile: $input $output\n"
}

# Sort and print output
puts [lsort -dictionary $internals]