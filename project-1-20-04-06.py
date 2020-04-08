T=int(input())
for i in range(T):
    N,Q=map(int,input().split())
    S=[]
    Top=[]
    for j in range(N+1):
        S.append([])
        Top.append(-1)
    for j in range(Q):
        nums = list(map(int, input().split()))
        if nums[0]==1 :
            S[nums[1]].append(nums[2])
            Top[nums[1]]=Top[nums[1]]+1
        elif nums[0]==2 :
            if Top[nums[1]]==-1 :
                print("EMPTY")
            else :
                print(S[nums[1]][Top[nums[1]]])
                S[nums[1]].pop()
                Top[nums[1]]=Top[nums[1]]-1
        elif nums[0]==3 :
            S[nums[1]]=S[nums[1]]+S[nums[2]]
            Top[nums[1]]=len(S[nums[1]])-1
            S[nums[2]].clear()
            Top[nums[2]]=-1