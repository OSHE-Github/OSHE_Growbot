/*
Erica Umlor Wire Following Sensor Holder for MSE4777

Created: 04/16/2020
Description: This is for my GrowBot project
for senior design. This is the right end to the wire 
following sensor holders. This end has a slot for 
the inductor to sit in. Don't try to edit this code.
Most of it is not parametric, and it should fit just
fine with this this project. 
*/

sensorEndR(); 

// values
holeL = 15;    // length of pin hole
holeR = 2;     // pin hole radius
brace = 4;     // width 
w = 10;        // height and length
h1 = 35;       // length of inductor end
h2 = 25;       // length of inductor slot
depth = 4.1;   // depth of inductor slot
width = depth; // depth of inductor slot
more = 2;

module sensorEndR() {
    translate([0,0,10]) {
      rotate([0,90,0]) {
        union() {
          difference() {  
            rotate([90,0,0])
             // right inductor pocket
             translate([0,0,0])  
             cube([w,w+width,h2/8]);  
             
             // pocket slot hole
             rotate([90,0,0])
             translate([width,6.9,0])  
             cylinder(h2/2,width,width); 
              
             // inductor cutout 
             translate([0,-15,3])
             cube([5,30,8.8+width-5]);
          }           
          difference() {       
            // main body
            translate([0,-more/2,0])
            cube([w,w+more,h1]);
    
            // top hole
            translate([w/2,-20,h1-w/2])
            rotate([-90,0,0])
            cylinder(holeL*4,holeR,holeR);
        
            // wire slot
            translate([0,w/4,0])
            cube([w/2,w/2,h1]);
         
            // inductor slot
            translate([0,-3,3])
            cube([5,5+more,8.8+width-5]);
             
            rotate([0,0,270]){
              translate([-w,0,0]) {
                // chamfer top
                translate([-more/2,-w/4,h1-w/2-1])
                rotate([45,0,0])
                cube([w+more,w,w]);

                // chamfer bottom
                translate([0,w*5/4,h1-w/2-1])
                rotate([45,0,0])
                cube([w,w,w]);
              }
            }
          }
        }    
      }   
    }
}


