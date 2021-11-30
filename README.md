# BREACH
This is an example of how to perform a breach attack on a test website to extract secret and private tokens.

## Requirements
- **Python3** (Recomended but also Python2 works)
- **Requests** module for python

## Setup
1. **Clone the repository**

`git clone https://github.com/miguelob/BREACH`

2. **Install requests module for Python**:
  - Python2.X
  
    `pip install requests`
  - Python 3.X

    `pip3 install requests`

 3. **Run de code**
 
 ## Modificacions
 For testing this code on your own websites, you can change the URL parameter for your one. The MASK might be also needed to change, but you will figure it out as you develop your own breach attack. For testing and educational purposes, I recommend testing on the public URL on the code. That website is created specifically for testing this attack.
 
 ## Examples
-  **Debug ON**: Uncomment the print lines
  ![example gif](https://github.com/miguelob/BREACH/blob/main/media/debug.gif)
  
-  **Standart output**: Time elapsed, iterations and token.
  ![example gif](https://github.com/miguelob/BREACH/blob/main/media/output.gif)
