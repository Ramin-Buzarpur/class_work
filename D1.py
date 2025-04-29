# x=range(6)
# print(x)
# x = complex(1j+2j+2)	
# x = list(("apple", "banana", "cherry"))	
# x=12E5
# print(type(x))
# print(x)
# x=int(x)
# print(type(x))
# print(x)
# a='''laskdjlkasjldaj
# sad
# '''
# print(a)
# b="aklkfkjl\n"\
# "kasdjlkd\n"\
# "klfdjlk"
# print(b)
# a="dskfjds"
# print(a[0])
# for x in "banana":
#     print(x)
# print(len("anksjdhk"))
# txt="ra min"
# txt1="ar min"
# print("ra" in txt)
# print(" " in txt)
# print("ra" and "ar" not in txt)
# for x in "banana":
#     print(x)
# for x in range(0,20,2):
#     print(x)
# b = "Hello, World!"
# print(b[-5:-2])
# a = "Hello, World!"
# print(a.upper())
# a = "Hello, World!"
# # print(a.lower())
# a = "   ssHello,  World  !  " 
# print(a.strip())
# a = "   ssHello,  World  !  " 
# print(a.replace("ss","a"))
# text="ramin is a beautiful man !"
# words=text.split()
# print(words)
# words=text.split()
# print(words)
# words=text.split(",")
# print(words)
# words=text.split("") invalid  syntax
# print(words)
# words=text.split(" ")
# print(words)
# words=text.split("i")
# print(words)
# exit()
# name="ali"
# print("akaa"name)
# print("akaa",3,name)
# x=input("asksd")
# print(type(x))
# print(x+2)
# x=int(input("asksd"))
# print(type(x))
# print(x+2)
# price = 59
# txt = f"The price is {20*30:.3f} dollars"
# print(txt)
# try :
#     age=int(input("a"))
#     print(f"askjl {age}")
# except :
#     print("vorodi namotabar")
# #     return 
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''okey
# a = "Hello, World!"
# print(len(a))
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
# b = "Hello, World!"
# print(b[2:5])
# txt = "We are the so-called \"Vikings\" from the north."
# txt = "We are the so-called \"'''Vikings\";'; from the north."
# print(bool(""))
# x=int(input("sen"))
# b=input("esm")
# c=int(input("tedad dars"))
# global f
# for i in range(c):
#     h=int(input("nomre"))
#     f+=h
# print(f)
# x=int(input("yek adad vared kon:"))
# for i in range(x) :
#     if i == 0 or i == x-1:
#         print("*"*(x-1))
#     else :
#         print("*"+" "*(x-2)+"*")
# x=int(input("yek adad vared kon"))
# b = 0
# for i in range(1,x+1):
#     if x%i == 0 :
#         b+=1
# if b>2 :
#     print("NO")
# else:
#     print("YES")
# x=int(input())
# total =0
# if x>0 :
#     for i in range(1,x):
#         b=x%i
#         if b==0 :
#             total+=i
#     if(total==x):
#         print("YES")
#     else :
#         print("NO")
# else :
#     print("input is invalid")

# x=int(input())
# i=j=k=0
# magic=0
# for i in range(1,x) :
#     for j in range(1,x) :
#         for k in range(1,x) :
#             if (i+j+k)==x :
#                 if(i**2+j**2)==k**2:    
#                     if magic==0 :
#                         # sort_number=sorted([i,j,k])
#                         # print(sort_number)
#                         smallest=min(i,j,k)
#                         maximum=max(i,j,k)
#                         middle=i+j+k-smallest-maximum
#                         print(smallest,middle,maximum)
#                         magic+=1
# if magic<=0 :
#     print("IMPOSSIBLE")
# x=int(input())
# sum=0
# total=""
# for i in range(1,x+1):
#     sum+=i
#     if i==x :
#         total+=f"{i} = {sum}"
#     else :
#         total+=f"{i} + "
# print(total)
# x='''***   *   *  *****  *   *   ***   *   *  
# *  *   * *     *    *   *  *   *  **  *  
# ***     *      *    *****  *   *  * * *  
# *       *      *    *   *  *   *  *  **  
# *       *      *    *   *   ***   *   *
# '''
# print(x)


# a=input()
# if a=="square" :
#     s=int(input())
#     sum=s*s
#     print(f"{sum:.1f}")
# elif a=="circle" :
#     s=int(input())
#     sum=3.14*s*s
#     print(f"{sum:.1f}")
# elif a=="rectangle" :
#     s1=int(input())
#     s2=int(input())
#     sum=s1*s2
#     print(f"{sum:.1f}")
# elif a=="triangle" :
#     s1=int(input())
#     s2=int(input())
#     sum=(0.5)*s1*s2
#     print(f"{sum:.1f}")
# else :
#     print("invalid information")

# a=int(input())
# sum=1
# for i in range(1,a+1):
#     sum*=i
# print(sum)

# s1=int(input())
# s2=int(input())
# s3=int(input())
# if s1>0 and s2>0 and s3>0 :

# else:
#     print("No Negative Edges") 
#     exit()

# x=int(input())
# if x==2 :
#     print(x)
# else :
#     sum="2 "
#     for i in range(3,x) :
#         magic=0
#         for j in range(2,i):
#             if i%j==0 :
#                 magic+=1 
#                 break
#         if magic==0:
#             sum+=f"{i} "
# print(sum)
# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")

# thislist.extend(thistuple)

# print(thislist) 

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")

# thistuple.extend(thislist)
# print(thistuple)
# x='''
#    * 
#   ***  
#  *****    
# *******
# '''
# print(x)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = False)
# print(thislist)
# x=int(input())
# sum=0
# for i in range(len(str(x))) :
#     b=(a/((10)**i))
#     c=b%10
    
# class DB:
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
#         self.asdhgja="adahjk"
# dog1=DB("ad",18)
# print(dog1.asdhgja)

# import pandas as pd
# print("Pandas نصب شده! نسخه:", pd.__version__)