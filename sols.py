from utils import *
import re
import time
from itertools import chain

class Day1Solution:
    
    lines = read_file_1("inputs/input_day1.txt")
    # lines = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

    def solution_part1(self, lines):
        
        pos = 50
        total_zero = 0

        for line in lines:
            dir = line[0]
            steps = int(line[1:])

            if dir == 'L': 
                pos = (100  + (pos - steps)) % 100 
            elif dir == 'R':
                pos = (100  + (pos + steps)) % 100

            if pos == 0:
                total_zero += 1

        return total_zero

    def solution_part2(self, lines):
        
        pos = 50
        total_zero = 0

        for line in lines:
            dir = line[0]
            steps = int(line[1:])

            into = 0 

            if dir == 'L':
                into_temp = abs((pos - steps - 1) // 100) 
                # starting zero does not count as it was already counted in the previous step
                # however, count it if we arrive at zero
                into = into_temp if pos != 0 else into_temp - 1 
                pos = (100  + (pos - steps)) % 100 
            else:
                into = (pos + steps) // 100 
                pos = (100  + (pos + steps)) % 100 

            total_zero += into

        return total_zero
    
    def run(self):
        print("--------------------------------------")
        print("--------------- Day 1 ----------------")
        print("--------------------------------------")
        start1 = time.time()
        result_part1 = self.solution_part1(self.lines)
        end1 = time.time() - start1
        print(f">   Part 1 Result: {result_part1}")

        start2 = time.time()
        result_part2 = self.solution_part2(self.lines)
        end2 = time.time() - start2
        print(f">   Part 2 Result: {result_part2}")
        print(f">   Timing: {end1 + end2}")
        print("--------------------------------------")
        print("\n")

class Day2Solution:
        
    lines = read_file_2("inputs/input_day2.txt")
    # lines = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224", "1698522-1698528","446443-446449","38593856-38593862","565653-565659", "824824821-824824827","2121212118-2121212124"]

    def split_string(self, s, n):
        mid = len(s) // n
        return s[:mid], s[mid:]

    def solution_part1(self, lines):
        total = 0
        for line in lines:
            a, b = map(int, line.split('-', 1))
            for i in range(a, b + 1):
                if len(str(i)) % 2 == 0:
                    left, right = self.split_string(str(i), 2)
                    if left == right:
                        total += i
        return total

    def solution_part2(self, lines):
        total = 0
        for line in lines:
            a, b = map(int, line.split('-', 1))
            for i in range(a, b + 1):
                for k in range(1, len(str(i)) // 2 + 1):
                    if len(str(i)) % k != 0:
                        continue
                    pattern = rf'(.{{{k}}})\1+'
                    if re.fullmatch(pattern, str(i)) is not None:
                        total += i
                        break
        return total

    def run(self):
        print("--------------------------------------")
        print("--------------- Day 2 ----------------")
        print("--------------------------------------")
        start1 = time.time()
        result_part1 = self.solution_part1(self.lines)
        end1 = time.time() - start1
        print(f">   Part 1 Result: {result_part1}")

        start2 = time.time()
        result_part2 = self.solution_part2(self.lines)
        end2 = time.time() - start2
        print(f">   Part 2 Result: {result_part2}")
        print(f">   Timing: {end1 + end2}")
        print("--------------------------------------")
        print("\n")

class Day3Solution:
        
    lines = read_file_1("inputs/input_day3.txt")
    # lines = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

    def solution_part1(self, lines):
        total_joltage = 0

        for line in lines:
            
            start = 0 
            end = 1
            length = len(line) - 1

            for i in range(1, length):
                if int(line[i]) > int(line[start]):
                    start = i
                    end = i + 1
                elif int(line[i]) > int(line[end]):
                    end = i
            end = length if int(line[length]) > int(line[end]) else end

            number = int(line[start] + line[end])
            total_joltage += number

        return total_joltage

    def solution_part2(self, lines):
        total_joltage = 0
        # the largest 12 digit number i can make 
        # from an n digit number reading only from left to right    
        for line in lines:
            start = 0
            biggest_joltage = ''
            for i in range(11, -1, -1):
                for j in range(start, len(line) - i):
                    if int(line[j]) > int(line[start]):
                        start = j
                biggest_joltage += line[start]
                start += 1
            
            total_joltage += int(biggest_joltage)

        return total_joltage

    def run(self):
        print("--------------------------------------")
        print("--------------- Day 3 ----------------")
        print("--------------------------------------")
        start1 = time.time()
        result_part1 = self.solution_part1(self.lines)
        end1 = time.time() - start1
        print(f">   Part 1 Result: {result_part1}")

        start2 = time.time()
        result_part2 = self.solution_part2(self.lines)
        end2 = time.time() - start2
        print(f">   Part 2 Result: {result_part2}")
        print(f">   Timing: {end1 + end2}")
        print("--------------------------------------")
        print("\n")

class Day4Solution:
        
    lines = read_file_1("inputs/input_day4.txt")
    # lines =  ['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.',]

    def check_body(self, new_lines):

        counts = 0
        points = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        for r in range(1, len(new_lines) - 1):
            for c in range(1, len(new_lines[r]) - 1):
                if new_lines[r][c] != '@':
                    continue
                
                total = 0
                for dr, dc in directions:
                    if new_lines[r + dr][c + dc] == '@':
                        total += 1

                if total < 4:
                    points += [(r, c)]
                counts += 1 if total < 4 else 0
        
        for (x, y) in points:
            new_lines[x][y] = 'x'          

        return counts, new_lines


    def solution_part1(self, lines):

        new_lines = [list('.'*len(lines[0]))] + [list(line) for line in lines] + [list('.'*len(lines[0]))]
        for line in new_lines:
            line.insert(0, '.')
            line.append('.')

        x, _ = self.check_body(new_lines)
        return x

    def solution_part2(self, lines):

        new_lines = [list('.'*len(lines[0]))] + [list(line) for line in lines] + [list('.'*len(lines[0]))]
        for line in new_lines:
            line.insert(0, '.')
            line.append('.')

        count = 0
        while True:
            x, new_lines = self.check_body(new_lines)
            if x == 0:
                break
            count += x

        return count


    def run(self):
        print("--------------------------------------")
        print("--------------- Day 4 ----------------")
        print("--------------------------------------")
        start1 = time.time()
        result_part1 = self.solution_part1(self.lines)
        end1 = time.time() - start1
        print(f">   Part 1 Result: {result_part1}")

        start2 = time.time()
        result_part2 = self.solution_part2(self.lines)
        end2 = time.time() - start2
        print(f">   Part 2 Result: {result_part2}")
        print(f">   Timing: {end1 + end2}")
        print("--------------------------------------")
        print("\n")

class Day5Solution:
        
    fresh_ranges, available_ids = read_file_3("inputs/input_day5.txt")
    # fresh_ranges = [(16, 20), (3, 5), (10, 14), (12, 18)]
    # available_ids = [ 1, 5, 8, 11, 17, 32 ]


    def solution_part1(self, fresh_ranges, available_ids):
        fresh_set = [range(s, e + 1) for s, e in fresh_ranges] 
        count = 0
        for id in available_ids:
            for fresh in fresh_set:
                if id in fresh:
                    count += 1
                    break
        return count

    def solution_part2(self, fresh_ranges, available_ids):
        fresh_rangess = sorted(fresh_ranges, key=lambda r: r[0]) 
        start = fresh_rangess[0]
        new_fresh_ranges = []
        for fresh in fresh_rangess[1:]:
            if start[1] >= fresh[0] and start[1] <= fresh[1]:
                start = (start[0], fresh[1])
            elif start[1] < fresh[0]:
                new_fresh_ranges.append(start)
                start = fresh
        
        new_fresh_ranges.append(start) 
        
        return sum([e - s + 1 for s, e in new_fresh_ranges])
                
        

    def run(self):
        print("--------------------------------------")
        print("--------------- Day 5 ----------------")
        print("--------------------------------------")
        start1 = time.time()
        result_part1 = self.solution_part1(self.fresh_ranges, self.available_ids)
        end1 = time.time() - start1
        print(f">   Part 1 Result: {result_part1}")

        start2 = time.time()
        result_part2 = self.solution_part2(self.fresh_ranges, self.available_ids)
        end2 = time.time() - start2
        print(f">   Part 2 Result: {result_part2}")
        print(f">   Timing: {end1 + end2}")
        print("--------------------------------------")
        print("\n")

class Day6Solution:
        
    # lines = read_file_1("inputs/input_day6.txt")
    lines = []

    def solution_part1(self, lines):
        pass 

    def solution_part2(self, lines):
        pass

    def run(self):
        print("--------------------------------------")
        print("--------------- Day 6 ----------------")
        print("--------------------------------------")
        start1 = time.time()
        result_part1 = self.solution_part1(self.lines)
        end1 = time.time() - start1
        print(f">   Part 1 Result: {result_part1}")

        start2 = time.time()
        result_part2 = self.solution_part2(self.lines)
        end2 = time.time() - start2
        print(f">   Part 2 Result: {result_part2}")
        print(f">   Timing: {end1 + end2}")
        print("--------------------------------------")
        print("\n")

# Day1Solution().run()
# Day2Solution().run()
# Day3Solution().run()
# Day4Solution().run()
Day5Solution().run()
# Day6Solution().run()
