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