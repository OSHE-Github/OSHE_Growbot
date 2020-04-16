/*
Erica Umlor Wire Following Sensor Holder for MSE4777

Created: 04/16/2020
Description: This is for my GrowBot project
for senior design. This is the ppin that connects
each of the parts. Don't try to edit this code.
Most of it is not parametric, and it should fit just
fine with this this project. 
*/

pin(); 

// values
holeL = 15;    // length of pin hole
holeR = 2;     // pin hole radius
pR = holeR-.05; 

module pin() {
  union(){
    cylinder(2,holeR+2,holeR+2);
    cylinder(holeL+7,pR,pR);
  }
}
