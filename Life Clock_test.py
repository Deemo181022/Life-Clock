import datetime
import math

def front_end():

     print ('Welcome!')
     print ('Please input your birthday in the format of mm/dd/yyyy')

def core():

        '/get users information/'

        month1=int(input("month:"))
        day1=int(input("day:"))
        year1=int(input("year:"))
        
        if (month1>12 or day1>31 or year1>2019):
              print('error!error!error!error!error!error!error!error!error!error!')
              print('error!error!error!error!error!error!error!error!error!error!')
              print('error!error!error!error!error!error!error!error!error!error!')
        
        '/get system information/'
        
        today =datetime.date.today()
        month2=today.month
        day2=today.day
        year2=today.year
        
        age=year2-year1
        
        '/calculate day in age /'
        
        i=1 
        x=0
        if month1==1:
             x=day1
        else:
             while i<month1:
                   if i==4 or i==6 or i==9 or i==11:
                          x=x+30
                   if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                          x=x+31
                   if i==2:
                          x=x+28
                          if year1%4==0:
                              x=x+1
                   i=i+1
             x=x+day1
        X=365-x
        j=1
        z=0
        
        if month2==1:
             z=day2
        else:
             while j<month2:
                   if j==4 or j==6 or j==9 or j==11:
                          z=z+30
                   if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
                          z=z+31
                   if j==2:
                          z=z+28
                          if year2%4==0:
                              z=z+1
                   j=j+1
             z=z+day2
        Z=z
        k=year1+1
        y=0
        
        while k<year2:
            y=y+365
            if k%4==0:
                y=y+1
            k=k+1
        Y=y
        
        '/return age and print day in age/'
        
        if year2==year1:
            day_in_age=Z-x
        else:
            day_in_age=X+Y+Z
            
        print ("Congratulations, you've survived for:")
        print (day_in_age)
        print ("days!")
        
        return age

def suggest(Age):

     '/According to the Wikipedia, today, the average life expectancy of humans has reached *79* years old./'
 
          
     '/for those who have exceeded the average human lifespan/'
     
     if Age>79:
          print ('A beautiful wish to you and your family -- live a happy life and everything goes well')
          print ('May happiness follow you wherever you go!')
          Goal=''

     '/for boys and girls/'
     
     if Age<14:
          print ('Would you like a seed, the courage to break through the sand, verdant shoots out of the ground, pointing to the sky.')
          print ('The longer, the more beautiful, the wiser, the healthy and happy growth in the new year!')
          Goal=''
     
     if (Age>13 and Age<81):
          percentage=int((Age/79)*100)
          print ("You have spent")
          print (percentage)
          print ("%of your life")
          
          '/for teenagers/'
          
          if Age<30:
             print('Youth means limitless possibilities.')
             print('2019 is about to pass, your dreams come true?')
             print('Just do it! Why not set your goals for the next year right away?')
             Goal=input("My goal for 2020 is:")
          
          '/for elderly/'
          
          if Age>60:
             print('Wishing you and yours a happy happy new year!')
             print('2019 is about to pass,Why not set your goals for the next year right away?')
             Goal=input("My goal for 2020 is:")
             
          '/for middle-aged/'
          
          if (Age<61 and Age>29):
             print('The good seaman is known in bad weather.') 
             print('2019 is about to pass, your dreams come true?')
             print('Just do it! Why not set your goals for the next year right away?')
             Goal=input("My goal for 2020 is:") 
             
     '/return 2020 goal and print suggest/'
             
     return Goal

def output(Age,str):

     if (Age>13 and Age<80):
     
          '/It is December,2019/'
          '/January-November:365-31=334/'
          
          Today=datetime.date.today()
          Day=Today.day
          Percentage=int(((334+Day)*100)/365)
          print('Attention!')
          print(Percentage)
          print("% has passed in 2019")
          print('Finally,remember your goals for 2020:')
          print(str)
          
     print('If you have any questions about life expectancy, please visit the following website:')
     print('https://en.wikipedia.org/wiki/Life_expectancy')
     print('https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy')
     print('Thank you!Have a good day!')
     print('See you next time!')
     
def main():

     front_end()
     age=core()   
     users_goal=suggest(age)       
     output(age,users_goal)

