def friend(x):
    friends = []

    for i in range(0, len(x)):
        word = x[i]

        if len(word) == 4: 
            friends.append(word)

    return friends

print(friend(["Ryan", "Kieran", "Mark"]))