import sys
import math
import time
sys.stdin = open("input.in", 'r')
input = sys.stdin.read
T = int(input())

class binary:
    def __init__(self, n):
        self.tree = [0] * (n + 2)
        self.depth = 1
        self.n = n


    def build(self, i = 1):
        if i > self.n:
            return

        self.build(i * 2)
        self.tree[i] = self.depth
        self.depth += 1
        self.build(i * 2 + 1)


    def search(self):
        target = int(self.n / 2) # Tq 2번 노드에 저장된 값으로 나누고 있어서 1시간동안 답이 안나옴
        return print(self.tree[1], self.tree[target])

for k in range(1, T+1):
    start = time.time()
    N = int(input())
    tree = binary(N)
    tree.build()
    print(f'#{k}', end = ' ')
    tree.search()
    end = time.time()
    print(f'{end-start:.5f} sec')
