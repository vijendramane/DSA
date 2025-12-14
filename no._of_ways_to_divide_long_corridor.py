class Solution(object):
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7

        total_seats = corridor.count('S') 
        if total_seats == 0 or total_seats % 2 != 0: 
            return 0

        ways = 1 
        seats = 0
        plants = 0 

        for c in corridor:
            if c == 'S':
                seats += 1
                # after completing one section of 2 seats
                if seats == 3:
                    ways = (ways * (plants + 1)) % MOD
                    plants = 0
                    seats = 1
            else:  # c == 'P'
                if seats == 2:
                    plants += 1

        return ways
