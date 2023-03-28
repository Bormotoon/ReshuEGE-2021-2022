with open('24.txt', 'r') as f:
    characters = f.read().strip()

# replace all M with "\n"
characters = characters.replace('M', '\n')
print(characters)

# put all lines in characters into a list
characters_list = characters.splitlines()
print(characters_list)

# remove all empty items from characters_list
characters_list = [x for x in characters_list if x]
print(characters_list)

# remove all items where two neighboring chars are the same
characters_list = [x for x in characters_list if not any(x[i] == x[i+1] for i in range(len(x)-1))]
print(characters_list)

# find the longest item in characters_list
longest = max(characters_list, key=len)
print(longest)
print(len(longest))
