//A simple cricuit which blinks an LED on and off periodically
module simpleOR(
    input[1:0] in,  //Input
    output o_led);  //Output to LED

    //Combinational logic 
    //
    //Drives o_led high if in is high
    always @(*) begin
        if (in[1] | in[0]) begin
            o_led <= 1'b1;
        end else begin
            o_led <= 1'b0;
        end
    end

endmodule
