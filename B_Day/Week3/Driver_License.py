def main():
    ques = []
    ques_choice = []
    cor = []
    ans = []

    # READ DATA FROM FILE
    with open('Ques.txt', encoding='utf-8-sig', mode='r') as f:
        ques = f.readlines()
    ques = [x.strip() for x in ques]

    with open('Ans.txt', encoding='utf-8-sig', mode='r') as f:
        cor = f.readlines()
    cor = [x.strip() for x in cor]

    # PRINT QUESTION AND INPUT ANSWER
    check = ['A', 'B', 'C', 'D']
    total = 1
    for i in range(len(ques)):
        print(ques[i])
        if ques[i] == '':
            total += 1
            while True:
                in_ = input('Câu trả lời của bạn: ')
                in_ = in_.upper()
                if in_.isalpha() == False:
                    print('Điền A,B,C hoặc D')
                    continue
                elif not in_ in check:
                    print('Điền A,B,C hoặc D')
                    continue
                else:
                    break
            ans.append(in_)
            print()
        else:
            continue
    print()
    while True:
        in_ = input('Câu trả lời của bạn: ')
        in_ = in_.upper()
        if in_.isalpha() == False:
            print('Điền A,B,C hoặc D')
            continue
        elif not in_ in check:
            print('Điền A,B,C hoặc D')
            continue
        else:
            break
    ans.append(in_)
    print()
    print(ans)
    # COMPARE ANSWER WITH KEY
    total_num_wr = 0
    ques_wrong = []
    for i in range(total):
        if ans[i] != cor[i][-1:]:
            total_num_wr += 1
            ques_wrong.append(i + 1)

    # CALCULATE TOTAL SCORE AND EVALUATE
    total_num_cor = total - total_num_wr
    print('Số câu đúng là:', total_num_cor)
    print('Số câu sai là:', total_num_wr)
    print('Các câu sai:', ques_wrong)
    if total_num_cor >= 2:
        print('ĐỖ!')
    else:
        print('TẠCH!')


main()
