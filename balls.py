import pygame
import math
import random

# Define the Ball class
class Ball:
    def __init__(self, pos, radius, velocity, color, is_main=False):
        self.pos = pos
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.is_main = is_main  # True if this ball is the main red ball

    def move(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.check_boundaries()

    def check_collision(self, center, radius):
        distance_to_center = math.sqrt((self.pos[0] - center[0])**2 + (self.pos[1] - center[1])**2)
        return distance_to_center + self.radius >= radius

    def bounce(self):
        self.velocity[0] = -self.velocity[0] + random.uniform(-1, 1)
        self.velocity[1] = -self.velocity[1] + random.uniform(-1, 1)

    def check_boundaries(self):
        # Calculate distance from the center to the current position
        distance_from_center = math.sqrt((self.pos[0] - circle_center[0])**2 + (self.pos[1] - circle_center[1])**2)
        
        # Check if the ball is outside the circle
        if distance_from_center + self.radius > circle_radius:
            # Calculate the angle from the center to the ball
            angle = math.atan2(self.pos[1] - circle_center[1], self.pos[0] - circle_center[0])
            
            # Set the ball's position to the edge of the circle
            self.pos[0] = circle_center[0] + (circle_radius - self.radius) * math.cos(angle)
            self.pos[1] = circle_center[1] + (circle_radius - self.radius) * math.sin(angle)
            
            # Reflect the velocity vector off the circle edge
            normal = [self.pos[0] - circle_center[0], self.pos[1] - circle_center[1]]
            normal_length = math.sqrt(normal[0]**2 + normal[1]**2)
            normal = [n / normal_length for n in normal]
            
            dot_product = (self.velocity[0] * normal[0] + self.velocity[1] * normal[1])
            self.velocity[0] -= 2 * dot_product * normal[0]
            self.velocity[1] -= 2 * dot_product * normal[1]

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncing Ball Simulation')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Font for displaying ball count
font = pygame.font.Font(None, 36)

# Ball properties
initial_ball_radius = 10
initial_ball_velocity = [2, 3]
initial_ball_color = black
main_ball_color = red

# Circle properties
circle_center = (400, 300)
circle_radius = 250

# Initialize balls
main_ball = Ball([400, 300], initial_ball_radius, initial_ball_velocity[:], main_ball_color, is_main=True)
balls = [main_ball]

# Control variables
balls_to_add = 10  # Number of new balls added each time the red ball bounces

# Run the game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Move and check collision for all balls
    new_balls = []
    for ball in balls:
        ball.move()
        if ball.check_collision(circle_center, circle_radius):
            ball.bounce()
            if ball.is_main:
                # Add new white balls
                for _ in range(balls_to_add):
                    new_ball_pos = [ball.pos[0] + random.uniform(-10, 10), ball.pos[1] + random.uniform(-10, 10)]
                    new_balls.append(Ball(new_ball_pos, ball.radius, initial_ball_velocity[:], white))

    # Add the new balls to the list
    balls.extend(new_balls)

    # Draw everything
    window.fill(black)  # Set background color to black
    pygame.draw.circle(window, white, circle_center, circle_radius, 1)  # Set circle color to white
    for ball in balls:
        pygame.draw.circle(window, ball.color, (int(ball.pos[0]), int(ball.pos[1])), ball.radius)
    
    # Draw ball count
    ball_count_text = font.render(f'Ball Count: {len(balls)}', True, white)  # Change text color to white for better contrast
    window.blit(ball_count_text, (10, 10))

    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
