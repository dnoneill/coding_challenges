# Assignment

In this folder is a text file named `images.txt`, the file has urls to 5 images. 
The script you are writing should download all five of the images in the `images.txt` file.
You will need to make sure all your filenames are unique and this script should output 5 jpg images.

# Some hints:
- You need to figure out how to read the txt file
- You need to figure out how to convert the file to a [list](https://www.w3schools.com/python/python_lists.asp)
- You will need to iterate over the list to download each image
- You will need to download the url contents using a library. The library `urllib.request` will do this or another library. It is not required to use this library. If you get stuck with this library, try searching for another library/combination. 
- Google and Stack Overflow are your friends if you get stuck anywhere in this assignment.  
- https://docs.python.org/3/ is where the full documentation to libraries exist. It can be overwhelming so I would try Google and Stack Overflow for your answers first.


# Optional
1. Try making filenames derivatives of the url. i.e. `ua023_007-003-bx0005-008-028.jpg`
2. Try adding new images to the images.txt file. Does the script still work? If it doesn't figure out what might have gone wrong.
3. Try adding an extra space to the end of each line in the images.txt file. Does it break your results? If so how do you fix that?
4. Try writing the files to a specific folder. 
5. Try writing the files to a folder you create through the script. (The `os` library is very handy for creating folders and checking to see if they exist)
