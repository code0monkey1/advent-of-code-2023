#--- Day 2: Cube Conundrum ---

# Problem Link : https://adventofcode.com/2023/day/2
passes={
    'green':13,
    'red':12,
    'blue':14,
  }
tot=0
while True:

  try:
    s= input()
   
    colon= s.find(":")

    [_,game]= s[0:colon].split(' ')
    games= s[colon+1:].split(';')
    
    isValid=True

    for contest in games:
      for single in contest.split(','):
          [value, color]=single.strip().split(' ')
          print("The value is",value,"The color is",color)
          if int(value)>passes[color]:
            isValid=False
            break
    print("game is ",game,"total is",tot)
    tot+= int(game) if isValid else 0
    print("tot is",tot)
    
  except:
    break

print(tot)