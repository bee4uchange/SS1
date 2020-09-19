size = list(input().split(' '))
height = int(size[0])
width = int(size[1])

for i in range(height):
    if i%2 != 0:
        print(('.|.'*i).center(width,'-'))
print('WELCOME'.center(width,'-'))
for i in reversed(range(height)):
    if i%2 != 0:
        print(('.|.'*i).center(width,'-'))
