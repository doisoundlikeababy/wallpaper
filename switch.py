import os 
from pathlib import Path

raw_path = input("What is the path to the new wallpaper?\n")
path = Path(raw_path)

if(path.exists()):
    os.system('~/.config/polybar/shapes/scripts/pywal.sh ' + str(path))
    os.system(f'dconf write /org/gnome/desktop/background/picture-uri-dark "\'file://{str(path)}\'"') 

    os.system('~/oomox-gtk-theme/change_color.sh -o wallpaper-theme ~/.cache/wal/colors-oomox') 
else:
    print("Oh no!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! The path is wrong!!!!!!!!")
