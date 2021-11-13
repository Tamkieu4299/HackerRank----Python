def minion_game(string):
    string_ = string.lower()
    consonants_ = ["b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowels_ = ["u", "a", "o", "e", "i"]
    stuart_ = []
    kevin_ = []
    #loop in string_
    for i in range(len(string_)):

        #consonants
        for conso_var_ in consonants_:
            if string_[i] == conso_var_:
                conso_var_index = i
                for z in range(len(string_) - conso_var_index):
                    stuart_.append(string_[conso_var_index: conso_var_index + z + 1])

        #vowels
        for vow_var_ in vowels_:
            if string_[i] == vow_var_:
                vow_var_index = i
                for z in range(len(string_) - vow_var_index):
                    kevin_.append(string_[vow_var_index: vow_var_index + z + 1])

    #calculate the point
    sum_stuart = len(stuart_)
    sum_kevin = len(kevin_)

    #print the winner
    if sum_stuart > sum_kevin:
        print("Winner is: Stuart", sum_stuart)
    elif sum_stuart == sum_kevin:
        print("Raw\n", "Stuart =>", sum_stuart, "Kevin =>", sum_kevin)
    else:
        print("Winner is: Kevin", sum_kevin)

    return sum_stuart, sum_kevin

#Main function:
minion_game(string="Banana")



#Their solution
vow = "AEIOU"
slen = len(string)
tsub = int(slen * (slen + 1) / 2)
k = sum(slen - i for i in range(slen) if string[i] in vow)
s = tsub - k

if s > k: print(f"Stuart {s}")
elif s < k: print(f"Kevin {k}")
else: print("Draw")