def read_file_1(path): 
    with open(path, "r") as file:
        lines = file.read().splitlines()
    return lines

def read_file_2(path):
    with open(path, "r") as file:
        content = file.read().strip().split(',')
    return content
    
def read_file_3(path):
    with open(path, "r") as file:
        lines = file.read().splitlines()
        fresh_ranges = []
        available_ids = []
        for l in lines:
            if l == '':
                fresh_ranges = available_ids.copy()
                available_ids = []
                continue
            available_ids.append(l)
        
        fresh_ranges = [(int(s), int(e)) for s, e in (r.split('-') for r in fresh_ranges)]
        available_ids = [int(r) for r in available_ids]

    return fresh_ranges, available_ids

def read_file_4_part1(path): 
    with open(path, "r") as file:
        lines = file.read().splitlines()
        length = len(lines) - 1
        for i in range(length):
            lines[i] = [int(x) for x in lines[i].split()]

        lines[length] = lines[length].split()
        return lines
    
def read_file_4_part2(path): 
    with open(path, "r") as file:
        lines = file.read().splitlines()
        length = len(lines)

        for i in range(length):
            lines[i] = list(lines[i])

        lines = list(zip(*lines))

        new_lines = []
        splitted = []
        for i in lines:
            st = set(i)
            if len(st) == 1 and st.pop() == ' ':
                new_lines.append(splitted)
                splitted = []
                continue
            splitted.append(i)
        new_lines.append(splitted)

        for i in range(len(new_lines)):
            new_new_line = []
            operator = new_lines[i][0][-1]
            first_line = new_lines[i][0][0:-1]
            new_new_line.append(operator)
            new_new_line.append(int(''.join(first_line)))
            for num in new_lines[i][1:]:
                new_new_line.append(int(''.join(num)))

            new_lines[i] = new_new_line

        return new_lines