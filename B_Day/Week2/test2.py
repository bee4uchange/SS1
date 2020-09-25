input_ = list(map(str,input('Enter: ').split(",")))

donvi1 = ["đồng chẵn", "ngàn", "triệu", "tỷ"]
so = {"0": "", "1": "một", "2": "hai", "3": "ba", "4": "bốn", "5": "năm", "6": "sáu", "7": "bảy", "8": "tám", "9": "chín", "10": "mười"}
donvi2 = ["", "mươi", "trăm"]
donvi3 = ["trăm", "mươi", ""]

part = ''

split_ = []
for i in range(len(input_)):
    split_.append(donvi1[i])





for i in range(len(input_)):
    split__ = donvi2[0:len(input_[i])]
    print(split__)





    if input_[i].endswith("00"):
        part = part + so[input_[i][0]] + " " + split__[(len(split__) - 1) - 0]

    elif input_[i].endswith("1"):
        for j in range(len(input_[i])-1):
            part = part + so[input_[i][j]] + " " + split__[(len(split__)-1)-j] + " "
        part = part + "mốt" + " "
    else:
        for j in range(len(input_[i])):
            part = part + so[input_[i][j]] + " " + split__[(len(split__)-1)-j] + " "
    part = part + " " + split_[len(split_)-1-i] + " "





if "một mươi" in part:
    part = part.replace("một mươi","mười")
elif "một mươi mốt" in part:
    part = part.replace("một mươi mốt", "mười một")
elif "mười mốt" in part:
    part = part.replace("mười mốt", "mười một")
elif "trăm ngàn  trăm đồng chẵn" in part:
    part = part.replace("trăm ngàn  trăm đồng chẵn", "trăm ngàn đồng chẵn")
elif "   ngàn  trăm đồng chẵn " in part:
    part = part.replace("   ngàn  trăm đồng chẵn ", " ngàn đồng chẵn")
if "mười năm" in part:
    part = part.replace("mười năm","mười lăm")
print(part)
