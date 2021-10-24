# R3-SoftwareTask2-BrandonTran
 
This project was written in Python using Visual Studio Code

Method: Keyboard

The purpose of this project was to create a Client and Server program that would read the inputs
of the keyboard and send back outputs based on what was received. The inputs were "1, 2, 3, 4, 5"
to determine the speed of the motors and "w,a,s,d" to determine the direction of movement. The 
output would display the speed and corresponding wheels that would reverse or move forward with respect
to the directional input. i.e Speed of 5 and W would output [f255][f255][f255][f255] because all 4 wheels 
move forward at speed of 5 * 51. 

The program was kept continously running by creating an infinite loop using While True. The Keyboard
library from Python was also used to read the keyboard inputs. Wait times of 1s were supposed to prevent
the program from flooding the terminal with print statements and a large Port number was used to ensure
that it was not interfering with other ports that may be in use. 

