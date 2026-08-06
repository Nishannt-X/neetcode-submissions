class Solution:
    def isValidSudoku(self, boards: List[List[str]]) -> bool:
        
        for row in range(len(boards)):
            temp=set()
            for j in range(len(boards[row])):
                if boards[row][j]==".":
                    continue
                if boards[row][j] in temp:
                    return False
                temp.add(boards[row][j])
        
        for col in range(9):
            temp=set()
            for i in range(9):
                if boards[i][col]==".":
                    continue
                if boards[i][col] in temp:
                    return False
                temp.add(boards[i][col])

        for i in range(0,9,3):
            for j in range(0,9,3):
                temp=set()

                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if boards[row][col]==".":
                            continue
                        if boards[row][col] in temp:
                            return False
                        temp.add(boards[row][col])
        return True

        