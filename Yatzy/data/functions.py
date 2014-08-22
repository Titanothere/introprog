def cast_die(list):
    global dies

    for i in range(0, 5):
        if list[i]:
            dies[i] = random.randint(1, 6)

# Tests for die combinations
def test_block1(l, i):
    return l.count(i) * int(i)

def test_block2(l, s):
    if s == "pair":
        for r in range(6, 0, -1):
            if l.count(r) >= 2:
                return r*2
            
        return 0
        
    elif s == "two pairs":
        part1,part2 = 0,0
        for r in range(6, 0, -1):
            if l.count(r) >= 2:
                part1 = 2 * r
                tva = r
            if l.count (r) >= 2 and r != tva:
                part2 = 3 * r
        if part1 != 0 and part2 != 0:
            return part1+part2
        return 0
        
    elif s == "three of a kind":
        for r in range(6, 0, -1):
            if l.count(r) >= 3:
                return r*3
        return 0
        
    elif s == "four of a kind":
        for r in range(6, 0, -1):
            if l.count(r) >= 4:
                return r*4
        return 0
        
    elif s == "full house":
        part1,part2 = 0,0
        for r in range(6, 0, -1):
            if l.count(r) == 2:
                part1 = 2 * r
                tva = r
            if l.count (r) == 3 and r != tva:
                part2 = 3 * r
        if part1 != 0 and part2 != 0:
            return part1+part2
        return 0
    
    elif s == "small straight":
        for r in range(1, 6):
            if l.count(r) == 0:
                return 0
        return 15
        
    elif s == "large straight":
        for r in range(2, 7):
            if l.count(r) == 0:
                return 0
        return 20
        
    elif s == "chance":
        summa = 0
        for i in l:
            summa += i
        return summa
        
    elif s == "yahtzee":
        for r in range(0, 5):
            for i in l:
                if i != r:
                    break
                else:
                    return 50
        return 0
    
    # If string is not valid, return -1
    else:
        return -1