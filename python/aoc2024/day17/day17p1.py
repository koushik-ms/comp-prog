"""
Register A: 46187030
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0

2,4, -> reg A mod 8 -> ?? -> B
1,5, -> B xor 5 -> ? -> B=?
7,5, -> reg A/(2^reg B) -> 46187030/1 -> 46187030 -> C=46187030
0,3, -> reg A/(2^3) -> 46187030/8 -> 5773378 -> A=5773378
4,0, -> reg B XOR reg C -> 0 ^ 46187030 -> B=46187030
1,6, -> reg B XOR 6 -> 46187030 ^ 6 -> 46187024 -> B=46187024
5,5, -> OUT reg B mod 8 -> 46187024 mod 8 -> OUT 0
3,0 -> jump 0 unless reg A == 0
"""

A = 46187030
B = 0
C = 0
out=[]
while A:
    B = A % 8 # 2,4
    B = B ^ 5 # 1, 5
    C = A // (2 ** B) # 7, 5
    A = A // 8 # 0, 3
    B = B ^ C # 4, 0
    B = B ^ 6 # 1, 6
    print(f"{B % 8}, A -> {A}") # 5, 5
    out.append(B%8)

ans=",".join(map(str, out))
print(ans)
