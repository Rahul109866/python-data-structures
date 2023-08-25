string1 = "Public Relations"
string2 = "crap built on lies"


def anagram_checker(s1, s2):
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()

    s1_dict = {}
    for i in s1:
        if i not in s1_dict:
            s1_dict[i] = s1.count(i)

    s2_dict = {}
    for i in s2:
        if i not in s2_dict:
            s2_dict[i] = s2.count(i)

    if s1_dict == s2_dict:
        return True

    else:
        return False
    
print(anagram_checker(string1,string2))
