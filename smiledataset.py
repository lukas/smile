from glob import glob
from skimage.measure import block_reduce
from skimage.io import imread
import numpy as np
import re


# load the data
negative_paths = glob('SMILEsmileD-master/SMILEs/negatives/negatives7/*.jpg')
positive_paths = glob('SMILEsmileD-master/SMILEs/positives/positives7/*.jpg')



def examples_to_dataset(examples, block_size=2):
    train_X = [] # pixels
    train_y = [] # labels
    test_X = []
    test_y = []
    for path, label in examples:
        num = re.search(r'([0-9]+)\.jpg', path)
        img_id = int(num.group(1))
        # read the images
        img = imread(path, as_grey=True)

        # scale down the images
        img = block_reduce(img, block_size=(block_size, block_size), func=np.mean)

        if img_id < 2000:
            test_X.append(img)
            test_y.append(label)
        else:
            train_X.append(img)
            train_y.append(label)
    return np.asarray(train_X).astype(np.float32), np.asarray(train_y), \
            np.asarray(test_X).astype(np.float32), np.asarray(test_y)

def load_data():
    examples = [(path, 0) for path in negative_paths] + [(path, 1) for path in positive_paths]

    return(examples_to_dataset(examples))
