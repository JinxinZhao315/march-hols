import itertools

def gen_passcode(keyword):
    """
	Generates a list of possible permutations of the characters in a string.
    Args:
        keyword: string
            String of characters to generate permutations from

    Returns:
        A list, which contains all possible permutations
    """

    char_list = []
    permu_list2=[]
    keyword.lower()
    for char in keyword:
        char_list.append(char)
    permu_list1 = list(itertools.permutations(char_list))
    for a_list in permu_list1:
        a_list = ''.join(a_list)
        permu_list2.append(a_list)
    return permu_list2


if __name__ == "__main__":
	print("The string is 'Kleen")
	print("\n".join(gen_passcode("Kleen")))

	# Add tests below
