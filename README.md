# CHEME 5500 Final Project

### Group Members:
Moran, Terrence   
Zhao, Mingjie   
2018/05/07   

### Program Introduction
This program is designed to prevent a headache for undergraduate engineering students tasked with solving Euler Beam problems.

### How-to
To run the program start by running main_script.py.
This will prompt the user to input several values   
1. Geometry/Material Properites   
  a. Length of the Beam (ft)   
  b. Width of the Cross Section (in)   
  c. Height of the Cross Section (in)   
  d. Modulus of Elasticity of the Beam material(Ksi)   

2. Support Conditions at each end of the beam. Options:    
  [1] fixed    
  [2] pinned    
  [3] roller    
  [4] cantilever (free end)    
  If input conditions that make the beam indeterminate (unsolvable) or are not any of the options above 
an error message will be printed and the questions will be reasked.

3. Loading Conditions throughout the beam. Options:        
  [1] point load (kips): will prompt user to input location of point load and magnitude of load     
  [2] distributed load (kips/ft): will ask what type of distributed load     
	  a. constant asks for magnitude of constant load      
    b. triangular distributed asks for magnitude of load at x=Length (assumes load is zero at x=zero)    
  If the loading conditions are incorrect (example: point load location outside of beam domain), the program will output an error and reask the question.
 
4. Solving for displacement of the beam      
The above info is passed to a function (deflection.py) and solved. It returns a numpy array of the length of the beam and the deflection of the beam.

5. Post processing       
This info is then plotted in main_script.py          
The next step is to find the maximum deflection in the beam as this is often a governing value. The program then asks the user to specify a location. With this input the deflection at that point is calculated using the function find nearest.

6. PyGame GUI (pygame_script)      
This script sets up PyGame and generates a GUI to display the outputs from the command window. When run, a pop-up window will guide you towards the results. One interesting thing is that we defined some buttons for users to click on to enhance interactions. 

