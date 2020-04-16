/*
Erica Umlor Wire Following Sensor Holder for MSE4777

Created: 04/16/2020
Description: This is for my GrowBot project
for senior design. This is the bot end to the wire 
following sensor holders. This end connects to the 
frame of our robot. Don't try to edit this code.
Most of it is not parametric, and it should fit just
fine with this this project. 
*/

botEnd();

// values
holeL = 15;    // length of pin hole
holeR = 2;     // pin hole radius
brace = 4;     // width 
w = 10;        // height and length

module botEnd() {   
    translate([0,40,0]) {
      rotate([0,270,0]) {
        difference() {
          // bottom bracket
          translate([-3,-brace/2-4,0])
          cube([w+6,w+brace+8,w*2]);
    
          // bottom hole
          translate([w/2,-(holeL-10)/2-5,w/2])
          rotate([-90,0,0])
          cylinder(holeL+10,holeR,holeR);
       
          // bracket cutout
          translate([-4,-0.5,0])
          cube([w+8,w+1,w]);
        
          // middle hole
          translate([brace+1,w/2,0])
          cylinder(holeL*2,3-.5,3-.5);
        
          translate([brace+1,w/2,-3])
          cylinder(holeL+3,3+1.2,3+1.2);
        }
      }
    }
}

