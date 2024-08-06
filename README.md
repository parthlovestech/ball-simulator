# Bouncing Balls Simulation

## Overview

This Python script simulates bouncing balls within a circular area. Each time a ball bounces, the total number of balls doubles.
## Features

- **Bouncing Balls**: Balls bounce off the circle's boundary and double in number each time they bounce.
- **Dynamic Ball Count**: The total number of balls is updated in real-time and displayed on the screen.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/parthlovestech/ball-simulator.git
   cd ball-simulator
   ```

2. **Install Pygame:**

   ```bash
   pip install pygame
   ```

## Usage

1. **Run the Script:**

   ```bash
   python balls.py
   ```

2. **Control the Simulation:**

   - Press `ESC` to quit the simulation.

## Configuration

Customize the simulation by modifying these variables in the \`balls.py\` script:

- `circle_center`: Coordinates of the circle's center (x, y).
- `circle_radius`: Radius of the circle.
- `hole_center`: Coordinates of the hole's center (x, y).
- `hole_radius`: Radius of the hole.
- `initial_ball_radius`: Radius of each ball.
- `initial_ball_velocity`: Initial velocity of the balls (x, y).
- `balls_to_add`: Number of new balls added each time any ball bounces.


