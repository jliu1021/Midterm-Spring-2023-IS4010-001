# videoGame.py

if __name__ != "__main__":
    import random
    def play():
        '''
        returns True if you won, False if you lost 
        '''
        if random.randint(0,100) == 10:
            raise Exception("Game Crashed")
        return random.choice([True, False])