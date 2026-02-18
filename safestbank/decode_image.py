import uu

# Input and output file paths
input_file = 'secret_image.txt'
output_file = 'secret_image.jpg'

# Decode the uuencoded image
with open(input_file, 'r') as infile, open(output_file, 'wb') as outfile:
    uu.decode(infile, outfile)

print("Image decoded and saved as", output_file)
