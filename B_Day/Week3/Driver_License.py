def correct():
    cor = ['C', 'A', 'B', 'D', 'C']
    return cor


def main():
    print('Answer the questions')
    ques = ['1. Cuộc đua xe chỉ được thực hiện khi nào?',
            '2.Người điều khiển phương tiện giao thông đường bộ mà trong cơ thể có chất ma tuý có bị nghiêm cấm hay không?',
            '3.Sử dụng rượu, bia khi lái xe, nếu bị phát hiện thì bị xử lý như thế nào?',
            '4.Theo Luật phòng chống tác hại của rượu, bia, đối tượng nào dưới đây bị cấm sử dụng rượu, bia khi tham gia giao thông?',
            '5.Hành vi điều khiển xe cơ giới chạy quá tốc độ quy định, giành đường, vượt ẩu có bị nghiêm cấm hay không?']

    ques_choice = [
        'A.Diễn ra trên đường phố không có người qua lại.   B.Được người dân ủng hộ.   C.Được cơ quan có thẩm quyền cấp phép.',
        'A.Bị nghiêm cấm.   B.Không bị nghiêm cấm.   C.Không bị nghiêm cấm, nếu có chất ma tuý ở mức nhẹ, có thể điều khiển phương tiện tham gia giao thông.',
        'A.Chỉ bị nhắc nhở.   B.Bị xử phạt hành chính hoặc có thể bị xử lý hình sự tùy theo mức độ vi phạm.   C.Không bị xử lý hình sự.',
        'A.Người điều khiển: Xe ô tô, xe mô tô, xe đạp, xe gắn máy.   B.Người ngồi phía sau người điều khiển xe cơ giới.   C.Người đi bộ.   D.Cả ý 1 và ý 2.',
        'A.Bị nghiêm cấm tuỳ từng trường hợp.   B.Không bị nghiêm cấm.   C.Bị nghiêm cấm.']
    ans = []

    check = ['A', 'B', 'C', 'D']
    for i in range(5):
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
    c = correct()
    for i in range(5):
        if ans[i] != c[i]:
            total_num_wr += 1
            ques_wrong.append(i + 1)

    total_num_cor = 5 - total_num_wr
    print('Số câu đúng là:', total_num_cor)
    print('Số câu sai là:', total_num_wr)
    print('Các câu sai:', ques_wrong)
    if total_num_cor >= 4:
        print('ĐỖ!')
    else:
        print('TẠCH!')


main()
