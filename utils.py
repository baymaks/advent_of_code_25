def read_file_1(path): 
    with open(path, "r") as file:
        lines = file.read().splitlines()
    return lines

def read_file_2(path):
    with open(path, "r") as file:
        content = file.read().strip().split(',')
    return content
    