main()  

###############################################################################################################################################
#                                                               '/Test/'
###############################################################################################################################################
#
#Example 1
#
#Name:Tom
#Birthday:11/9/2008
#Goal: Work hard at school
#
#Output: Welcome!
#        Please input your birthday in the format of mm/dd/yyyy
#        month:11
#        day:9
#        year:2008
#        Congratulations, you've survived for:
#        4037
#        days!
#        Would you like a seed, the courage to break through the sand, verdant shoots out of the ground, pointing to the sky.
#        The longer, the more beautiful, the wiser, the healthy and happy growth in the new year!
#        If you have any questions about life expectancy, please visit the following website:
#        https://en.wikipedia.org/wiki/Life_expectancy
#        https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy
#        Thank you!Have a good day!
#        See you next time!
#
###############################################################################################################################################
#
#Example 2
#
#Name:Jerry
#Birthday:07/18/1936
#
#Output: Welcome!
#        Please input your birthday in the format of mm/dd/yyyy
#        month:7
#        day:18
#        year:1936
#        Congratulations, you've survived for:
#        30449
#        days!
#        A beautiful wish to you and your family -- live a happy life and everything goes well
#        May happiness follow you wherever you go!
#        If you have any questions about life expectancy, please visit the following website:
#        https://en.wikipedia.org/wiki/Life_expectancy
#        https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy
#        Thank you!Have a good day!
#        See you next time!
#
###############################################################################################################################################
#
#Example 3
#
#Name:Jack
#Birthday:03/14/1992
#Goal:Marry my girlfriend
#        
#Output: Welcome!
#        Please input your birthday in the format of mm/dd/yyyy
#        month:3
#        day:14
#        year:1992
#        Congratulations, you've survived for:
#        10121
#        days!
#        You have spent
#        34
#        %of your life
#        Youth means limitless possibilities.
#        2019 is about to pass, your dreams come true?
#        Just do it! Why not set your goals for the next year right away?
#        My goal for 2020 is:Marry my girlfriend
#        Attention!
#        99
#        % has passed in 2019
#        Finally,remember your goals for 2020:
#        Marry my girlfriend
#        If you have any questions about life expectancy, please visit the following website:
#        https://en.wikipedia.org/wiki/Life_expectancy
#        https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy
#        Thank you!Have a good day!
#        See you next time!
#
###############################################################################################################################################
#
#Example 4
#
#Name:Jones
#Birthday:10/23/1978
#Goal:Start my own company
#
#Output:Welcome!
#       Please input your birthday in the format of mm/dd/yyyy
#       month:10
#       day:23
#       year:1978
#       Congratulations, you've survived for:
#       15013
#       days!
#       You have spent
#       51
#       %of your life
#       The good seaman is known in bad weather.
#       2019 is about to pass, your dreams come true?
#       Just do it! Why not set your goals for the next year right away?
#       My goal for 2020 is:Start my own company
#       Attention!
#       99
#       % has passed in 2019
#       Finally,remember your goals for 2020:
#       Start my own company
#       If you have any questions about life expectancy, please visit the following website:
#       https://en.wikipedia.org/wiki/Life_expectancy
#       https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy
#       Thank you!Have a good day!
#       See you next time!
#
###############################################################################################################################################
#
#Example 5
#
#Name:Bob
#Birthday:2/14/1955
#Goal:Travel around the world
#
#Output:Welcome!
#       Please input your birthday in the format of mm/dd/yyyy
#       month:2
#       day:14
#       year:1955
#       Congratulations, you've survived for:
#       23665
#       days!
#       You have spent
#       81
#       %of your life
#       Wishing you and yours a happy happy new year!
#       2019 is about to pass,Why not set your goals for the next year right away?
#       My goal for 2020 is:Travel around the world
#       Attention!
#       99
#       % has passed in 2019
#       Finally,remember your goals for 2020:
#       Travel around the world
#       If you have any questions about life expectancy, please visit the following website:
#       https://en.wikipedia.org/wiki/Life_expectancy
#       https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy
#       Thank you!Have a good day!
#       See you next time!
###############################################################################################################################################
#                                                               '/End/'
###############################################################################################################################################
