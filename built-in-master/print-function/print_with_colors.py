#!/usr/bin/env python3

# Example of printing text in different 256 colors
for i in range(256):
    print(f"\033[38;5;{i}m{i:3d}\033[0m ", end="")
    if (i + 1) % 16 == 0:
        print()
