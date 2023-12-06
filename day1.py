# Advent of code : Day 1 


# Link : https://adventofcode.com/2023/day/1

# Part 2 

word_to_digit={
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
  }

digits =[
           '0',
           '1',
           "2",
           '3', 
           '4', 
           '5', 
           '6',
           '7', 
           '8', 
           '9'
  ]


  # find the minimum find and the maximum  rfind values for all :

res=0

while True:

    try:
         
         s = input("")
         
         l=''
         r=''
         
         lindex=len(s)
         rindex=-1

         for word in word_to_digit:

             
            if s.find(word)!=-1 and s.find(word)<lindex:
               lindex=s.find(word)
               l=word_to_digit[word]
            if s.rfind(word)!=-1 and s.rfind(word)>rindex:
               rindex=s.rfind(word)
               r=word_to_digit[word]
               

          
  
         for digit in digits:
    
            if s.find(digit)!=-1 and s.find(digit)<lindex:
               lindex= s.find(digit)
               l=digit

               
            if s.rfind(digit)!=-1  and s.rfind(digit)>rindex:
               rindex=s.rfind(digit)
               r=digit

         first= int(l)*10
         last = int(r)
         

         
         res = res + (first + last)
         
         
    except:

          break
  
  

print(res)