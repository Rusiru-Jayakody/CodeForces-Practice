t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    xk,yk = map(int, input().split())
    xq,yq = map(int, input().split())
    set_k = set()
    set_q = set()

    for i, j in [(a,b),(b,a),(a,-b),(b,-a),(-a,b),(-a,-b),(-b,a),(-b,-a),]:
        set_k.add((xk+i,yk+j))
        set_q.add((xq+i,yq+j))
    
    print(len(set_k & set_q))