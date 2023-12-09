# The Jerker: Olympic Weightlifting Analysis with Machine Learning

![Image]([https://i.ibb.co/tqhV5tb/imagem.png](https://www.shutterstock.com/image-vector/black-white-illustration-barbell-isolated-600nw-1291006585.jpg)https://www.shutterstock.com/image-vector/black-white-illustration-barbell-isolated-600nw-1291006585.jpg)

## Overview

The objective with this project was to build a tool to help an Olympic Wigthlifting Athlete to optimize the efficiency of their movements using Machine Learning models to analyze critical points of the technique and use it as an indicator to assess their technical work.
The tool is is used to analyze two aspects: the **bar trajectory** and the the athlet's **triple extension**,

This tool was built for Ironhack's Data Analytics Final Project.



## Technical Requirements

The requirements to run the code are in the **requirements.txt**. To install those packages just run:

```bash
pip install -r requirements.txt
```

I'll hightlight some:

* **YOLOv8**: used for object detections and tracking so the bar path trajectory line drawing was possible;
* **MediPipe**: used for pose estimations so to analyze the body positioning that would allow to calculate angles between joints and therefore check if triple extension is performed or not;
* **OpenCV**: the Open Computer Vision library supports both YOLO and Mediapipe for processing the video with the overlays for the desired analsysis.



## Tools

### Bar Trajectory

YOLOv8 pre-trained model for object detection and tracking supported by OpenCV allows to make this type of observation and analysis:

![Trajectory](https://ibb.co/nz3jRwV)

### Triple Extension Checker

MediaPipe's pose estimator allowed to track ankles, kness and hips coordinates and then calculate the angle on the with a functions made apart from that. You'll get an observation like this one:

![Not extended](https://ibb.co/SRVN4Dj)

![Perfect](https://ibb.co/zmLP71G)

### 2 Additional Features

Added the **NO Half Rep!** tool to check if the squat "breaks the parellel", also using MediaPipe pose estimator.

Also added a **1-Rep Max Calculator** to calculate the Rep Max giving the number of repetions done in a certain weight, assuming that's the maximum effort.


## Future Improvements

* Train my own models for plates and barbell detection. YOLO worked really well on this one because it's trained to detect objects with similar shapes;
* Build an App that takes as an input a recording of a movement done in a training session and output the analysis asked to help athlets and coaches to anylize and know how to aproach their technique work.

## Resources

[YOLOv8 Documentation: Plot tracks over multiple video frames](https://docs.ultralytics.com/modes/track/#persisting-tracks-loop)

[MediaPipe Documentation: Pose landmark detection guide](https://developers.google.com/mediapipe/solutions/vision/pose_landmarker#get_started)

[Youtube: AI Pose Estimation with Python and MediaPipe | Plus AI Gym Tracker Project](https://www.youtube.com/watch?v=06TE_U21FK4)

[How To Calculate and Use Your 1-Rep Max](https://www.healthline.com/health/fitness/one-rep-max-how-to-calculate-and-use)
