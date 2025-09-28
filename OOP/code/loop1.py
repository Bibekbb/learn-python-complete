import sys

def filter_lines(lines, filtered):
    if not lines:
        return filtered
    line = lines[0].strip()
    if line:
        return filter_lines(lines[1:], filtered + [line])
    else:
        return filter_lines(lines[1:], filtered)

def calculate_sum(numbers, acc):
    if not numbers:
        return acc
    num = numbers[0]
    if num <= 0:
        return calculate_sum(numbers[1:], acc + num ** 4)
    else:
        return calculate_sum(numbers[1:], acc)

def process_test_cases(N, lines, idx, results):
    if N == 0:
        return results
    if idx >= len(lines):
        return results + [-1] * N
    X_line = lines[idx]
    idx += 1
    try:
        X = int(X_line)
    except ValueError:
        new_results = results + [-1]
        if idx < len(lines):
            idx += 1
        return process_test_cases(N - 1, lines, idx, new_results)
    
    if idx >= len(lines):
        return results + [-1] * N
    
    Yn_line = lines[idx]
    idx += 1
    Yn_parts = Yn_line.split()
    
    if len(Yn_parts) != X:
        return process_test_cases(N - 1, lines, idx, results + [-1])
    
    try:
        Yn_numbers = list(map(int, Yn_parts))
    except ValueError:
        return process_test_cases(N - 1, lines, idx, results + [-1])
    
    total = calculate_sum(Yn_numbers, 0)
    return process_test_cases(N - 1, lines, idx, results + [total])

def print_results(results):
    if not results:
        return
    print(results[0])
    print_results(results[1:])

def main():
    lines = sys.stdin.read().splitlines()
    filtered_lines = filter_lines(lines, [])
    if not filtered_lines:
        return
    N = int(filtered_lines[0])
    results = process_test_cases(N, filtered_lines, 1, [])
    print_results(results)

if __name__ == "__main__":
    main()