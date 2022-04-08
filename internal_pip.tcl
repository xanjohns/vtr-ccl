set diag_pips [get_pips -of_object [get_selected_objects] -regexp -filter {NAME =~ ".*LOGIC_OUTS_L([0-9]+)->>IMUX.*"}] 
set internals [list]
foreach test_pip $diag_pips {
  regexp {LOGIC_OUT.*([0-9]+)->>} $test_pip logic_out_num
  regexp {[0-9]+} $logic_out_num logic_out_num
  select_objects $test_pip
  regexp {X([0-9]+)Y([0-9]+)} $test_pip tile_num
  regexp {([0-9]+)$} $test_pip matched
  set tile [get_tiles -regexp -filter "NAME =~ CLB.*$tile_num"]
  set crossbar_output_pip [get_pips -of_object $tile -regexp -filter "NAME =~ .*LOGIC_OUT.*$logic_out_num"]
  regexp {/.*\->} $crossbar_output_pip input
  set crossbar_pip [get_pips -of_object $tile -regexp -filter "NAME =~ .*$match.*IMUX$matched.*"]
  regexp {\->.*} $crossbar_pip output
  lappend internals "$tile: $input $output\n"
}

puts [lsort -dictionary $internals]