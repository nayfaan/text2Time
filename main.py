import re
import math
import os

def parseTimestamp (timestamp):
    if (not len(timestamp) == 9) or (not re.search("\d{4}-\d{4}",timestamp)):
        raise ValueError("Timestamp is improperly formatted!")
        
    timestampParsed = re.findall("\d{2}", timestamp)
    timestampParsed[:] = [int(time) for time in timestampParsed]
    
    if timestampParsed[0] > 23 or timestampParsed[1] > 59 or timestampParsed[2] > 23 or timestampParsed[3] > 59:
        raise ValueError("Timestamp exceeds possible time!")
    
    return timestampParsed
    
def timeDiff(timestamp):
    timestampParsed = parseTimestamp(timestamp)
    
    hours = timestampParsed[2] - timestampParsed[0]
    mins = timestampParsed[3] - timestampParsed[1]
    
    if mins < 0:
        hours = hours - 1
    mins = mins % 60
    hours = hours % 24
    
    return [timestamp, hours, mins]

def run():
    timestamps = input("Input timestamps: ")
    timestamps = re.sub("\s","", timestamps)
    print()
    
    if timestamps == "0":
        return 0
    
    if not type(timestamps) is str:
        raise TypeError("Input is not a string!")
        
    res = []
    
    if len(timestamps) < 9:
        raise ValueError("Input is less than 1 time span!")
        
    if len(timestamps) == 9:
        res.append(timeDiff(timestamps))
    elif len(timestamps) % 10 == 9:
        timestampsSplit = re.split(",", timestamps)
        if not timestampsSplit:
            raise ValueError("Input is not properly comma-separated!")
        
        for timestamp in timestampsSplit:
            if not len(timestamp) == 9:
                raise ValueError("Input is not properly comma-separated!")
            res.append(timeDiff(timestamp))
    else:
        raise ValueError("Input is not properly formatted!")
        
    return res
    
def calcRes(res):
    hours = 0
    mins = 0
    
    for span in res:
        print (span[0], ": ", f"{span[1] :02d}", " h ", f"{span[2] :02d}", " m", sep="")
        hours = hours + span[1]
        mins = mins + span[2]
        
    hours = hours + math.floor(mins/60)
    mins = mins % 60
    
    print("--------------------")
    print("Total:     ", f"{hours :02d}", " h ", f"{mins :02d}", " m", sep="")
    
if __name__ == "__main__":
    while True:
        res = run()
        if res == 0:
            break
        calcRes(res)
        
        print()
        input("Press Enter to continue...")
        os.system('clear')
