#! /usr/bin/env python3

import os
import subprocess


import os
import subprocess

def convert_mkv_to_mp4(directory):
    """Converts all .mkv files in the specified directory to .mp4."""
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".mkv"):
            mkv_file = os.path.join(directory, filename)
            mp4_file = os.path.join(directory, f"{os.path.splitext(filename)[0]}.mp4")

            if os.path.exists(mp4_file):
                print(f"Skipping {mkv_file} as {mp4_file} already exists.")
                continue

            try:
                print(f"Converting {mkv_file} to {mp4_file}...")
                subprocess.run([
                    "ffmpeg", "-i", mkv_file, "-c:v", "copy", "-c:a", "copy", mp4_file
                ], check=True)
                print(f"Successfully converted {mkv_file} to {mp4_file}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {mkv_file} to {mp4_file}: {e}")

if __name__ == "__main__":
    convert_mkv_to_mp4("/home/rg/Code/websites/curlew.local/synthesia")
