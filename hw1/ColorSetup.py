from Myro import *


def getBlobConfiguration():
    """Walks user through process of getting a reference picture and a rectangle in it
    of the desirect color, and it returns the picture and four coordinates for use later
    in setting the color to search for."""
    
   
    # Step 1:  Set the robot pointing directly at the sign
    #          and at the specified distance
    yesno("Click Yes once the robot is pointing at the reference color: ")


    # Step 2:  Take a picture and save it in a variable (you'll
    #          need it later). Show the picture.
    refPic = takePicture()
    show(refPic)


    # Step 3:  User selects rectangle in picture, and program computes
    #          the (x, y) values for the corners
    speak("Click on the upper left corner and lower right corner of a rectangle containing the reference color.")
    speak("The (x, y) coordinates will be printed in the Output section.")
    speak("You have three seconds.")
    wait(3.0)
    coordRes = ask("Type the four coordinates separated by spaces: ulx uly lrx lry")
    coordList = [int(s) for s in coordRes.split()]
    [ulX, ulY, lrX, lrY] = coordList


    # Step 4:  Calls function to set the blob configuration
    configureBlob(refPic, ulX, ulY, lrX, lrY)


    # Step 5:  Test it by showing the blob picture
    blobPic = takePicture('blob')
    show(blobPic)

    # Step 6:  Return the information needed to configure the blob-seeker later
    return refPic, ulX, ulY, lrX, lrY



# The script part below sets up the yellow and pink reference information

#speak("First point the robot at the yellow sign")
 
#(yellPic, yellULX, yellULY, yellLRX, yellLRY) = getBlobConfiguration()
 
#speak("Next point the robot at the pink sign")
 
#(pinkPic, pinkULX, pinkULY, pinkLRX, pinkLRY) = getBlobConfiguration()


    