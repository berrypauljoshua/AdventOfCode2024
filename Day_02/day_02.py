p1_answer = 0
p2_answer = 0

fail_list = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        report = line.rstrip().split()

        rule_increasing = all(int(curr_level) < int(next_level) <= int(curr_level)+3 for curr_level, next_level in zip(report, report[1:]))
        rule_decreasing = all(int(curr_level) > int(next_level) >= int(curr_level)-3 for curr_level, next_level in zip(report, report[1:]))

        p1_answer += rule_increasing or rule_decreasing

print(f"[PART ONE ANSWER] Total Safe Reports {p1_answer}") # Correct!
print(f"[PART TWO ANSWER] Total Safe Reports (Dampened) {p2_answer}") # Not Completed!