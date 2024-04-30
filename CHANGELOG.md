# Change Log

All notable changes to this project will be documented in this file.
 
## [1.0.4] - 2023-09-05
 
Removed the LCD kit display because it was redundant and added an OBS Source display that will display the contents of the OBS source file.

## [1.0.3] - 2023-07-27
 
Added the behavior to query the TD-50X for the current kit number on midi connect and by the press of a button.

## [1.0.2] - 2023-07-24
 
This release changes the way Kit Data is queried from TD-50X. It maintains an offline list of kit data and simply listens for program changes over midi.
 
## [1.0.1] - 2023-07-20

Added a taskbar icon

### Fixed

Instead of querying kit data on the fly, it queries all kits up front in one request.
 
## [1.0.0] - 2023-07-19
 
Initial Release