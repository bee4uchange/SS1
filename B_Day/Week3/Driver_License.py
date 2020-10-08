def main():
    ques = []
    ques_choice = []
    cor = []
    ans = []

    with open('Ques.txt', encoding='utf-8-sig', mode='r') as f:
        ques = f.readlines()
    ques = [x.strip() for x in ques]

    with open('Ques2.txt', encoding='utf-8-sig', mode='r') as f:
        ques_choice = f.readlines()
    ques_choice = [x.strip() for x in ques_choice]

    with open('Ans.txt', encoding='utf-8-sig', mode='r') as f:
        cor = f.readlines()
    cor = [x.strip() for x in cor]

    check = ['A', 'B', 'C', 'D']
    for i in range(len(ques)):
        print(ques[i])
        print(ques_choice[i])
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
    total_num_wr = 0
    ques_wrong = []
    for i in range(len(ques)):
        if ans[i] != cor[i]:
            total_num_wr += 1
            ques_wrong.append(i + 1)

    total_num_cor = len(ques) - total_num_wr
    print('Số câu đúng là:', total_num_cor)
    print('Số câu sai là:', total_num_wr)
    print('Các câu sai:', ques_wrong)
    if total_num_cor >= 2:
        print('ĐỖ!')
    else:
        print('TẠCH!')


main()
