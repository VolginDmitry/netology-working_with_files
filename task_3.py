import os

file_names = ['1.txt', '2.txt', '3.txt']  

file_info = []

for file_name in file_names:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        file_info.append((file_name, line_count, lines))

file_info.sort(key=lambda x: x[1]) 

with open('merged_result.txt', 'w') as merged_file:
    for file_name, line_count, lines in file_info:
        merged_file.write(f"{file_name}\n{line_count}\n")
        merged_file.writelines(lines)
        merged_file.write("\n")
 
with open('merged_result.txt', 'r') as merged_file:
    result_lines = [line for line in merged_file.readlines() if line.strip() != '']

with open('merged_result.txt', 'w') as merged_file:
    merged_file.writelines(result_lines)