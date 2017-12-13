
def run_High_Entropy_Passphrases_1(Passphrases):

    valids = 0
    for idx in xrange(len(Passphrases)):
        valid = True
        pass_idx = Passphrases[idx].split()
        for i in xrange(len(pass_idx)):
            for j in xrange(len(pass_idx)):
                if (pass_idx[i] == pass_idx[j]) and i != j:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valids+=1

    print 'The solution to ' +str(Passphrases) + ' captcha is: \n' + str(valids)

def run_High_Entropy_Passphrases_2(Passphrases):

    valids = 0
    for idx in xrange(len(Passphrases)):
        valid = True
        pass_idx = Passphrases[idx].split()
        for i in xrange(len(pass_idx)):
            for j in xrange(len(pass_idx)):
                if len(pass_idx[i]) == len(pass_idx[j]) and i != j:
                    found_correspondence = 0
                    for i_letter in xrange(len(pass_idx[i])):
                        if (pass_idx[j].count(pass_idx[i][i_letter]) == pass_idx[i].count(pass_idx[i][i_letter])):
                            found_correspondence +=1
                        if found_correspondence == len(pass_idx[i]):
                            valid = False
                            break
            if not valid:
                break
        if valid:
            valids+=1

    print 'The solution to ' +str(Passphrases) + ' captcha is: \n' + str(valids)

def open_file_txt(file_name):
    file = open(file_name, 'r')
    return [line[0:len(line)].replace("\n", "") for line in file.readlines()]

if __name__ == '__main__':
    input = open_file_txt('./file_directory/Day_4.txt')

    run_High_Entropy_Passphrases_1(input)
    run_High_Entropy_Passphrases_2(input)
