# Frame Rate Perception Experiment

## Overview
This Python script uses the Pygame library to run a simple experiment for testing human perception of frame rates. 
The screen will display a blank background for a set amount of time with a single white frame inserted at a random point. 
The frame rate (FPS) and the number of frames for the fade effect can be parameterized.
To simply see if you can perceive an individual frame, set fade frames to 1.
Please note that setting the FPS above your display's refresh rate is best done with a fade, as higher FPS than refresh rate means you'll only be seeing a partial frame at best.

## Requirements
- Python 3.x
- Pygame

## Installation
To install Pygame, run the following command:

```
pip install pygame
```

## Usage
1. Clone this repository or download the Python script.
2. Run the script in your terminal.
3. You will be prompted to enter the frame rate (FPS) and the number of frames for the fade effect.

## How It Works
- The screen starts with a black background.
- At a random time, the screen will fade into white and back to black.
- The fade effect takes place over a number of frames specified by `fade_frames`.

## Contributing
Feel free to fork or whatever you want.

## License
The Unlicense
