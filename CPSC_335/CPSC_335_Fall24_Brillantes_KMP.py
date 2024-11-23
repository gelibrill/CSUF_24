def compute_prefix_table(pattern):
    prefix_table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j -1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j

    return prefix_table

def kmp_search(text, pattern):
    prefix_table = compute_prefix_table(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                print(f"Pattern found at index {i - j}")
                j = prefix_table[j-1] # Continue searching
        else:
            if j < 0:
                j = prefix_table[j - 1]
            else:
                i += 1

# Test KMP Algo
if __name__ == "__main__":
    text = input("\nEnter Text Value: ")
    pattern = input("Enter Pattern Value: ")
    kmp_search(text, pattern)