#! /usr/bin/env python3

import os

# Path to the symlink folder
video_folder = "synthesia"
output_file = "index.html"


def list_videos(folder):
    """
    List all video files in the given folder.
    """
    try:
        # Filter for files with common video extensions
        video_extensions = ".mp4"
        return sorted(file for file in os.listdir(folder) if file.endswith(video_extensions))
    except FileNotFoundError:
        print(f"Folder '{folder}' not found.")
        return []


def generate_html(video_files):
    """
    Generate an HTML template with video tags for each video file.
    """
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Curlew</title>


        <link rel="stylesheet" href="style.css">

    </head>
    <body>
        <h1>Curlew</h1>

        <quote>
            Hearing his voice, a god who had made the curlew would almost instantly want to remake himself as the thing he had made.

            Universes he couldn’t call into being with a human voice he could call into being with the voice of a curlew.
        </quote>

        {video_tags}
    </body>
        <script src="./index.js"></script>
    </html>
    """

    video_tags = ""
    for video in video_files:
        video_tags += f"""
        <div>
            <h2>{video}</h2>
            <video preload="none" controls width="640">
                <source src="{video_folder}/{video}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        """

    return html_template.format(video_tags=video_tags)


def main():
    video_files = list_videos(video_folder)
    if not video_files:
        print("No videos found.")
        return

    html_content = generate_html(video_files)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML file generated: {output_file}")


if __name__ == "__main__":
    main()
