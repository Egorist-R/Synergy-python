import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    numbers = input_data[1:n+1]
    for num in reversed(numbers):
        print(num)

if __name__ == '__main__':
    main()
