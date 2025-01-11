# utils.py
import sys     # Import system module for writing to console
import time    # Import time module for creating delays

def print_with_delay(text, delay=0.03):
    """This function prints text character by character with a time delay
    
    Parameters:
    - text: The string to be printed
    - delay: Time in seconds to wait between each character (default 0.03)
    """
    for char in text:                    # Loop through each character in the text
        sys.stdout.write(char)           # Write a single character to the console
        sys.stdout.flush()               # Force the character to display immediately
        time.sleep(delay)                # Pause for the specified delay time
    print()                             # Add a newline at the end of the text
