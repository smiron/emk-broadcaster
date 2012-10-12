import emotiv 
headset = emotiv.Emotiv() 
try:    
    while True:        
        headset.dequeue()        
finally: 
    headset.close()
