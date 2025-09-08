# Debian Package Statistics Tool

## Overview

This tool fetches and analyzes the Debian Contents index for a given architecture. 
It outputs the top 10 packages with the most files.

## How to use:

```bash
./package_statistics.py amd64
```

## Thought process:

Looking into this problem, it was easy enough to understand what was required, but I am not experienced in file readings. So, to start, I took my time with research. First, I looked deeply into the requirements to fully understand what was being asked. I then looked into different Python packages that can read/intake files, as well as different parsing strategies. 

Next, I planned out what functions/structure I wanted my code to have. I wrote the headers to each function I thought I'd need. Finally, I started implementing code - regularly testing to ensure the output was expected.

This entire process took me around 3-4 hours
##
