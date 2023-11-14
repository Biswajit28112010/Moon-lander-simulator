# Moon-lander-simulator
Overview:

Introduction:

The script welcomes users to the Moon Landing Simulator and sets the context that they are controlling a Chandrayaan-3 lander from ISRO.
User Instructions:

Provides clear instructions on how to control the spacecraft: 'thrust' to decrease speed or 'descend' to land.
Simulation Parameters:

Initializes the spacecraft's altitude and speed parameters for the simulation.
Main Simulation Loop:

Enters a while loop that continues as long as the altitude is above 0.
Displays current altitude and speed to the user.
Takes user input for commands ('thrust' or 'descend').
User Commands:

If the user inputs 'thrust', decreases altitude by 100 and increases speed by 10.
If the user inputs 'descend', decreases altitude by 200 and decreases speed by 30.
Prints an error message for invalid commands.
Landing Outcome:

Checks if the altitude is less than or equal to 0.
If the speed is less than 5, declares a successful landing.
If the speed is 5 or greater, declares a crash.
Altitude Warning:

If the altitude is less than or equal to 100, warns the user about low altitude.
Delay for Visualization:

Introduces a delay of 1 second between iterations for better visualization.
Script Execution:

The main() function is called if the script is run directly.
Potential Enhancements:

Function decomposition for improved readability.
Introduction of random events or obstacles.
User feedback and scoring system.
Graphics or visualization enhancements.
Difficulty levels and customizable parameters.
Logging for events during the simulation.
This script provides a foundation for a text-based Moon Landing Simulator and can be expanded upon to create a more immersive and engaging experience.




