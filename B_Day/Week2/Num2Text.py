def num2text():
    input_ = list(map(str, input('Enter: ').split(",")))
    print(digit(input_))


def digit(input_):
    digit = ["", "nghìn", "triệu", "tỷ"]

    split_ = []
    for i in range(len(input_)):
        split_.append(digit[i])

    out = ''
    for i in range(len(input_)):
        if input_[i] == '000':
            out = out + ""
        else:
            out = out + core(input_[i]) + " " + split_[len(split_) - 1 - i] + " "

    out = out + "đồng chẵn"
    return out


def core(input_):
    count = {"0": "", "1": "một", "2": "hai", "3": "ba", "4": "bốn", "5": "năm", "6": "sáu", "7": "bảy", "8": "tám",
             "9": "chín"}
    out = ''
    if len(input_) == 3:
        if (input_[1] == '1') and (input_[2] != '0'):
            out = out + count[input_[0]] + " trăm" + " mười " + count[input_[2]]
        elif input_[2] == '0' and input_[1] != '0' and input_[1] != '1':
            out = out + count[input_[0]] + " trăm" + " " + count[input_[1]] + " mươi"
        elif input_[1] == '0' and input_[2] != '0':
            out = out + count[input_[0]] + " trăm" + " linh " + count[input_[2]]
        elif (input_[1] != '1') and (input_[2] == '1'):
            out = out + count[input_[0]] + " trăm" + " " + count[input_[1]] + " mươi mốt"
        elif (input_[1] == '1') and (input_[2] == '0'):
            out = out + count[input_[0]] + " trăm" + " mười"
        elif (input_[1] == '0') and (input_[2] == '0'):
            out = out + count[input_[0]] + " trăm"
        elif (input_[0] == '0') and (input_[1] == '0') and (input_[2] == '0'):
            out = out + ""
        else:
            out = out + count[input_[0]] + " trăm" + " " + count[input_[1]] + " mươi " + count[input_[2]]
        if (input_[1] != '0') and (input_[2] == '5'):
            out = out.replace(" năm", " lăm")

    if len(input_) == 2:
        if (input_[0] == '1') and (input_[1] == '0'):
            out = out + "mười"
        elif (input_[0] == '1') and (input_[1] != '0'):
            out = out + "mười " + count[input_[1]]
        elif (input_[0] != '1') and (input_[1] == '0'):
            out = out + count[input_[0]] + " mươi"
        else:
            out = out + count[input_[0]] + " mươi " + count[input_[1]]
        if (input_[0] != '0') and (input_[1] == '5'):
            out = out.replace(" năm", " lăm")

    if len(input_) == 1:
        out = out + count[input_[0]]

    return out


num2text()
