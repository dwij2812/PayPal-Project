from pymongo import *
from random import randint
from bson import ObjectId
from flask import Flask, request,jsonify #import main Flask class and request object
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db=client.test
import requests as requests
import json as json
def get(url):
    try:
        res = requests.get(url)
        return res.json()
    except:
        return False
categories=["Electronics","Daily Needs","Clothes","Tickets","Entertainment","Education","Automobile"]
a=["Electronics","Tickets","Tickets"]
b=["Clothes","Tickets","Tickets"]
c=["Daily Needs","Clothes","Tickets","Entertainment","Clothes","Clothes"]
d=["Tickets","Tickets","Tickets","Tickets","Tickets"]
e=["Electronics","Daily Needs","Clothes","Tickets","Entertainment","Education"]
f=["Electronics","Daily Needs","Clothes","Tickets","Entertainment","Education","Electronics","Electronics","Electronics","Tickets"]
g=["Tickets","Daily Needs","Clothes"]
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
    print('\n\n//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')
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
        """print("The User Transaction Data is: ")
        print(user)
        print("The User Categories Cummulated into categories are")
        print(rel)"""
        m=rel[1].index(max(rel[1]))
        """print("The User is an buyer related to the field of:")
        print(rel[0][m])
        print("Considering all the Categories the top categories are:")
        if(score>3):
            print(sorted(zip(rel[1], rel[0]), reverse=True)[:3])      #To print the Top three categories with the number of times the thing wass sorted for.
        else:
            print(sorted(zip(rel[1], rel[0]), reverse=True)[:score])      #To print the Top three categories with the number of times the thing wass sorted for.
        print("Category Spread Coefficient is:")"""
        cat_spread=1-(len(categories)-score)/len(categories)
        """print(cat_spread)
        print("The number of categories user has shopped from is:")
        print (score)
        print("==========================================================================================================================================")
        print("User Score (100) according to category is:")"""
        for i in rel[0]:
            z=rel[0].index(i)
            purchases_field=rel[1][z]/rel[1][m]#len(user)
            #print("For ",i," the score is: ")
            cat_score=cat_spread*50+purchases_field*50
            ##General Capping for the upper limit of not purchased categories
            ##if((cat_score>25) and (rel[1][z]==0)) :
                ##print("Since the value might shoot up unnecessarily, we have capped it")
                ##cat_score=25
            cat_score_list.append(cat_score)
            #print(cat_score)
        #################################################################################################
        ##Dynamic Capping for the Upper Limit of the not purchased Categories
        #print("----------After Normalization of the data and introducing the Upper value Caps We Get----------")
        flag=0
        for i in rel[0]:
            z=rel[0].index(i)
            purchases_field=rel[1][z]/rel[1][m]#len(user)
            #print("For ",i," the score is: ")
            cat_score=cat_spread*50+purchases_field*50
            if((cat_score>max(cat_score_list)/4) and (rel[1][z]==0)) :
                #print("**********Since the value might shoot up unnecessarily, we have capped it**********")
                cat_score=max(cat_score_list)/4
            cat_score_list[flag]=cat_score
            flag+=1
            #print(cat_score)
        return cat_score_list
        ############################################################################################
        """print("For the User the Average Score Is:")
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
        plt.show()"""
    else:
        '''print("Meed more data before calculating the User Score")
        #easygui.msgbox("\nSince the available transactions for the user are less than three hence we cannot predict the Score\n",title="Insufficient Data")
        print("=============MINIMUM LIMIT CAP=============")'''
        for i in range(len(categories)):
            cat_score_list.append(0)
        return cat_score_list
def addtodb(user,categories,user_id):
    k=score(user,categories)
    test = {
            'electronics' : k[0],
            'daily_needs' : k[1],
            'clothes' : k[2],
            'tickets' : k[3],
            'entertainment' : k[4],
            'education' : k[5],
            'automobile' : k[6]
        }
    param={
            '_id':ObjectId(user_id)
           } 
    result=db.test.update_one(param,{"$set": test},upsert=False)
    print("Added the data to the Database")
"""print("G: ",addtodb(g,categories))
print("A: ",addtodb(a,categories))
print("B: ",addtodb(b,categories))
print("C: ",addtodb(c,categories))
print("D: ",addtodb(d,categories))
print("E: ",addtodb(e,categories))
print("F: ",addtodb(f,categories))"""
##############################################################################
app = Flask(__name__) #create the Flask app

@app.route('/buyerscore',methods=['POST'])
def query_example():
    r= requests.form['email']
    data=r.json()
    user_id=data
    list=fetch(str)
    addtodb(list,categories,user_id)
    return
if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
user_id="5ad0edac8698a52bf05f7f2e"
def fetch(str):
    k=db.test.find_one({"email": user_id})
    print(k)
    tickets=k["N_Tickets"]
    education=k["N_Education"]
    Entertainment=k["N_Entertainment"]
    Automobile=k["N_Automobile"]
    Daily_Needs=k["N_Daily_Needs"]
    Electronics=k["N_Electronics"]
    Clothes=k["N_Clothes"]
    print(tickets,education,Entertainment,Automobile,Daily_Needs,Electronics,Clothes)
    fetched=[]
    for i in range(tickets):
        fetched.append('Tickets')
    for i in range(education):
        fetched.append('Education')
    for i in range(Entertainment):
        fetched.append('Entertainment')
    for i in range(Automobile):
        fetched.append('Automobile')
    for i in range(Daily_Needs):
        fetched.append('Daily Needs')
    for i in range(Electronics):
        fetched.append('Electronics')
    for i in range(Clothes):
        fetched.append('Clothes')
    print(fetched)
    return fetched
list=fetch(str)
print("Adding to the Database ",addtodb(list,categories,user_id))
