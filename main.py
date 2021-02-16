from PIL import Image, ImageDraw

im = Image.new("RGBA", (500,250), (0,0,0,255)) # intialising the image class
draw = ImageDraw.Draw(im) # Getting ready to draw fibonachi

num = 16 # The amount of fibonachi numbers to visualise
fibo1 = 0 # Used to caculate the fibonachi sequence
fibo = 1 # Same as above
angle = 90 # Used to keep track of the angle of the arc
divNumY = 1.5 # Used to decide where the center will be
divNumX = 3 # Same as above

x1 = im.size[0] / divNumX # Used to keep track of the size and placement of each arc
y1 = im.size[1] / divNumY
x2 = im.size[0] / divNumX
y2 = im.size[1] / divNumY


for i in range(num): # Looping over the amount of numbers to generate

    tempFibo = fibo1 + fibo # Calculating the next number in the fibonachi sequence
    fibo1 = fibo # Swapping around the variables
    fibo = tempFibo

    draw.arc( # Making an arc
        (x1,y1,x2,y2), # Deciding the size and placement of the arc
        angle - 90, # Deciding the angle of the arc
        angle,
        fill = (0,255,0), # Making it green
        width = 1 # Making the arc wider to mach it with the size of the image class
    )
    if i % 4 == 0: # Making it run every fourth time
        x1 -= fibo1 # Doing some math to make the arcs fit
        y1 -= fibo1 * 2
        x2 += fibo1
        angle += 90 # Changing the angle of the arc

    elif i % 4 == 1: # Doing the same as above
        y1 -= fibo1
        x2 += fibo1 * 2
        y2 += fibo1
        angle += 90

    elif i % 4 == 2:
        x2 += fibo1
        y2 += fibo1 * 2
        x1 -= fibo1
        angle += 90

    elif i % 4 == 3:
        y2 += fibo1
        x1 -= fibo1 * 2
        y1 -= fibo1
        angle = 90

    else: # if python is broken
        print("how da fuck") # be confused

im.save("image.png", quality = 100) # save the image
