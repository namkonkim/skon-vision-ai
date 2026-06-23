"""
Generate 5 training images for Object Detection (Bounding Box) labeling practice.
Uses PIL to create illustration-style images with clear objects for bounding box practice.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math
import os

# Output directory
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_apple(draw, cx, cy, size, color='red'):
    """Draw an apple shape"""
    # Main body
    colors = {
        'red': [(180, 20, 20), (200, 30, 30), (220, 40, 40)],
        'green': [(40, 160, 40), (50, 180, 50), (60, 200, 60)],
    }
    c = colors.get(color, colors['red'])
    
    # Main apple body (slightly oval)
    x0, y0 = cx - size, cy - size * 0.9
    x1, y1 = cx + size, cy + size * 1.1
    draw.ellipse([x0, y0, x1, y1], fill=c[1])
    
    # Slight highlight
    hx, hy = cx - size * 0.3, cy - size * 0.4
    hs = size * 0.4
    draw.ellipse([hx - hs, hy - hs, hx + hs, hy + hs], fill=c[2])
    
    # Stem
    stem_w = max(2, size * 0.08)
    draw.line([(cx, cy - size * 0.9), (cx + size * 0.1, cy - size * 1.3)], 
              fill=(80, 50, 20), width=int(stem_w))
    
    # Small leaf
    leaf_pts = [
        (cx + size * 0.1, cy - size * 1.2),
        (cx + size * 0.4, cy - size * 1.4),
        (cx + size * 0.5, cy - size * 1.1),
        (cx + size * 0.2, cy - size * 1.0),
    ]
    draw.polygon(leaf_pts, fill=(40, 140, 40))

def draw_banana(draw, cx, cy, size, angle=0):
    """Draw a banana shape using arcs"""
    # Banana body - curved shape using polygon points
    points = []
    for i in range(20):
        t = i / 19.0
        # Curve
        x = cx + size * 2 * (t - 0.5)
        y = cy - size * 0.8 * math.sin(t * math.pi)
        points.append((x, y))
    # Return path (inner curve)
    for i in range(19, -1, -1):
        t = i / 19.0
        x = cx + size * 2 * (t - 0.5)
        y = cy - size * 0.5 * math.sin(t * math.pi) + size * 0.3
        points.append((x, y))
    
    draw.polygon(points, fill=(240, 220, 60))
    # Darker edge
    for i in range(len(points) // 2):
        if i < len(points) - 1:
            draw.line([points[i], points[i + 1]], fill=(200, 180, 40), width=2)
    
    # Brown tips
    draw.ellipse([cx - size + 2, cy - size * 0.2, cx - size + size * 0.15, cy + size * 0.15], 
                 fill=(120, 80, 30))
    draw.ellipse([cx + size - size * 0.15, cy - size * 0.2, cx + size - 2, cy + size * 0.15], 
                 fill=(120, 80, 30))

def draw_orange(draw, cx, cy, size):
    """Draw an orange"""
    # Main body
    draw.ellipse([cx - size, cy - size, cx + size, cy + size], fill=(240, 160, 30))
    # Texture dots
    for _ in range(15):
        dx = random.randint(-int(size * 0.7), int(size * 0.7))
        dy = random.randint(-int(size * 0.7), int(size * 0.7))
        if dx * dx + dy * dy < (size * 0.7) ** 2:
            ds = max(1, int(size * 0.03))
            draw.ellipse([cx + dx - ds, cy + dy - ds, cx + dx + ds, cy + dy + ds], 
                        fill=(230, 150, 25))
    # Highlight
    hx, hy = cx - size * 0.25, cy - size * 0.3
    hs = size * 0.3
    draw.ellipse([hx - hs, hy - hs, hx + hs, hy + hs], fill=(250, 180, 50))
    # Small stem dimple at top
    draw.ellipse([cx - size * 0.1, cy - size - size * 0.05, 
                  cx + size * 0.1, cy - size + size * 0.1], fill=(100, 140, 40))

def draw_mug(draw, cx, cy, w, h):
    """Draw a coffee mug"""
    # Body
    draw.rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2], 
                   fill=(240, 240, 245), outline=(180, 180, 185), width=2)
    # Handle (right side)
    handle_box = [cx + w // 2 - 2, cy - h // 4, cx + w // 2 + w // 4, cy + h // 4]
    draw.arc(handle_box, -90, 90, fill=(180, 180, 185), width=4)
    # Coffee inside (dark brown at top)
    coffee_top = cy - h // 2 + h // 6
    draw.ellipse([cx - w // 2 + 4, coffee_top - 5, cx + w // 2 - 4, coffee_top + 10], 
                 fill=(60, 30, 10))
    # Rim
    draw.ellipse([cx - w // 2, cy - h // 2 - 6, cx + w // 2, cy - h // 2 + 6], 
                 fill=(235, 235, 240), outline=(180, 180, 185), width=2)

def draw_keyboard(draw, cx, cy, w, h):
    """Draw a keyboard"""
    # Body
    draw.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2], 
                           radius=8, fill=(50, 50, 55), outline=(30, 30, 35), width=2)
    # Keys
    key_rows = 5
    key_cols = 14
    kw = (w - 30) // key_cols
    kh = (h - 20) // key_rows
    for r in range(key_rows):
        for c in range(key_cols):
            kx = cx - w // 2 + 12 + c * kw
            ky = cy - h // 2 + 8 + r * kh
            # Space bar on last row
            if r == key_rows - 1 and 4 <= c <= 9:
                if c == 4:
                    draw.rounded_rectangle([kx, ky + 2, kx + kw * 6 - 4, ky + kh - 2], 
                                          radius=2, fill=(70, 70, 75), outline=(40, 40, 45))
                continue
            elif r == key_rows - 1 and 5 <= c <= 9:
                continue
            draw.rounded_rectangle([kx, ky + 2, kx + kw - 4, ky + kh - 2], 
                                  radius=2, fill=(70, 70, 75), outline=(40, 40, 45))

def draw_smartphone(draw, cx, cy, w, h):
    """Draw a smartphone"""
    # Body
    draw.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2], 
                           radius=12, fill=(20, 20, 25), outline=(10, 10, 15), width=2)
    # Screen
    margin = 6
    draw.rounded_rectangle([cx - w // 2 + margin, cy - h // 2 + margin * 3,
                           cx + w // 2 - margin, cy + h // 2 - margin * 2],
                          radius=4, fill=(40, 120, 200))
    # Camera notch
    draw.ellipse([cx - 4, cy - h // 2 + 6, cx + 4, cy - h // 2 + 14], fill=(30, 30, 35))
    # Home indicator
    draw.rounded_rectangle([cx - 15, cy + h // 2 - margin, cx + 15, cy + h // 2 - margin + 3],
                          radius=1, fill=(60, 60, 65))

def draw_car(draw, cx, cy, w, h, color=(60, 100, 180)):
    """Draw a simplified car from the side"""
    # Body
    body_top = cy - h * 0.1
    draw.rounded_rectangle([cx - w // 2, body_top, cx + w // 2, cy + h // 2], 
                           radius=6, fill=color, outline=(max(0, color[0] - 30), max(0, color[1] - 30), max(0, color[2] - 30)), width=2)
    # Roof/cabin
    cabin_pts = [
        (cx - w * 0.3, body_top),
        (cx - w * 0.2, cy - h * 0.5),
        (cx + w * 0.25, cy - h * 0.5),
        (cx + w * 0.35, body_top),
    ]
    draw.polygon(cabin_pts, fill=color, outline=(max(0, color[0] - 30), max(0, color[1] - 30), max(0, color[2] - 30)))
    # Windows
    win1_pts = [
        (cx - w * 0.27, body_top - 2),
        (cx - w * 0.18, cy - h * 0.45),
        (cx - w * 0.02, cy - h * 0.45),
        (cx - w * 0.02, body_top - 2),
    ]
    draw.polygon(win1_pts, fill=(180, 210, 240))
    win2_pts = [
        (cx + w * 0.02, body_top - 2),
        (cx + w * 0.02, cy - h * 0.45),
        (cx + w * 0.22, cy - h * 0.45),
        (cx + w * 0.32, body_top - 2),
    ]
    draw.polygon(win2_pts, fill=(180, 210, 240))
    # Wheels
    wh_r = h * 0.2
    draw.ellipse([cx - w * 0.3 - wh_r, cy + h // 2 - wh_r, cx - w * 0.3 + wh_r, cy + h // 2 + wh_r], 
                 fill=(30, 30, 30), outline=(20, 20, 20))
    draw.ellipse([cx - w * 0.3 - wh_r * 0.5, cy + h // 2 - wh_r * 0.5, cx - w * 0.3 + wh_r * 0.5, cy + h // 2 + wh_r * 0.5], 
                 fill=(80, 80, 85))
    draw.ellipse([cx + w * 0.3 - wh_r, cy + h // 2 - wh_r, cx + w * 0.3 + wh_r, cy + h // 2 + wh_r], 
                 fill=(30, 30, 30), outline=(20, 20, 20))
    draw.ellipse([cx + w * 0.3 - wh_r * 0.5, cy + h // 2 - wh_r * 0.5, cx + w * 0.3 + wh_r * 0.5, cy + h // 2 + wh_r * 0.5], 
                 fill=(80, 80, 85))
    # Headlights
    draw.ellipse([cx + w // 2 - 12, body_top + 8, cx + w // 2 - 2, body_top + 20], fill=(255, 255, 200))
    draw.ellipse([cx - w // 2 + 2, body_top + 8, cx - w // 2 + 12, body_top + 20], fill=(255, 50, 50))

def draw_tree(draw, cx, cy, trunk_h, canopy_r):
    """Draw a tree"""
    # Trunk
    tw = canopy_r * 0.25
    draw.rectangle([cx - tw, cy, cx + tw, cy + trunk_h], fill=(100, 70, 40))
    # Canopy (multiple overlapping circles)
    for dx, dy in [(0, 0), (-canopy_r * 0.5, canopy_r * 0.2), (canopy_r * 0.5, canopy_r * 0.2),
                   (0, -canopy_r * 0.4), (-canopy_r * 0.3, -canopy_r * 0.2), (canopy_r * 0.3, -canopy_r * 0.2)]:
        r = canopy_r * 0.6
        draw.ellipse([cx + dx - r, cy - canopy_r * 0.3 + dy - r, 
                      cx + dx + r, cy - canopy_r * 0.3 + dy + r], 
                     fill=(40 + random.randint(-10, 10), 130 + random.randint(-20, 20), 40 + random.randint(-10, 10)))


def draw_table_surface(draw, width, height, color=(220, 200, 170)):
    """Draw a wooden table surface"""
    # Table top
    draw.rectangle([0, height * 0.3, width, height], fill=color)
    # Wood grain lines
    for i in range(8):
        y = int(height * 0.3 + (height * 0.7) * i / 8)
        grain_color = (color[0] - 15, color[1] - 15, color[2] - 15)
        draw.line([(0, y), (width, y)], fill=grain_color, width=1)
    # Shadow at edge
    draw.rectangle([0, int(height * 0.3), width, int(height * 0.32)], fill=(color[0] - 20, color[1] - 20, color[2] - 20))

def add_shadow(draw, cx, cy, rx, ry):
    """Add an elliptical shadow under an object"""
    shadow_color = (0, 0, 0, 30)
    for i in range(3):
        draw.ellipse([cx - rx - i, cy - ry // 3 + i, cx + rx + i, cy + ry // 3 + 3 + i],
                    fill=(180, 170, 155))


# ============================================
# IMAGE 1: det_easy_1.jpg - Single red apple
# ============================================
def generate_det_easy_1():
    img = Image.new('RGB', (800, 600), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    
    # Table surface
    draw_table_surface(draw, 800, 600, color=(245, 240, 235))
    
    # Shadow under apple
    add_shadow(draw, 400, 380, 70, 40)
    
    # Single red apple, centered
    draw_apple(draw, 400, 320, 65, color='red')
    
    img.save(os.path.join(OUT_DIR, 'det_easy_1.jpg'), quality=95)
    print("Generated det_easy_1.jpg")


# ============================================
# IMAGE 2: det_easy_2.jpg - Three separated fruits
# ============================================
def generate_det_easy_2():
    img = Image.new('RGB', (800, 600), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    
    # Table surface
    draw_table_surface(draw, 800, 600, color=(240, 235, 225))
    
    # Apple on the left
    add_shadow(draw, 180, 380, 60, 35)
    draw_apple(draw, 180, 320, 55, color='red')
    
    # Banana in the middle
    add_shadow(draw, 400, 370, 90, 30)
    draw_banana(draw, 400, 330, 55)
    
    # Orange on the right
    add_shadow(draw, 620, 380, 55, 35)
    draw_orange(draw, 620, 330, 50)
    
    img.save(os.path.join(OUT_DIR, 'det_easy_2.jpg'), quality=95)
    print("Generated det_easy_2.jpg")


# ============================================
# IMAGE 3: det_medium.jpg - Desk scene
# ============================================
def generate_det_medium():
    img = Image.new('RGB', (800, 600), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    
    # Desk surface (darker wood)
    draw_table_surface(draw, 800, 600, color=(160, 130, 100))
    
    # Keyboard (center-bottom area)
    draw_keyboard(draw, 400, 400, 350, 120)
    
    # Coffee mug (upper-left area, close to keyboard but not overlapping)
    draw_mug(draw, 180, 280, 70, 90)
    
    # Smartphone (right side, slightly angled visual)
    draw_smartphone(draw, 620, 320, 65, 130)
    
    img.save(os.path.join(OUT_DIR, 'det_medium.jpg'), quality=95)
    print("Generated det_medium.jpg")


# ============================================
# IMAGE 4: det_hard_1.jpg - Crowded fruit basket
# ============================================
def generate_det_hard_1():
    img = Image.new('RGB', (800, 600), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    
    # Table surface
    draw_table_surface(draw, 800, 600, color=(230, 220, 200))
    
    # Basket outline (woven look)
    basket_cx, basket_cy = 400, 350
    basket_w, basket_h = 300, 180
    # Basket body
    draw.ellipse([basket_cx - basket_w, basket_cy - basket_h // 2,
                  basket_cx + basket_w, basket_cy + basket_h],
                fill=(180, 140, 80), outline=(140, 100, 50), width=3)
    # Basket rim
    draw.ellipse([basket_cx - basket_w, basket_cy - basket_h // 2 - 15,
                  basket_cx + basket_w, basket_cy - basket_h // 2 + 25],
                fill=(190, 150, 90), outline=(140, 100, 50), width=2)
    # Weave pattern
    for i in range(12):
        x = basket_cx - basket_w + 50 * i + 25
        if basket_cx - basket_w < x < basket_cx + basket_w:
            draw.line([(x, basket_cy - basket_h // 4), (x, basket_cy + basket_h * 0.7)],
                     fill=(160, 120, 60), width=2)
    
    # Pile of overlapping fruits
    random.seed(42)
    
    # Layer 1 (back) - oranges and apples
    draw_orange(draw, 300, 280, 38)
    draw_apple(draw, 370, 270, 35, 'red')
    draw_orange(draw, 440, 275, 40)
    draw_apple(draw, 510, 280, 36, 'green')
    
    # Layer 2 (middle) - bananas and more fruits  
    draw_banana(draw, 350, 310, 35)
    draw_apple(draw, 280, 320, 32, 'red')
    draw_orange(draw, 460, 310, 35)
    draw_apple(draw, 400, 305, 33, 'red')
    
    # Layer 3 (front) - more overlapping
    draw_banana(draw, 430, 350, 30)
    draw_apple(draw, 340, 350, 30, 'green')
    draw_orange(draw, 380, 360, 28)
    draw_apple(draw, 470, 345, 32, 'red')
    
    # Extra fruits spilling out
    draw_apple(draw, 200, 380, 35, 'red')
    draw_orange(draw, 580, 370, 33)
    
    img.save(os.path.join(OUT_DIR, 'det_hard_1.jpg'), quality=95)
    print("Generated det_hard_1.jpg")


# ============================================
# IMAGE 5: det_hard_2.jpg - Street scene with parked cars
# ============================================
def generate_det_hard_2():
    img = Image.new('RGB', (800, 600), (135, 180, 220))
    draw = ImageDraw.Draw(img)
    
    # Sky gradient
    for y in range(250):
        r = 135 + int(50 * y / 250)
        g = 180 + int(40 * y / 250)
        b = 230 - int(20 * y / 250)
        draw.line([(0, y), (800, y)], fill=(min(r, 255), min(g, 255), min(b, 255)))
    
    # Buildings in background
    buildings = [
        (0, 120, 120, 300, (160, 155, 150)),
        (110, 100, 200, 300, (170, 165, 160)),
        (190, 140, 300, 300, (150, 145, 140)),
        (290, 90, 400, 300, (165, 160, 155)),
        (390, 130, 480, 300, (155, 150, 145)),
        (470, 110, 570, 300, (170, 165, 158)),
        (560, 95, 670, 300, (160, 155, 150)),
        (660, 125, 800, 300, (165, 160, 153)),
    ]
    for x0, y0, x1, y1, c in buildings:
        draw.rectangle([x0, y0, x1, y1], fill=c)
        # Windows
        ww, wh = 12, 15
        for wy in range(y0 + 15, y1 - 20, 25):
            for wx in range(x0 + 10, x1 - 10, 22):
                wc = (200, 210, 220) if random.random() > 0.3 else (240, 230, 140)
                draw.rectangle([wx, wy, wx + ww, wy + wh], fill=wc)
    
    # Road
    draw.rectangle([0, 300, 800, 600], fill=(80, 80, 85))
    # Sidewalk/curb
    draw.rectangle([0, 295, 800, 310], fill=(180, 175, 170))
    # Road markings
    for x in range(0, 800, 80):
        draw.rectangle([x, 440, x + 40, 445], fill=(220, 220, 220))
    
    # Trees (partially occluding)
    random.seed(123)
    
    # Tree 1 (left side, in front of cars)
    draw_tree(draw, 150, 200, 120, 70)
    
    # Tree 2 (right side)
    draw_tree(draw, 580, 190, 130, 80)
    
    # Parked cars along the curb
    # Car 1 - partially cut off at left edge
    draw_car(draw, -30, 370, 180, 80, color=(180, 40, 40))
    
    # Car 2 - fully visible but partially behind tree
    draw_car(draw, 200, 375, 170, 75, color=(60, 80, 170))
    
    # Car 3 - in the middle, partially occluded by car 2 and car 4
    draw_car(draw, 370, 370, 160, 75, color=(200, 200, 210))
    
    # Car 4 - overlapping with car 3
    draw_car(draw, 520, 375, 165, 78, color=(40, 40, 45))
    
    # Car 5 - partially cut off at right edge
    draw_car(draw, 720, 370, 180, 80, color=(60, 140, 60))
    
    # Re-draw trees on top for occlusion effect
    draw_tree(draw, 150, 200, 120, 70)
    draw_tree(draw, 580, 190, 130, 80)
    
    # Add a small tree/bush
    draw_tree(draw, 380, 220, 90, 50)
    
    img.save(os.path.join(OUT_DIR, 'det_hard_2.jpg'), quality=95)
    print("Generated det_hard_2.jpg")


# Generate all images
if __name__ == '__main__':
    generate_det_easy_1()
    generate_det_easy_2()
    generate_det_medium()
    generate_det_hard_1()
    generate_det_hard_2()
    print("\nAll 5 detection training images generated successfully!")
