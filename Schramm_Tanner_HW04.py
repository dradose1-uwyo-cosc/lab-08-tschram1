# Tanner Schramm
# COSC 1010
# Homework 4
# Lab section 10
# 11/11/2024
# Sources, help given by, help given: Patrick was able to help me with this code and it works. 
# Chat GPT was used to help me get a start with my code. I looked up how to start this project and I got it to work once I learned from chat. 
# I was also given help by Colter to get it to run. 

from pathlib import Path

path=Path('prompt.txt')
created_file=Path('out_text')
created_file.write_text

with open('prompt.txt', 'r') as infile, open('out.txt', 'w') as outfile:
    for line in infile:
        pairs=line.strip().split('\t')
        output_line=""
        for pair in pairs:
            key, value=pair.split(':')
            count=int(value)
            if key=='w':
                output_line+=' '*count
            elif key=='*':
                output_line+='*'*count
        outfile.write(output_line + '\n')