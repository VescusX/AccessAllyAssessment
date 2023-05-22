def sequences_seen(mins):
    cycles = mins // (60 * 12)
    remainder = mins % (60 * 12)

    seen = 0

    for i in range(0, remainder + 1):
        if i < 60:
            l_s = [1,2]
        else:
            l_s = [int(x) for x in str(i // 60)]
        
        if i % 60 < 10:
            r_s = [0, i % 60]
        else: 
            r_s = [int(y) for y in str(i % 60)]

        digits = l_s + r_s

        is_arithmetic = True

        for j in range(0, len(digits) - 2):
            #If a number is in an arithmatic sequenc it is the average of it's neighbours
            if (digits[j] + digits[j+2]) / 2 != digits[j+1]:
                is_arithmetic = False
        
        if is_arithmetic:
            seen += 1
        
    #Running the program for one full cycle (719) minutes produce 31 arithmatic sequences
    seen += cycles * 31

    return seen


if __name__ == "__main__":
    mins = int(input())

    print(sequences_seen(mins))
 