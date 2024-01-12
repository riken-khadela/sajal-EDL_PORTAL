import random, time

class Bot():
    
    def get_data(self) :
        data = {
            "leistuning" : {
                "L1" : f"{random.randint(5,30)}.{random.randint(5,30)} kw",
                "L2" : "15.29 kw",
                "L3" : "15.29 kw"
                },
            "main" : {
                "L1" : "15.29 kw",
                "L2" : "15.29 kw",
                "L3" : "15.29 kw"
                }
        }
        
        return data