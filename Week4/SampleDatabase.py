infile = open("sample_text.txt","r")

# Read all line into lines
lines = infile.readlines()
# Close the file
infile.close()

# Assign first line into lastLine valuable
firstLine = lines[0].strip()
print(firstLine)

# Assign last line into lastLine valuable
lastLine = lines[-1]
print(lastLine)