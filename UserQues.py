#############################UserQues.py###########################################
def userQues():
    import csv
    f=open("Ques.csv","w+",newline="")
    w=csv.writer(f,delimiter=",")
    ft=['qid','q','i','o']
    w.writerow(ft)
    Q=[['LA1','Return the factorial of a given natural number','5','120'],
       ['LA2','Return the list of series of even natural numbers till a given value','10','[2, 4, 6, 8, 10]'],
       ['LA3','Return the nth element of Fibonacci series','5','3'],
       ['LA4','Return the list of series of odd natural numbers till a given value','9',
        '[1, 3, 5, 7, 9]'],
       ['LA5','Return the area of a circle with given radius=r(in cm); use pi=3.14','5','78.5'],
       ['LB1','Check if a given number is a palindrome,return (Yes/No)','12321','Yes'],
       ['LB2','Return sum of the series of first n natural numbers','5','15'],
       ['LB3','Reverse a given integer without converting its datatype','123','321'],
       ['LB4','Find the sum of the digits of a given number','45312','15'],
       ['LB5','Return the number of vowels in a given string','PythonProgramming','4'],
       ['LC1','Check whether a given year is a leap year or not,return "Yes" or "No"','1600','Yes'],
       ['LC2','Find and return the largest word from a given sentence',"You are currently at level C","currently"],
       ['LC3','Find the sum of all the odd digts in a given number',"943249","21"],
       ['LC4','Return the index value of a given digit from 9238484224','2','8'],
       ['LC5','Given a list of N integers, return the sum of two integers such that their sum is nearest to 0','[-8,-66,-60]','-68']]       
    w.writerows(Q)
    f.close()
userQues()
