class TotalDigits:

    def __init__(self):
        self.arr = []
        self.fill_array()

    def get_number(self, i, j):

        digit = ''

        is_valid = False

        while j < len(self.arr[0]) and self.arr[i][j].isdigit():

            if self.is_valid_digit(i, j):
                is_valid = True

            digit += self.arr[i][j]
            j += 1
        
        return int(digit) if is_valid else 0

    def is_adjacent_to_symbol(self, i, j):
        
        return i>=0 and i<len(self.arr) and j>=0 and j<len(self.arr[0]) and \
        self.arr[i][j] != '.' and not self.arr[i][j].isdigit()

    def is_valid_digit(self, i, j):
        return  self.is_adjacent_to_symbol(i - 1, j - 1) or \
                self.is_adjacent_to_symbol(i - 1, j + 1) or \
                self.is_adjacent_to_symbol(i + 1, j - 1) or \
                self.is_adjacent_to_symbol(i + 1, j + 1) or \
                self.is_adjacent_to_symbol(i, j - 1) or \
                self.is_adjacent_to_symbol(i, j + 1) or \
                self.is_adjacent_to_symbol(i-1, j ) or \
                self.is_adjacent_to_symbol(i+1,j)
    
    def fill_array(self):

        while True:

            s = input()
            if s:
                self.arr.append(list(s))

            else:
                print("End of function", self.arr)
                break

    def get_total(self):

        tot=0

        for i in range(len(self.arr)):

            isNumber=False

            for j in range(len(self.arr[0])):

                if not isNumber and self.arr[i][j].isdigit():
                    isNumber = True
                    tot+=self.get_number(i,j)

                
                if isNumber and not self.arr[i][j].isdigit():
                    isNumber=False
        return tot



if __name__ == "__main__":
    td = TotalDigits()
    print(td.get_total())
