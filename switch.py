import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='A wallpaper switcher for GNOME')

parser.add_argument('path', type=str, help='The path to the wallpaper')
args = parser.parse_args()

raw_path = args.path
path = Path(raw_path)

if(path.exists()):
    os.system('~/.config/polybar/shapes/scripts/pywal.sh ' + str(path))
    os.system(f'dconf write /org/gnome/desktop/background/picture-uri-dark "\'file://{str(path)}\'"') 

    os.system('~/oomox-gtk-theme/change_color.sh -o wallpaper-theme ~/.cache/wal/colors-oomox') 
else:
    print("Oh no!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! The path is wrong!!!!!!!!")
