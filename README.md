# detect-footrest-condition

## Problem and its implementation
```
We need to find out when the footrest is closed and when it is open. Only if the footrest is 100% closed, it is assigned
the label closed, else in all other cases, we have to label it as open.
Since, our camera angle is fixed, we can take this problem as an object detection problem, rather than classification
problem to better focus on the footrest only.
```

## Training
```
100 images of motorcycle were used for training, assuming that the camera angle is fixed while detection.
These images are augmented (100 times per image) using rotation, saturation, brightness, hue addition etc.
Translation and flips are not used since our camera is fixed.
This way, we have generated nearly 10,000 images for training.
Loss when the training was stopped can be seen below:
```
<img src="https://github.com/AshishGusain17/detect-footrest-condition/blob/master/tensorboard.png?raw=true" width=683 height=384>


## Results
```
Various results can be seen below:
```
<img src="https://github.com/AshishGusain17/detect-footrest-condition/blob/master/output/img2.png?raw=true" width=683 height=384>
<img src="https://github.com/AshishGusain17/detect-footrest-condition/blob/master/output/img3.png?raw=true" width=683 height=384>
<img src="https://github.com/AshishGusain17/detect-footrest-condition/blob/master/output/img6.png?raw=true" width=683 height=384>
<img src="https://github.com/AshishGusain17/detect-footrest-condition/blob/master/output/img7.png?raw=true" width=683 height=384>
<img src="https://github.com/AshishGusain17/detect-footrest-condition/blob/master/output/img9.png?raw=true" width=683 height=384>
