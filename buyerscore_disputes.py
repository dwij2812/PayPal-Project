import numpy as np
import matplotlib.pyplot as plt
###############################################################
dispute_categories=["INR","SNAD","UT"]
'''INR-Item Not Recieved
   SNAD-Significantly Not As Described
   UT-Unauthorized Transaction
'''

a=["INR","GOOD","GOOD","SNAD","UT","SNAD"]
b=["GOOD","GOOD","GOOD","GOOD","GOOD"]
c=["GOOD","GOOD"]
d=["BAD","BAD","GOOD","GOOD","GOOD"]
###############################################################
def cummulated_disputes(categories=[]):
    k = 0
    l = [[0 for x in range(len(categories))]for x in range(2)]
    for i in categories:
        l[0][int(k)] = i
        l[1][int(k)] = 0
        k+=1
    return l
###############################################################
def score(user=[],categories=[]):
    print('\n\n////////////////////////////////////////////////////\n')
    rel=cummulated_disputes(categories)
    good = 0
    disputes = 0
    score = 0
    hold = 0
    bad = 0
    counted = []
    y = [0 for i in range(len(user))]
    x=range(len(user))
    k=0    #Count Variable for the loops
    for i in user:
        if i in categories:
            n=rel[0].index(i)
            rel[1][n]+=1
            disputes+=1
            y[int(k)]=int(0)
            k+=1
            if i not in counted:
                counted.append(i)
                score+=1
        else:
            if i == 'HOLD':
                y[int(k)]=2
                hold+=1
                k+=1
            elif i == 'BAD':
                y[int(k)]=3
                bad+=1
                k+=1
            else:
                y[int(k)]=int(1)
                good+=1
                k+=1
    print("The User Transaction Data is: ")
    print(user)
    print("The User Disputes Cummulated into categories are:")
    print(rel)
    print("\nThe Number Of good Transaction Are:")
    print(good)
    print("\nThe Number Of Disputed Transactions are:")
    print(disputes)
    print("\nThe Number of Transactions put on hold is:")
    print(hold)
    print("\nThe number of bad Transactions are:")
    print(bad)
    m=rel[1].index(max(rel[1]))
    print("The User is facing most of the problems as:")
    print(rel[0][m])
    print("Dispute Category Spread Coefficient is:")
    cat_spread=(len(categories)-score)/len(categories)
    print(cat_spread)


    #Score Generation
    if(len(user)>=3):
        if(good>disputes):
            score=cat_spread*30+(good/len(user))*70
            print("The User Score Is:\n\n")
            print(score)
        else:
            score=(good/len(user))*100
            print("The User Score Is:\n\n")
            print(score)
    else:
        print("Needed More Transactions to generate the score");


	#Interpolation Method for prediction of the Next Data Item
    print(y)
    z=np.polynomial.polynomial.polyfit(x,y,3)
    print(z)
    ffit=np.poly1d(z)
    print(ffit)
    print(ffit(len(user)))



    labels = ['Good', 'Disputes','Hold','False Claims']
    sizes = [good,disputes,hold,bad]
    colors = ['#003087', '#009cde','#F68900','#fe001a']
    explode = (0.1, 0.1,0.1,0.1)
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title("Good transactions vs Disputes")
    plt.show()


    if (disputes != 0):
        labels = dispute_categories
        sizes = rel[1]
        colors = ['#003087', '#009cde','#012169']
        explode = (0.1, 0.1, 0.1)
        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title("Spread of Disputes")
        plt.show()

print("A: ",score(a,dispute_categories))
print("B: ",score(b,dispute_categories))
print("C: ",score(c,dispute_categories))
print("D: ",score(d,dispute_categories))
