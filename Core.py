import Next_price
import Graph_Draw
import time

a = 0
while a < 1000:
    Next_price.call()
    # Graph_Draw.show_koti()
    #time.sleep(1)
    a += 1

Graph_Draw.show_koti()
