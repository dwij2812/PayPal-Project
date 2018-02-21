import numpy as np
import matplotlib.pyplot as plt
############################################################################################
categories=["Electronics","Daily Needs","Clothes","Tickets","Entertainment","Education","Automobile"]
a=["Electronics","Tickets","Tickets"]
b={"Clothes","Tickets","Tickets"}
c=["Daily Needs","Clothes","Tickets","Entertainment","Clothes","Clothes"]
d=["Tickets","Tickets","Tickets","Tickets","Tickets"]
e=["Electronics","Daily Needs","Clothes","Tickets","Entertainment","Education"]
f=["Electronics","Daily Needs","Clothes","Tickets","Entertainment","Education","Electronics","Electronics","Electronics","Tickets"]
g=["Tickets"]
############################################################################################
def reliability(categories=[]):
    k=0
    l=[[0 for x in range(len(categories))]for x in range(2)]
    for i in categories:
        l[0][int(k)]=i
        l[1][int(k)]=0
        k+=1
    return l
############################################################################################
def score(user=[],categories=[]):       # To Describe the Spread Of Products Bought
    print('\n\n///////////////////////////////////////////////////////////////////////////////\n')
    rel=reliability(categories)
    counted=[]
    cat_score_list=[]
    score=0
    if(len(user)>=3):
        for i in user:
            n=rel[0].index(i)
            rel[1][n]+=1
            if i not in counted:
                counted.append(i)
                score+=1
        print("The User Transaction Data is: ")
        print(user)
        print("The User Categories Cummulated into categories are")
        print(rel)
        m=rel[1].index(max(rel[1]))
        print("The User is an buyer related to the field of:")
        print(rel[0][m])
        print("Considering all the Categories the top categories are:")
        if(score>3):
            print(sorted(zip(rel[1], rel[0]), reverse=True)[:3])      #To print the Top three categories with the number of times the thing wass sorted for.
        else:
            print(sorted(zip(rel[1], rel[0]), reverse=True)[:score])      #To print the Top three categories with the number of times the thing wass sorted for.
        print("Category Spread Coefficient is:")
        cat_spread=1-(len(categories)-score)/len(categories)
        print(cat_spread)
        print("The number of categories user has shopped from is:")
        print (score)
        print("====================================================")
        print("User Score (100) according to category is:")
        for i in rel[0]:
            z=rel[0].index(i)
            purchases_field=rel[1][z]/rel[1][m]#len(user)
            print("For ",i," the score is: ")
            cat_score=cat_spread*50+purchases_field*50
            if((cat_score>25) and (rel[1][z]==0)) :
                print("Since the value might shoot up unnecessarily, we have capped it")
                cat_score=25
            cat_score_list.append(cat_score)
            print(cat_score)
        print("For the User the Average Score Is:")
        avg_score=0
        d=0
        var=0
        for i in rel[1]:
            if(i != 0):
                avg_score+=cat_score_list[d]
                var+=1
            d+=1
        avg_score=avg_score/var
        print(avg_score)
        print("For the Graph Follow the Legend")
        j=0
        for i in categories:
            print(j,' -- ',i)
            j+=1

        y=range(len(categories))
        plt.plot(y,cat_score_list,marker='o', color='g')
        plt.ylim(0,100)
        plt.title("Category Score")
        plt.xlabel("Category")
        plt.ylabel("Score")
        ##plt.text("Score Graph of the Different Categories which we have")
        plt.show()
    else:
        print("Meed more data before calculating the User Score")
        print("=============MINIMUM LIMIT CAP=============")
############################################################################################
print("G: ",score(g,categories))
print("A: ",score(a,categories))
print("B: ",score(b,categories))
print("C: ",score(c,categories))
print("D: ",score(d,categories))
print("E: ",score(e,categories))
print("F: ",score(f,categories))
