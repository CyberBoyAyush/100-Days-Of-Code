def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read()) 
    except FileNotFoundError:
        print(f'File {filename} is not found')
readFile("/home/cyberboyayush/Documents/Python/Practise/Chapter 12/1.txt")
readFile("/home/cyberboyayush/Documents/Python/Practise/Chapter 12/2.txt")
readFile("/home/cyberboyayush/Documents/Python/Practise/Chapter 12/3.txt")
