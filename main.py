from sense_hat import SenseHat

sense = SenseHat()

A = (100,100,100)
B = (0,0,0)
S = (255,0,0)

pixels = [  
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
    S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S
]

sense.set_pixels(pixels)



