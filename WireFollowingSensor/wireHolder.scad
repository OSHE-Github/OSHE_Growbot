/*
Erica Umlor Wire Following Sensor Holder for MSE4777

Created: 04/16/2020
Description: This is for my GrowBot project
for senior design. This is the middle part of the 
wire holder. One end connects to the end that connects
to the frame of our robot and the other end connects
to the end that has a slot for the inductor to sit
in. Don't try to edit this code. Most of it is not
parametric, and it should fit just fine with this
this project. 
*/


wireHolder();

// values
h1 = 100;    // length 
holeL = 15;
holeR = 2;
brace = 4;
w = 10;

module wireHolder() {
  rotate([0,90,0]) {
     difference() {
       base();
       holes();
    }
  }
}

module base() {
    union() {
        // main body
        translate([0,0,0])
        cube([w,w,h1]);
        
        // bottom bracket
        translate([0,-brace/2,0])
        cube([w,w+brace,w+brace]);
    }
}

module holes() {
    // top hole
    translate([w/2,0,h1-w/2])
    rotate([-90,0,0])
    cylinder(holeL,holeR,holeR);

    // bottom hole
    translate([w/2,-(holeL-10)/2,w/2])
    rotate([-90,0,0])
    cylinder(holeL,holeR,holeR);
    
    // bracket cutout
    translate([0,-0.5,0])
    cube([w,w+1,w]);
    
    // wire slot
    translate([0,w/4,0])
    cube([w/2,w/2,h1]);
    
    // chamfered corners
    rotate([0,0,270]){
        translate([-w,0,0]) {
            translate([0,-w/4,h1-w/2-1])
            rotate([45,0,0])
            cube([w,w,w]);

            translate([0,w*5/4,h1-w/2-1])
            rotate([45,0,0])
            cube([w,w,w]);
        }
    }   
    // ziptie slot
    translate([0,0,h1/2])
    cube([holeR,w,holeR]);
}