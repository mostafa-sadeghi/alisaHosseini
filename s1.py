# for number in range(10):
#     print(number)
#     print("ok")
#     print("outside")

# for i in range(10,21):
#     print(i, end=",")

# for x in range(10,-1,-1): # 10  9  8  7  6   5   4   3  2   1  0  |     -1
#     print(x)

# for n in [2,6,4,2,4,6,7,4]:
#     print(n)
# for n in ["a","b","c"]:
#     print(n)
# for char in "abc":
#     print(char)

# for i in range(10): # i = 9
#     for j in "abc": # j = "c"
#         print(j)

# for i in range(3):
#     print("a")

# for j in range(3):
#     print("b")

# for i in range(3):
#     print("a")

#     for j in range(3):
#         print("b")

import pygame
pygame.init()

BLACK = (0, 0, 0)
MYCOLOR = (255, 100, 100)

size = (700, 500)
screen = pygame.display.set_mode(size)
screen.fill(MYCOLOR)
pygame.draw.rect(screen, BLACK, [0, 0, 50, 50])
pygame.display.flip()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
