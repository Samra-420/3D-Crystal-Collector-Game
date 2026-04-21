"""
============================================================
CRYSTAL COLLECTOR 3D - Ultimate Professional Edition
Perfect UI + Smooth Controls + Complete Visual Experience
============================================================
"""

import turtle
import time
import math
import random as py_random

print("="*60)
print("    🎮 CRYSTAL COLLECTOR 3D 🎮")
print("="*60)

# ===== PART 1: PERFECT TURTLE MENU =====
print("\n[SYSTEM] Loading Main Menu...")

# Create perfect screen
screen = turtle.Screen()
screen.setup(900, 600)
screen.title("Crystal Collector 3D")
screen.bgcolor("#0a0e27")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# Clean stars background
py_random.seed(10)
for i in range(25):
    x = py_random.randint(-440, 440)
    y = py_random.randint(-270, 270)
    pen.goto(x, y)
    pen.dot(1.5, "#ffffff")

# Professional title
pen.goto(0, 160)
pen.color("#00d4ff")
pen.write("⚡ CRYSTAL COLLECTOR 3D ⚡", align="center", font=("Arial", 38, "bold"))

pen.goto(0, 115)
pen.color("#7dd3fc")
pen.write("Collect 8 Crystals | Avoid Red Obstacles", align="center", font=("Arial", 14))

# Clean instructions box
pen.goto(-220, 60)
pen.color("#1e40af")
pen.pensize(2)
pen.pendown()
for _ in range(2):
    pen.forward(440)
    pen.right(90)
    pen.forward(150)
    pen.right(90)
pen.penup()

# Instructions content
instructions = [
    ("🎮 CONTROLS", "#00d4ff", 16, "bold", 40),
    ("Arrow Keys : Move & Turn", "#a5f3fc", 13, "", 15),
    ("SPACE      : Jump", "#fde047", 13, "bold", 0),
    ("", "", 0, "", -10),
    ("🎯 MISSION", "#00d4ff", 16, "bold", -20),
    ("• Collect 8 Blue Crystals", "#d1d5db", 12, "", -45),
    ("• Avoid Red Obstacles", "#fca5a5", 12, "", -70),
    ("• Touch Red = Game Over", "#ff6b6b", 12, "bold", -95),
]

for text, color, size, style, y_offset in instructions:
    if text.strip():
        pen.goto(0, y_offset)
        pen.color(color)
        if style == "bold":
            pen.write(text, align="center", font=("Arial", size, "bold"))
        else:
            pen.write(text, align="center", font=("Arial", size))

# SIMPLE START BUTTON - No green box, just text
btn_text = turtle.Turtle()
btn_text.hideturtle()
btn_text.penup()
btn_text.goto(0, -180)  # Position for text
btn_text.color("#00d4ff")  # Changed to cyan/blue color

game_started = False
frame = 0

def start_game():
    global game_started
    game_started = True
    print("[USER] Starting game...")

screen.onkey(start_game, "space")
screen.listen()

print("\n⏳ Press SPACE to start...")

# Clean animation loop
while not game_started:
    frame += 1
    
    # Update button pulse effect
    btn_text.clear()
    btn_text.goto(0, -180)
    
    # Pulse effect for text only - no green box
    alpha = 0.6 + 0.4 * math.sin(frame * 0.1)
    r = int(0 * alpha)
    g = int(212 * alpha)
    b = int(255 * alpha)
    btn_text.color(f"#{r:02x}{g:02x}{b:02x}")
    btn_text.write("PRESS SPACE TO START", align="center", font=("Arial", 16, "bold"))
    
    screen.update()
    time.sleep(0.016)

# Quick transition
print("[SYSTEM] Loading 3D engine...")
pen.clear()
btn_text.clear()

