import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("ball buster")

# Player properties
player = pygame.Rect(370, 700, 150, 50)
player_speed = 5

# Ball properties
ball = pygame.Rect(400, 300, 20, 20)  # Ball's size and initial position
ball_speed_x = random.choice([-3, 3])  # Ball's horizontal speed
ball_speed_y = random.choice([-3, 3])  # Ball's vertical speed

class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Brick properties
brick_width = 50
brick_height = 20
num_bricks = screen_width // brick_width
bricks = []

# Create bricks using brick class
bricks = []
colors = [(255, 255, 255), (0, 255, 0)]  # Add more colors as needed
num_layers = 2

for layer in range(num_layers):
    for i in range(num_bricks):
        brick = Brick(i * brick_width, layer * brick_height, brick_width, brick_height, colors[layer])
        bricks.append(brick)


# Clock for frame rate control
clock = pygame.time.Clock()
fps = 120

# Game loop flag
run = True

# Main game loop
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    # Movement keys
    key = pygame.key.get_pressed()

    # Move left
    if key[pygame.K_a] and player.left > 0:
        player.move_ip(-player_speed, 0)
    
    # Move right
    if key[pygame.K_d] and player.right < screen_width:
        player.move_ip(player_speed, 0)

    # Move up
    if key[pygame.K_w] and player.top > 0:
        player.move_ip(0, -player_speed)

    # Move down
    if key[pygame.K_s] and player.bottom < screen_height:
        player.move_ip(0, player_speed)
        
         # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with window boundaries
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Ball collision with player
    if player.colliderect(ball):
    # Calculate the hit position
        hit_position = (ball.centerx - player.left) / player.width

    # Adjust the horizontal speed based on where the ball hit the paddle
        max_horizontal_speed = 3  # You can adjust this value
        ball_speed_x = (hit_position - 0.5) * 2 * max_horizontal_speed

    # Reverse the vertical direction and adjust the speed if needed
        ball_speed_y *= -1
            
             # Ball collision with bricks
    for brick in bricks[:]:  # Iterate over a copy of the list
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1  # Reverse ball direction

    # Clear screen and redraw player
    screen.fill((0, 0, 0))  # Black background
    pygame.draw.rect(screen, (120, 0, 255), player)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)  # Red ball
    
    for brick in bricks:
        brick.draw(screen)
        
    # Update display and tick clock
    pygame.display.update()
    clock.tick(fps)

# Quit Pygame
pygame.quit()
