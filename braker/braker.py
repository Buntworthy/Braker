#!venv/bin/python

import click
import os
import subprocess

handbrake_path = 'C:\\Program Files\\Handbrake\\HandBrakeCli.exe'

DEFAULT_PRESET = 'Roku 1080p30 Surround'
DEFAULT_START = 'duration:5'

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

def convert(in_folder, out_folder, preset, start_at):
    print('Starting conversion')
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

@click.command()
@click.argument('input_path',
    type=click.Path(
        exists=True,
        file_okay=False, # TODO make and option for files
    ))
@click.argument('output_path',
    type=click.Path(
        file_okay=False,
        writable=True
    ))
@click.option('--preset', default=DEFAULT_PRESET)
@click.option('--start_at', default=DEFAULT_START)
def cli(input_path, output_path, preset, start_at):
    convert(input_path, output_path, preset, start_at)
