module simpleOR(
    input[13:0] in,  //Input
    input clk,
    output[7:0] o_led);  //Output to LED

    //Combinational logic 
    //
    //Drives o_led high if in is high
    always @(*) begin
        o_led[0] = in[0] | in[1];
        o_led[1] = in[2] | in[3];
        o_led[2] = in[4] | in[5];
        o_led[3] = in[6] | in[7];
        o_led[4] = in[8] | in[9];
        o_led[5] = in[10] | in[11];
        o_led[6] = in[12] | in[13];
    end

  //  reg register;
  //  always @(posedge clk) begin
  //      if(in[0] & in[1])
  //      register <= in[13];
  //      else 
  //      register <= register;
  //  end

  //  assign o_led[7] = register;

    // use a width factor of at least 40
endmodule