import funcs
import argparse
from PIL import Image
from random import shuffle


def cli():
    parser = argparse.ArgumentParser(description="Creates a photomosaic from input images")
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)
    parser.add_argument('--reverse', dest='reverse', action='store_true')

    return parser.parse_args()


if __name__ == '__main__':
    args = cli()

    target_image = Image.open(args.target_image)
    print("Reading input folder")
    input_images = funcs.get_images(args.input_folder)

    if not input_images:
        print("No input images found in ", args.input_images,". Exiting.")
        exit(0)

    shuffle(input_images)
    reverse = False
    if args.reverse:
        reverse = True

    grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))
    output_filename = 'mosaic.png'
    if args.outfile:
        output_filename = args.outfile

    reuse_images = True
    resize_input = True
    print("Starting photomosaic creation...")

    if not reuse_images:
        if grid_size[0] * grid_size[1] > len(input_images):
            print("Grid size less thn number of images.")
            exit(0)

    if resize_input:
        print("Resizing images.")
        dimensions = (int(target_image.size[0] / grid_size[1]), int(target_image.size[1] / grid_size[0]))
        print("Max tile dimensions: {0}".format(dimensions, ))

        for img in input_images:
            img.thumbnail(dimensions)

    mosaic_image = funcs.create_photomosaic(target_image, input_images, grid_size, reverse, reuse_images)

    mosaic_image.save(output_filename, 'PNG')
    print("Saved to {0} \nDone.".format(output_filename, ))
