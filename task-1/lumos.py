runes = "GhJkLmNspQorStUvWx"

def lumos(runes) :
    i = 0
    lumos = {'l','u','m','o','s'}
    while(i < len(runes) and lumos):
        if runes[i].lower() in lumos :
            lumos.remove(runes[i].lower())
        i += 1
    if (lumos):
        return -1
    else:
        return i

print(lumos(runes))