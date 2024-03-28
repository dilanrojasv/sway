# Imports
import subprocess
import os

# Get Volume
def get_volume_info():
        result = subprocess.run(['pamixer', '--get-volume'], capture_output=True, text=True, check=True)
        volume_info = result.stdout.strip()
        return volume_info

# Get mute info
def get_mute_info():
        mute = subprocess.run(['pamixer', '--get-mute'], capture_output=True, text=True, check=True)
        mute_info = mute.stdout.strip()
        return mute_info

# States
volume = get_volume_info()
mute = get_mute_info()

# Path to icons
icon = os.path.expanduser('~/.local/share/icons/fontawesome/volume.png ')
icon_muted = os.path.expanduser('~/.local/share/icons/fontawesome/volume_mute.png ')

# Notification
if mute == 'false':
    # Unmuted
    os.system("dunstify -a 'volume' -r 9993 -u low -h int:value:"+volume +" -i " + icon + volume + "% -t 1500")
    # Play a volume test sound
    os.system("play /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga")
else:
    # Muted 
    os.system("dunstify -a 'volume' -r 9993 -u low -h int:value:"+volume +" -i " + icon_muted + volume + "% -t 1500")
