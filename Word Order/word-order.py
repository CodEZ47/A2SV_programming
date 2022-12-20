# Enter your code here. Read input from STDIN. Print output to STDOUT
def word_counter(words):
    words_dict = {}

    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    print(len(words_dict))
    print(*words_dict.values())

inp = int(input())
words_list = []
for i in range(inp):
    words_list.append(input())
# print(words_list)

word_counter(words_list)
