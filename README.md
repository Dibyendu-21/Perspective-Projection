# Perspective Projection

This repo gives a demonstration as to how to change the perspective view of an image.

## Design Pipeline
The Design pipeline is demonstrated as follows:
* Extract the ROI from the image whose perspective view needs to be changed suing mouse click event.

![ROI Image](ROI/ROI_Coordinate.png?raw=true)
* Extract the Projection area where the ROI needs to be projected to, using mouse click event.

![Projection Area](Projection%20Coordinate/Projection_Coordinate1.png?raw=true) 
* Get the perspective transformation between the two sets of points.
* Finally warp the ROI on the projected area.

![Output Image](Output/Output1.png?raw=true)
