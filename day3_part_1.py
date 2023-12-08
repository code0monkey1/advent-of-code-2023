class TotalDigits:

    def __init__(self):
        self.arr = []
     
    def get_number(self,i,j):
        
        digit=''

        is_valid=False

        while j< len(self.arr[0]) and self.arr[i][j].isdigit():
            
            if self.is_valid_digit(i,j):
                is_valid=True
            
            digit+=self.arr[i][j]
            j+=1

        return int(digit) if is_valid else 0

    def is_adjacent_to_symbol(self,i,j):
        return self.arr[i,j]!='.' and not self.arr[i,j].isdigit()
    
    def is_valid_digit(self,i,j):

        #top_left i-1 , j-1
        if i>0  and j>0  and self.is_adjacent_to_symbol(i-1,j-1) :
            return True
        #top_right i-1 , j+1
        if i>0  and j<len(self.arr[0]) and self.is_adjacent_to_symbol(i-1,j+1) :
            return True
        #bottom_left i+1 , j-1
        #bottom right i+1 , j+1
        #left i j-1
        if j>0 and self.is_adjacent_to_symbol(i,j-1):
               return True
            
        #right
        #top
        #bottom


    def fill_array(self):

        while True:
            
            s = input()
            if s:
                self.arr.append(list(s))

            else :
                print("End of function",self.arr)
                break
               

if __name__ == "__main__":
    td = TotalDigits()
    td.fill_array()
