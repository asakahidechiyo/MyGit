def initUlamSeq(n):
    vUlam=[1,2]
    if n<=2:
        return vUlam
    nStandby=3
    while(nStandby<n):
        nCnt=0
        for i in range(0,len(vUlam)):
            for j in range(i+1,len(vUlam)):
                if vUlam[i]+vUlam[j]==nStandby:
                    nCnt+=1
                    print(f"{vUlam[i]} + {vUlam[j]} = {nStandby}, cnt is {nCnt}")
        if nCnt==1:
            print(f"---{nStandby} is an Ulam number!---")
            vUlam.append(nStandby)
        else:
            print(f"{nStandby} is not an Ulam number")
        nStandby+=1
    return vUlam

n=input("Enter n for Ulam(n):")
vUlam=initUlamSeq(int(n))
print(vUlam)
input("Enter to continue...")