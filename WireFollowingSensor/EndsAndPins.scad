/*
Erica Umlor Wire Following Sensor Holder for MSE4777

Created: 04/16/2020
Description: This is for my GrowBot project
for senior design. These are the ends to the wire 
following sensor holders. One end connects to the 
frame of our robot and the other end has a slot for 
the inductor to sit in. Don't try to edit this code.
Most of it is not parametric, and it should fit just
fine with this this project. 
*/

// print all 
ends();
pins(); 

// values
holeL = 15;    // length of pin hole
holeR = 2;     // pin hole radius
brace = 4;     // width 
w = 10;        // height and length
h1 = 35;       // length of inductor end
h2 = 25;       // length of inductor slot
depth = 4.1;   // depth of inductor slot
width = depth; // depth of inductor slot
pR = holeR-.05; 
more = 2;

module ends() {
  translate([20,0,0])
  botEnd();
  translate([-20,0,0])
  botEnd();
  sensorEndR();
  translate([-40,0,0])   
  sensorEndL();
}

module pins() {  
  translate([10,20,0]) 
  pin();
  translate([20,20,0]) 
  pin();    
  translate([-10,20,0]) 
  pin();
  translate([-20,20,0]) 
  pin();
}

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

module sensorEndL() {
    translate([0,0,10]) {
      rotate([0,90,0]) {
        union() {
          translate([0,22,00]) {
            difference() {  
              // right inductor pocket
              rotate([90,0,0]) 
              translate([0,0,8])  
              cube([w,w+width,h2/8]);  

              // pocket slot hole
              rotate([90,0,0])
              translate([width,6.9,0])  
              cylinder(h2/2,width,width); 
                
              // inductor slot
              translate([0,-15,3])
              cube([5,30,8.8+width-5]);
            } 
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
         
            // inductor cutout
            translate([0,5,3])
            cube([5,30,8.8+width-5]);
             
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

module pin() {
  union(){
    cylinder(2,holeR+2,holeR+2);
    cylinder(holeL+7,pR,pR);
  }
}
