class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Extra Space
        res = [[0]*i for i in range(1, 102)]
        res[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                nextPour = (res[i][j]-1)/2
                if nextPour > 0:
                    res[i+1][j] += nextPour
                    res[i+1][j+1] += nextPour
        return min(1, res[query_row][query_glass])

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Optimal Space
        glass = [poured]
        for _ in range(query_row):
            nextGlas = [0]*(len(glass)+1)
            for j in range(len(glass)):
                Q = (glass[j]-1)/2
                if Q > 0:
                    nextGlas[j] += Q
                    nextGlas[j+1] += Q
            glass = nextGlas
        return min(1, glass[query_glass])
