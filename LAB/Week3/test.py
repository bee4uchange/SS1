with open('Ans.txt', encoding='utf-8-sig', mode='r') as f:
    cor = f.readlines()
cor = [x.strip() for x in cor]

print(cor)
