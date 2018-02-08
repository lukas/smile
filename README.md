![](https://github.com/hromi/SMILEsmileD/blob/master/SMILEs/positives/positives7/10046.jpg?raw=true)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/positives/positives7/10045.jpg)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/positives/positives7/10047.jpg)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/positives/positives7/10048.jpg)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/positives/positives7/10050.jpg)

![](https://github.com/hromi/SMILEsmileD/blob/master/SMILEs/negatives/negatives7/10211.jpg?raw=true)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/negatives/negatives7/10210.jpg)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/negatives/negatives7/10212.jpg)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/negatives/negatives7/10213.jpg)
![](https://raw.githubusercontent.com/hromi/SMILEsmileD/master/SMILEs/negatives/negatives7/10214.jpg)



# Smile :)

Smile Classifier - The challenge is to create a classifier that can distinguish a smiling face.

## Setup

Be sure to clone this repository and unzip the data on your AWS instance

```shell
cd ~
git clone https://github.com/lukas/smile.git
cd smile
unzip master.zip
```

Create an account at https://app.wandb.ai/login?invited if you don't have one.  Copy an api key from your [profile](https://app.wandb.ai/profile) and paste it after calling `wandb login` below.

In your AWS terminal run:

```
pip install -r requirements.txt --upgrade
wandb login
```

Now try running the default scaffolding:

```
wandb run smile.py
```

## Help

1. [Slack Channel](https://join.slack.com/t/doloreslabs/shared_invite/enQtMzExNjMzMDcwMzM4LTk4YTFjN2I0YWJkNTU5OGQ1YTI5NDU5ODU2MzUyYjVjM2Y0OTIyZDgwMmNiY2U3N2ZjNmQzOThmMzkwNjA0ODQ)
2. [Keras Docs](https://keras.io/getting-started/sequential-model-guide/)
3. [Previous Work](https://github.com/oarriaga/face_classification)
4. [Other datasets](http://www.face-rec.org/databases/)
5. [Data Augmentation](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
6. [Transfer Learning](https://www.learnopencv.com/keras-tutorial-transfer-learning-using-pre-trained-models/)

## Files

- smile.py - scaffolding to get you started
- smiledataset.py - loads the data
- master.zip - the face dataset, smiles are in the positive directory the rest are in the negative directory

## Stuck?

1. Ask for or help
2. https://blog.slavv.com/37-reasons-why-your-neural-network-is-not-working-4020854bd607

## Extra Credit
 
Deploy the model.  

## Ideas

### Simple, Effective:
- Normalize train_X and test_X
- Add dense layers
- Add convolutional layer(s)?
- Add dropout
- Change learning rate
- Experiment with activation functions

### Fancier, Maybe Effective:
- Data Augmentation (https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
- Transfer Learning (https://www.learnopencv.com/keras-tutorial-transfer-learning-using-pre-trained-models/)
Other ideas?

## GPU on AWS

```
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp27-none-linux_x86_64.whl
sudo pip install --upgrade $TF_BINARY_URL
```

