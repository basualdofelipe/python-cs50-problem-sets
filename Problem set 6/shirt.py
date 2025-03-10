#https://cs50.harvard.edu/python/2022/psets/6/shirt/

from PIL import Image, ImageOps
import sys, os

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        image_input = sys.argv[1]
        image_input_ext = os.path.splitext(image_input)[1]
        image_output = sys.argv[2]
        image_output_ext = os.path.splitext(image_output)[1]
    
    formats = [".jpeg", ".jpg", ".png"]

    if image_input_ext.lower() not in formats:
        sys.exit("Invalid input")
    elif image_output_ext.lower() not in formats:
        sys.exit("Invalid output")
    elif image_output_ext.lower() != image_input_ext.lower():
        sys.exit("Input and output have different extensions")
    else:
        try:
            paste_shirt(image_input, image_output)
        except IndexError:
            pass



def paste_shirt(img_input, img_out):
    try:
        with Image.open(f"img/{img_input}") as im:
            im_resized = ImageOps.fit(im, (600,600))
            shirt_image = Image.open("img/shirt.png")
            im_resized.paste(shirt_image, shirt_image)
            im_resized.show()
            im_resized.save(f"img/{img_out}")
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()