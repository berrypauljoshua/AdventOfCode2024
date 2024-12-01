l_list = []
r_list = []
p1_answer = 0
p2_answer = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        f_line = line.rstrip().split()
        l_list.append(int(f_line[0]))
        r_list.append(int(f_line[1]))

for item in zip(sorted(l_list), sorted(r_list), strict=True):
    p1_answer += abs(item[0] - item[1])
    p2_answer += item[0] * r_list.count(item[0])

print(f"[PART ONE ANSWER] Total Distance {p1_answer}") # Correct!
print(f"[PART TWO ANSWER] Similarity Score {p2_answer}") # Correct!