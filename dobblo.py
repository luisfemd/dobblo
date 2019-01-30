
res=[]

def init_game(num, sims):
    rng = num - 1
    res.append(list(sims[0 : num]))
    # sims[num : (num * num) - num + 1]

    m = []
    e = sims[0]
    for i in range(rng):
        r = []
        for j in range(rng):
            r.append(sims[i * rng + j + num])
        m.append(r)
        r.append(e)
        res.append(r)

    for i in range(rng):
        m = iterate(m, rng, sims[i + 1])
    return res

def iterate(m, s, e):
    n = []
    for i in range(s):
        r = []
        for j in range(s):
            r.append(m[j][(i + j) % s])
        n.append(r)
        r.append(e)
        res.append(r)
    return n

def main():
    #sims = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num = 8
    sims = range(57)
    ret = init_game(num, sims)
    print(ret)

if __name__ == '__main__':
    main()
