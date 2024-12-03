import re

p1_answer = 0
p2_answer = 0

enable_instruction = True

regex = re.compile('mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))')

with open('Day_03/input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        f_line = line.rstrip()

        for capture in regex.findall(f_line):
            if capture[0] != '' and capture[1] != '':
                p1_answer += int(capture[0]) * int(capture[1])

with open('Day_03/input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        f_line = line.rstrip()

        for capture in regex.findall(f_line):
            if capture[2] != '':
                enable_instruction = True

            if capture[3] != '':
                enable_instruction = False

            if enable_instruction and capture[0] != '' and capture[1] != '':
                p2_answer += int(capture[0]) * int(capture[1])
            

print(f"[PART ONE ANSWER] Sum of Multiplication Instructions {p1_answer}") # Correct!
print(f"[PART ONE ANSWER] Sum of Enabled Multiplication Instructions {p2_answer}") # Correct!