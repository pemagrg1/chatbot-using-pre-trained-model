
import matplotlib.pyplot as plt

def getdata(filepath):
    f = open(filepath,"r")
    st = f.readlines()
    numlist=[]
    print(len('test-step-20')) #../SMF/ckpt\
    for i in range(1000):
        numlist.append('test-step-'+str(i))

    print(numlist)
    flag=0
    bleu=[]
    brevity_penalty=[]
    rouge1=[]
    rougeL=[]
    epochlist=[]
    for i in st:
        if (i[-31:-16]=='../SMF/ckpt' or i[-30:-15]=='../SMF/ckpt') and 'valid-step-' in i: #(i[-14:-1] in numlist or (i[-13:-1] in numlist)) :
            epoch = i[-4:-1]
            if epoch[0]!='-':
                epochlist.append(int(epoch)/20)
            else:
                epochlist.append(int(epoch[1:])/20)
            print(i)
            flag=1

        if flag==1:
            if 'rouge1' in i:
                print(i.split(': ')[-2])
                r1=i.split(': ')[-4][:5]
                rl=i.split(': ')[-2][:5]
                rouge1.append(float(r1))
                rougeL.append(float(rl))

            if 'bleu' in i:
                b=i.split(': ')[-6][:5]
                if b == '0.0, ':
                    bleu.append(0.000)
                else:
                    bleu.append(float(b))
                bp=i.split(': ')[-4][:5]
                brevity_penalty.append(float(bp))
                flag=2
        if flag==2:
            flag=0
    f.close()
    return epochlist,bleu,brevity_penalty,rouge1,rougeL

# for i in range(len(epochlist)):
#     print(epochlist[i],bleu[i],brevity_penalty[i],rouge1[i],rougeL[i])

epochlist,bleu,brevity_penalty,rouge1,rougeL=getdata("with.txt")
epochlist2,bleu2,brevity_penalty2,rouge12,rougeL2=getdata("without.txt")


plt.figure(figsize=(11, 9))
plt.subplot(2, 2, 1)
plt.plot(epochlist, bleu, marker='o', linestyle='-', color='b', label='with knowledge')
plt.plot(epochlist, bleu2, marker='x', linestyle='--', color='r', label='without knowledge')
plt.xlabel('Epochs')
plt.ylabel('BLEU scores')
plt.title('BLEU scores')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(epochlist, brevity_penalty, marker='o', linestyle='-', color='b', label='with knowledge')
plt.plot(epochlist, brevity_penalty2, marker='x', linestyle='--', color='r', label='without knowledge')
plt.xlabel('Epochs')
plt.ylabel('Brevity Penalty')
plt.title('Brevity Penalty')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(epochlist,rouge1, marker='o', linestyle='-', color='b', label='with knowledge')
plt.plot(epochlist, rouge12, marker='x', linestyle='--', color='r', label='without knowledge')
plt.xlabel('Epochs')
plt.ylabel('Rouge1 scores')
plt.title('Rouge1 scores')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(epochlist,rougeL, marker='o', linestyle='-', color='b', label='with knowledge')
plt.plot(epochlist, rougeL2, marker='x', linestyle='--', color='r', label='without knowledge')
plt.xlabel('Epochs')
plt.ylabel('RougeL scores')
plt.title('RougeL scores')
plt.grid(True)
plt.legend()
plt.show()