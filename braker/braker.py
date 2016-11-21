import os
import subprocess

handbrake_path = 'C:\\Program Files\\Handbrake\\HandBrakeCli.exe'

in_folder = 'C:/etc'
out_folder = 'C:/Data'

preset = 'Roku 1080p30 Surround'
start_at = 'duration:5'

extensions = ('mp4')

def videos_in(folder, recursive=True):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith(extensions):
                yield filename, os.path.join(root, filename)

def get_sub_folder(path, original_folder):
    path = os.path.normpath(path)
    original_folder = os.path.normpath(original_folder)
    head, tail = os.path.split(path)
    _, sub_folders = head.split(original_folder)
    return sub_folders

if __name__ == '__main__':
    for filename, full_path in videos_in(in_folder):
        sub_folder = get_sub_folder(full_path, in_folder)
        folder = os.path.join(out_folder, sub_folder.lstrip('\\/'))
        if not os.path.isdir(folder):
            os.mkdir(folder)
        subprocess.run([handbrake_path,
                        '--preset', preset,
                        '--start-at', start_at,
                        '-i', full_path,
                        '-o', os.path.join(folder, filename)])
