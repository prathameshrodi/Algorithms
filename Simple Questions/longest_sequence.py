def find_longest_sequence(string):
    """
    Find the longest sequence of consecutive repeating characters in a string.
    
    Args:
        string (str): Input string to analyze
        
    Returns:
        tuple: (character, length, start_index) of the longest sequence
    """
    if not string:
        return None, 0, -1
    
    max_length = 1
    current_length = 1
    max_char = string[0]
    max_start_index = 0
    current_start_index = 0
    
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_char = string[i]
                max_start_index = current_start_index
        else:
            current_length = 1
            current_start_index = i
    
    return max_char, max_length, max_start_index

def main():
    # Test cases
    test_strings = [
        "AABBBCCCC",
        "Hello",
        "111222333",
        "",
        "AAAA"
    ]
    
    for test_str in test_strings:
        char, length, start_index = find_longest_sequence(test_str)
        if char is not None:
            print(f"String: {test_str}")
            print(f"Longest sequence: '{char}' repeated {length} times starting at index {start_index}")
            print(f"Sequence: {test_str[start_index:start_index+length]}")
            print("-" * 50)

if __name__ == "__main__":
    main()
