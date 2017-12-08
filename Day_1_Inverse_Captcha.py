from aux import data_reader as reader

def run_Inverse_Captcha_1(input_captcha):

    res_sum = 0
    for idx in xrange(len(input_captcha)):
        current_number = int(input_captcha[(idx+1)%len(input_captcha)])
        previous_number = int(input_captcha[idx])
        if current_number == previous_number:
            res_sum +=current_number

    print 'The solution to ' +str(input_captcha) + ' captcha is: \n' + str(res_sum)

def run_Inverse_Captcha_2(input_captcha):

    res_sum = 0
    num_of_digits = len(str(input_captcha))
    for idx in xrange(num_of_digits):
        current_number = int(str(input_captcha)[idx])
        previous_number = int(str(input_captcha)[(idx+num_of_digits/2)%num_of_digits])
        if current_number == previous_number:
            res_sum +=current_number

    print 'The solution to ' +str(input_captcha) + ' captcha is: \n' + str(res_sum)

if __name__ == '__main__':
    input = reader.open_file_txt('./file_directory/Day_1.txt')

    run_Inverse_Captcha_1(input)

    run_Inverse_Captcha_2(input)