for i in range(5):
    pen.goto(0, 0)
    pen.color("#00d4ff")
    pen.write("LOADING 3D WORLD...", align="center", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(0.1)
    pen.clear()

screen.bye()
print("[UI] Menu completed!\n")

# ===== PART 2: PROFESSIONAL 3D GAME =====
print("🚀 Starting 3D Game World...")

from vpython import *

class Config:
    SPEED = 0.3
    TURN = 4
    JUMP = 0.45  # Reduced jump height for better control
    GRAVITY = 0.03  # Increased gravity for faster falls
    SIZE = 35
    CRYSTALS = 8
    OBSTACLES = 9  # Increased from 5 to 9 obstacles

cfg = Config()

# Professional scene setup
scene = canvas(
    title="🎮 CRYSTAL COLLECTOR 3D - Arrow Keys: Move | SPACE: Jump",
    width=1200,
    height=700,
    background=vector(0.05, 0.05, 0.15),
    center=vector(0, 5, 0)
)

scene.camera.pos = vector(0, 25, 35)
scene.camera.axis = vector(0, -10, -35)
scene.range = 22
scene.ambient = color.gray(0.25)

# Enhanced lighting
sun = distant_light(direction=vector(0.5, -1, 0.3), color=vector(1, 0.98, 0.9))
fill = distant_light(direction=vector(-0.5, -0.5, -0.5), color=vector(0.3, 0.4, 0.5))
glow_light = local_light(pos=vector(0, 10, 0), color=vector(0.2, 0.5, 1))

# Clean arena with texture
floor = box(
    pos=vector(0, -1, 0),
    size=vector(cfg.SIZE, 1, cfg.SIZE),
    color=vector(0.15, 0.25, 0.35),
    shininess=0.5
)

# Subtle grid
for i in range(-cfg.SIZE//2, cfg.SIZE//2 + 1, 5):
    box(pos=vector(i, -0.45, 0), size=vector(0.03, 0.02, cfg.SIZE),
        color=vector(0, 0.8, 1), opacity=0.2)
    box(pos=vector(0, -0.45, i), size=vector(cfg.SIZE, 0.02, 0.03),
        color=vector(0, 0.8, 1), opacity=0.2)

# Transparent walls with glow
h = 5
hs = cfg.SIZE / 2
wall_color = vector(0.2, 0.5, 0.8)

walls = []
for pos, size in [
    (vector(0, h/2, -hs), vector(cfg.SIZE, h, 0.5)),
    (vector(0, h/2, hs), vector(cfg.SIZE, h, 0.5)),
    (vector(-hs, h/2, 0), vector(0.5, h, cfg.SIZE)),
    (vector(hs, h/2, 0), vector(0.5, h, cfg.SIZE))
]:
    wall = box(pos=pos, size=size, color=wall_color, opacity=0.3, shininess=0.5)
    walls.append(wall)

# ===== ENHANCED PLAYER WITH BETTER VISIBILITY =====
class Player:
    def __init__(self, p):
        # ENHANCED VISIBILITY: Larger and brighter collector
        self.body = compound([
            # Main body (brighter purple sphere)
            sphere(pos=vector(0, 0, 0), radius=1.2, color=vector(0.8, 0.3, 1), shininess=0.8),
            
            # Collector dish (larger and brighter gold)
            cylinder(pos=vector(0, 0, 1.0), axis=vector(0, 0, 0.7), radius=1.5,
                     color=vector(1, 0.9, 0.3), opacity=0.9, shininess=1.0),
            
            # Antenna with light
            cylinder(pos=vector(0, 1.0, 0), axis=vector(0, 0.5, 0), radius=0.1,
                     color=vector(1, 1, 0.5)),
            sphere(pos=vector(0, 1.5, 0), radius=0.15, color=vector(1, 1, 0), emissive=True),
            
            # Side thrusters (brighter)
            box(pos=vector(-0.8, -0.3, 0), size=vector(0.4, 0.5, 0.4),
                color=vector(1, 0.7, 0.3), shininess=0.7),
            box(pos=vector(0.8, -0.3, 0), size=vector(0.4, 0.5, 0.4),
                color=vector(1, 0.7, 0.3), shininess=0.7),
            
            # Front indicator
            arrow(pos=vector(0, 0, 1.5), axis=vector(0, 0, 0.7), shaftwidth=0.2,
                  color=vector(0, 1, 1))
        ])
        self.body.pos = p
        
        # Stronger purple glow effect
        self.glow = sphere(pos=p, radius=2.0, color=vector(0.9, 0.4, 1),
                          opacity=0.3, emissive=True)
        
        # Dynamic shadow
        self.shadow = cylinder(pos=vector(p.x, -0.45, p.z), axis=vector(0, 0.05, 0),
                              radius=1.8, color=vector(0, 0, 0), opacity=0.4)
        
        # Physics
        self.vel = vector(0, 0, 0)
        self.angle = 0
        self.on_ground = True
        self.alive = True
        self.jump_cooldown = 0

    @property
    def pos(self):
        return self.body.pos

    @pos.setter
    def pos(self, p):
        offset = p - self.body.pos
        self.body.pos = p
        self.glow.pos = p
        self.shadow.pos = vector(p.x, -0.45, p.z)
        
        # Dynamic shadow based on height
        h_factor = max(0.2, 1 - (p.y - 1) / 20)
        self.shadow.radius = 1.8 * h_factor
        self.shadow.opacity = 0.4 * h_factor

    def forward(self):
        if not self.alive: return
        direction = vector(sin(radians(self.angle)), 0, -cos(radians(self.angle)))
        new_pos = self.pos + direction * cfg.SPEED
        limit = hs - 1.5
        if abs(new_pos.x) < limit and abs(new_pos.z) < limit:
            self.pos = new_pos

    def backward(self):
        if not self.alive: return
        direction = vector(sin(radians(self.angle)), 0, -cos(radians(self.angle)))
        new_pos = self.pos - direction * cfg.SPEED * 0.7
        limit = hs - 1.5
        if abs(new_pos.x) < limit and abs(new_pos.z) < limit:
            self.pos = new_pos

    def turn_left(self):
        if not self.alive: return
        self.angle += cfg.TURN
        self.body.rotate(angle=radians(cfg.TURN), axis=vector(0, 1, 0))

    def turn_right(self):
        if not self.alive: return
        self.angle -= cfg.TURN
        self.body.rotate(angle=radians(-cfg.TURN), axis=vector(0, 1, 0))

    def jump(self):
        if not self.alive: return
        if self.on_ground and self.jump_cooldown <= 0:
            self.vel.y = cfg.JUMP
            self.on_ground = False
            self.glow.radius = 2.5
            self.glow.color = vector(1, 0.9, 0.4)  # Brighter gold when jumping
            self.jump_cooldown = 0.5

    def update(self, dt):
        if not self.alive: return
        
        if self.jump_cooldown > 0:
            self.jump_cooldown -= dt
        
        if not self.on_ground:
            self.vel.y -= cfg.GRAVITY
            new_pos = self.pos + self.vel
            if new_pos.y <= 1:
                new_pos.y = 1
                self.on_ground = True
                self.vel.y = 0
                self.glow.radius = 2.0
                self.glow.color = vector(0.9, 0.4, 1)  # Back to purple
            self.pos = new_pos

    def collect_effect(self):
        self.glow.color = vector(0, 1, 0.7)  # Brighter green when collecting
        self.glow.radius = 2.8

    def reset_effect(self):
        self.glow.color = vector(0.9, 0.4, 1)  # Back to purple
        self.glow.radius = 2.0

    def game_over(self):
        self.alive = False
        self.glow.color = vector(1, 0.3, 0.3)  # Red when game over
        self.glow.radius = 3.0

player = Player(vector(0, 1, 0))

# ===== SIMPLIFIED CRYSTAL =====
class Crystal:
    def __init__(self, p):
        self.collected = False
        
        # Crystal design
        self.core = cone(pos=p, axis=vector(0, 1.5, 0), radius=0.7,
                        color=vector(0, 1, 0.9), shininess=1)
        
        # Bottom part
        self.bottom = cone(pos=p, axis=vector(0, -1, 0), radius=0.7,
                          color=vector(0, 1, 0.9), shininess=1)
        
        # Enhanced glow
        self.glow = sphere(pos=p + vector(0, 0.4, 0), radius=1.2,
                          color=vector(0, 1, 1), opacity=0.25, emissive=True)
        
        # Rotating rings
        self.ring1 = ring(pos=p + vector(0, 0.4, 0), axis=vector(1, 0, 0),
                         radius=1.0, thickness=0.08, color=vector(0.5, 1, 1))
        self.ring2 = ring(pos=p + vector(0, 0.4, 0), axis=vector(0, 1, 0),
                         radius=1.0, thickness=0.08, color=vector(0, 1, 0.8))
        
        self.time = 0
        self.base_y = p.y
        self.rotation_speed = py_random.uniform(1, 2)
        self.float_speed = py_random.uniform(1.5, 2.5)

    @property
    def pos(self):
        return self.core.pos

    def update(self, dt):
        if self.collected: return
        
        self.time += dt
        
        # Enhanced floating animation
        new_y = self.base_y + 0.5 * sin(self.time * self.float_speed)
        self.core.pos.y = new_y
        self.bottom.pos.y = new_y
        self.glow.pos.y = new_y + 0.4
        self.ring1.pos.y = new_y + 0.4
        self.ring2.pos.y = new_y + 0.4
        
        # Enhanced rotation
        self.core.rotate(angle=radians(self.rotation_speed), axis=vector(0, 1, 0))
        self.bottom.rotate(angle=radians(self.rotation_speed), axis=vector(0, 1, 0))
        self.ring1.rotate(angle=radians(self.rotation_speed * 1.5), axis=vector(1, 0, 0))
        self.ring2.rotate(angle=radians(self.rotation_speed * 1.2), axis=vector(0, 1, 0))
        
        # Enhanced pulse
        pulse = 1 + 0.2 * sin(self.time * 3)
        self.glow.radius = 1.2 * pulse

    def collect(self):
        self.collected = True
        # Enhanced collection animation
        for i in range(10):
            scale = 1 + i * 0.25
            fade = 1 - i/10
            
            self.glow.radius = 1.2 * scale
            self.glow.opacity = 0.25 * fade
            
            self.ring1.radius = 1.0 * scale
            self.ring1.opacity = fade
            
            self.ring2.radius = 1.0 * scale
            self.ring2.opacity = fade
            
            rate(25)
        
        self.core.visible = False
        self.bottom.visible = False
        self.glow.visible = False
        self.ring1.visible = False
        self.ring2.visible = False

# Spawn crystals randomly
crystals = []
for _ in range(cfg.CRYSTALS):
    pos = vector(py_random.uniform(-hs + 3, hs - 3), 
                 py_random.uniform(1.5, 4), 
                 py_random.uniform(-hs + 3, hs - 3))
    crystals.append(Crystal(pos))

# ===== OBSTACLES WITH RANDOM POSITIONS AND ROTATION =====
class Obstacle:
    def __init__(self, p):
        # Create moving and rotating obstacle
        self.base_pos = p
        self.height = py_random.uniform(1.8, 2.2)
        
        # Main obstacle body
        self.core = box(pos=vector(p.x, self.height, p.z), 
                       size=vector(2.4, 3.0, 2.4), 
                       color=vector(1, 0.2, 0.2), shininess=0.9)
        
        # Rotating rings
        self.ring1 = ring(pos=vector(p.x, self.height + 1.5, p.z), 
                         axis=vector(0, 1, 0),
                         radius=1.8, thickness=0.2, 
                         color=vector(1, 0.1, 0.1))
        
        self.ring2 = ring(pos=vector(p.x, self.height + 1.5, p.z), 
                         axis=vector(1, 0, 0),
                         radius=1.8, thickness=0.2, 
                         color=vector(1, 0.5, 0.1))
        
        # Top light
        self.top_light = sphere(pos=vector(p.x, self.height + 2.2, p.z), 
                               radius=0.4,
                               color=vector(1, 0.6, 0.2), emissive=True)
        
        # Glow effect
        self.glow = box(pos=vector(p.x, self.height, p.z), 
                       size=vector(3.2, 3.8, 3.2),
                       color=vector(1, 0.3, 0.3), opacity=0.3, emissive=True)
        
        # Warning lights
        self.lights = []
        colors = [vector(1, 0.2, 0.2), vector(1, 0.6, 0.2), 
                  vector(1, 0.2, 0.2), vector(1, 0.6, 0.2)]
        for i in range(4):
            angle = i * 90
            x = cos(radians(angle)) * 1.6
            z = sin(radians(angle)) * 1.6
            light = sphere(pos=vector(p.x + x, self.height + 1.5, p.z + z), 
                          radius=0.3,
                          color=colors[i], emissive=True)
            self.lights.append(light)
        
        self.time = 0
        self.float_height = py_random.uniform(0.5, 1.0)
        self.float_speed = py_random.uniform(1.0, 2.0)
        self.rotate_speed = py_random.uniform(2.0, 4.0)  # Faster rotation
        self.move_speed = py_random.uniform(0.5, 1.5)
        self.move_radius = py_random.uniform(2.0, 5.0)
        self.move_angle = py_random.uniform(0, 360)

    def update(self, dt):
        self.time += dt
        
        # Floating movement
        float_y = self.base_pos.y + self.float_height * sin(self.time * self.float_speed)
        
        # Circular movement
        self.move_angle += self.move_speed * dt
        move_x = cos(radians(self.move_angle)) * self.move_radius
        move_z = sin(radians(self.move_angle)) * self.move_radius
        
        new_pos = vector(self.base_pos.x + move_x, float_y, self.base_pos.z + move_z)
        
        # Update all parts
        self.core.pos = new_pos
        self.ring1.pos = vector(new_pos.x, new_pos.y + 1.5, new_pos.z)
        self.ring2.pos = vector(new_pos.x, new_pos.y + 1.5, new_pos.z)
        self.top_light.pos = vector(new_pos.x, new_pos.y + 2.2, new_pos.z)
        self.glow.pos = new_pos
        
        # Update lights
        for i, light in enumerate(self.lights):
            angle = i * 90 + self.time * 30
            x = cos(radians(angle)) * 1.6
            z = sin(radians(angle)) * 1.6
            light.pos = vector(new_pos.x + x, new_pos.y + 1.5, new_pos.z + z)
        
        # Enhanced rotation - all parts rotate
        rotate_angle = radians(self.rotate_speed)
        self.core.rotate(angle=rotate_angle, axis=vector(0, 1, 0), origin=new_pos)
        self.ring1.rotate(angle=rotate_angle * 1.5, axis=vector(1, 0, 0), origin=vector(new_pos.x, new_pos.y + 1.5, new_pos.z))
        self.ring2.rotate(angle=rotate_angle * 1.2, axis=vector(0, 1, 0), origin=vector(new_pos.x, new_pos.y + 1.5, new_pos.z))
        self.glow.rotate(angle=rotate_angle, axis=vector(0, 1, 0), origin=new_pos)
        
        # Blinking lights
        blink = sin(self.time * 8) > 0
        for light in self.lights:
            light.opacity = 1.0 if blink else 0.4
            light.radius = 0.35 if blink else 0.25
        
        # Pulsing glow
        pulse = 1 + 0.15 * sin(self.time * 5)
        self.glow.size = vector(3.2, 3.8, 3.2) * pulse

    def check_hit(self, player_pos):
        return mag(self.core.pos - player_pos) < 2.8

# Spawn obstacles in COMPLETELY RANDOM positions - NOW 9 OBSTACLES
obstacles = []
occupied_positions = []  # Track positions to avoid overlap

for _ in range(cfg.OBSTACLES):
    attempts = 0
    while attempts < 50:  # Try up to 50 times to find a good position
        # Random position anywhere in arena
        pos = vector(py_random.uniform(-hs + 3, hs - 3), 
                     2.0,  # Base height
                     py_random.uniform(-hs + 3, hs - 3))
        
        # Check distance from center (start position)
        if mag(pos) < 6:  # Increased from 4 to 6
            attempts += 1
            continue
        
        # Check distance from other obstacles
        too_close = False
        for obstacle_pos in occupied_positions:
            if mag(pos - obstacle_pos) < 7:  # Minimum 7 units between obstacles
                too_close = True
                break
        
        # Check distance from crystals
        if not too_close:
            for crystal in crystals:
                if mag(pos - crystal.pos) < 5:
                    too_close = True
                    break
        
        if not too_close:
            obstacles.append(Obstacle(pos))
            occupied_positions.append(pos)
            break
        
        attempts += 1
    
    if attempts >= 50:
        # If can't find perfect spot, place anyway
        pos = vector(py_random.uniform(-hs + 4, hs - 4), 
                     2.0,
                     py_random.uniform(-hs + 4, hs - 4))
        obstacles.append(Obstacle(pos))
        occupied_positions.append(pos)

print(f"[SYSTEM] Spawned {len(obstacles)} obstacles")

# ===== PROFESSIONAL UI =====
# Top info bar
game_info = label(
    pos=vector(0, 13, 0),
    text="💎 0/8 | ⏱ 0s",
    height=22,
    color=vector(1, 1, 1),
    box=False,
    line=False
)

# Game over overlay (centered and properly sized)
game_over_label = label(
    pos=vector(0, 8, 0),
    text="",
    height=45,
    color=vector(1, 0.3, 0.3),
    box=False,
    visible=False,
    line=False
)

# Final score display
final_score_label = label(
    pos=vector(0, 0, 0),
    text="",
    height=32,
    color=vector(1, 1, 1),
    box=False,
    visible=False,
    line=False
)

# ===== INPUT SYSTEM =====
keys = {'up': False, 'down': False, 'left': False, 'right': False, 'space': False}

def handle_keydown(evt):
    k = evt.key
    if k == 'up': keys['up'] = True
    elif k == 'down': keys['down'] = True
    elif k == 'left': keys['left'] = True
    elif k == 'right': keys['right'] = True
    elif k == ' ': keys['space'] = True

def handle_keyup(evt):
    k = evt.key
    if k == 'up': keys['up'] = False
    elif k == 'down': keys['down'] = False
    elif k == 'left': keys['left'] = False
    elif k == 'right': keys['right'] = False
    elif k == ' ': keys['space'] = False

scene.bind('keydown', handle_keydown)
scene.bind('keyup', handle_keyup)

# ===== GAME LOOP =====
score = 0
game_time = 0
game_active = True
game_ended = False

print("\n✅ Game Started! Collect all crystals!")
print(f"Warning: {len(obstacles)} moving obstacles in arena!")
print("Controls: Arrow Keys = Move/Turn, SPACE = Jump\n")

# Main game loop
while not game_ended:
    rate(60)
    dt = 1/60
    game_time += dt
    
    if game_active:
        # Handle input
        if keys['up']:
            player.forward()
        if keys['down']:
            player.backward()
        if keys['left']:
            player.turn_left()
        if keys['right']:
            player.turn_right()
        if keys['space']:
            player.jump()
            keys['space'] = False
        
        # Update player
        player.update(dt)
        glow_light.pos = player.pos + vector(0, 5, 0)
        
        # Update crystals
        for crystal in crystals:
            if not crystal.collected:
                crystal.update(dt)
                if mag(crystal.pos - player.pos) < 2.8:
                    player.collect_effect()
                    crystal.collect()
                    score += 1
                    
                    # Reset effect
                    def reset():
                        rate(12)
                        player.reset_effect()
                    
                    if score >= cfg.CRYSTALS:
                        game_active = False
                        game_ended = True
        
        # Update obstacles (with movement and rotation)
        for obstacle in obstacles:
            obstacle.update(dt)
            if obstacle.check_hit(player.pos):
                player.game_over()
                game_active = False
                game_ended = True
        
        # Smooth camera follow
        target_cam_pos = player.pos + vector(0, 25, 38)
        target_look_at = player.pos + vector(0, -2, 0)
        
        scene.camera.pos = scene.camera.pos * 0.88 + target_cam_pos * 0.12
        current_look = scene.camera.pos + scene.camera.axis
        new_look = current_look * 0.88 + target_look_at * 0.12
        scene.camera.axis = new_look - scene.camera.pos
        
        # Update UI
        game_info.text = f"💎 {score}/{cfg.CRYSTALS} | ⏱ {int(game_time)}s"
    
    else:
        break

# ===== PROFESSIONAL END SCREENS =====
# Center camera for end screen
scene.camera.pos = vector(0, 25, 35)
scene.camera.axis = vector(0, -10, -35)
scene.center = vector(0, 5, 0)

if score >= cfg.CRYSTALS:
    # VICTORY SCREEN
    print("\n" + "="*50)
    print("     🎉 VICTORY! 🎉")
    print("="*50)
    print(f"Collected {score}/{cfg.CRYSTALS} crystals")
    print(f"Time: {int(game_time)} seconds")
    print(f"Avoided {len(obstacles)} obstacles!")
    print("="*50)
    
    game_over_label.text = "🎉 VICTORY!"
    game_over_label.color = vector(0, 1, 0)
    final_score_label.text = f"Score: {score}/{cfg.CRYSTALS} | Time: {int(game_time)}s"
    
else:
    # GAME OVER SCREEN
    print("\n" + "="*50)
    print("     💀 GAME OVER! 💀")
    print("="*50)
    print("You hit a red obstacle!")
    print(f"Collected: {score}/{cfg.CRYSTALS} crystals")
    print(f"Time: {int(game_time)} seconds")
    print("="*50)
    
    game_over_label.text = "💀 GAME OVER!"
    game_over_label.color = vector(1, 0.3, 0.3)
    final_score_label.text = f"Score: {score}/{cfg.CRYSTALS} | Time: {int(game_time)}s"

# Show end screen properly centered
game_over_label.visible = True
final_score_label.visible = True

# Victory celebration or game over animation
for i in range(180):  # 6 seconds at 30 FPS
    rate(30)
    player.body.rotate(angle=radians(3), axis=vector(0, 1, 0))
    
    # Update obstacles even in end screen
    for obstacle in obstacles:
        obstacle.update(1/30)
    
    # Pulse effect for end screen
    if score >= cfg.CRYSTALS:
        pulse = 0.7 + 0.3 * sin(i * 0.1)
        game_over_label.color = vector(0, pulse, 0.5)
    else:
        pulse = 0.7 + 0.3 * sin(i * 0.1)
        game_over_label.color = vector(pulse, 0.2, 0.2)

print("\n🎮 Game Complete! Close window to exit.")
print("Thanks for playing Crystal Collector 3D!")
