from PIL import Image
import os
import argparse

def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory+"\\"+img)
        im_rescaled = im.resize(size, Image.ANTIALIAS)
        im_rescaled.save(directory+"\\"+img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resized Images')
    parser.add_argument('-d', "--directory", type=str, required=True,dest="d")
    parser.add_argument('-s', type=int, nargs=2, required=True, metavar=('width', 'height'),dest="s")
    args = parser.parse_args()
    rescale_images(args.d, args.s)