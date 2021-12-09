# Polygon Manager

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

## Features

- Create a dictionary containing polygon points
- View drawn polygons
- Get polygon points and use it anywhere


## Tech

Polygon Manager only uses a number of open source projects to work properly:

- [Numpy] 
- [OpenCV]
- [Shapely] 

And of course Polygon Manager itself is open source with a [https://github.com/memona008/Polygon_Manager][poly]
 on GitHub.

## Installation

Install the package with entering this command in command line interface

```
pip3 install polygon_manager==0.1.2
```

## Usage
#### Create an object of Polygon Manager it will create a pkl file in root folder 
```
from polygon_manager import PolygonManager
pm = PolygonManager()
```

#### To create/edit a polygon 
```
pm.create_new_polygon(camera_no='10', vid_path='/path/to/video/')
```

It will open a window with first frame of video where you can add points Clockwise or Anti-Clockwise by clicking on picture. To undo the recent added point; use right click. 

![Polygon Points](https://user-images.githubusercontent.com/43179211/143847530-2734a4f2-a94a-4456-818b-cad84e8d904f.PNG)


#### To view all polygons
```
pm.view_polygons()
```

#### To view some specific polygon pass the camera name/number
```
pm.view_polygons('10')
```

![Drawn_Polygon](https://user-images.githubusercontent.com/43179211/143847634-a0055a49-48fd-491b-bc69-27882ecc726d.PNG)


#### To delete an existing polygon 
```
pm.delete_polygon('10')
```

It will return True or False based on deletion of polygon. And will throw exception if the polygon doesn't exist


#### To check if a point lies in polygon or not 
```
pm.is_point_in_polygon(point=(1,2),polygon_name='10')
```

It will return True or False based on point position in polygon. And will throw exception if the polygon doesn't exist


#### To get polygon points to use it anywhere else 
```
pm.get_polygon_points('10')
```
For example: [[32, 667], [279, 559], [551, 462], [766, 380], [972, 286], [1191, 204], [1407, 265], [1179, 412], [955, 531], [738, 664], [513, 817], [185, 1007]]

#### To Calculate IOU/Intersection of boxes over POLYGON
***Different formats of boxes can be used
Supported formats: XYXY, XYWH***
```
pm.box_to_poly_iou(bbox_list=[[515, 149, 621, 286],[654, 159, 721, 186]], '13', mode=pm.BOX_MODE_XYXY)
pm.box_to_poly_iou(bbox_list=[[568.0000, 217.5000, 106.0000, 137.0000]], '13', mode=pm.BOX_MODE_XYWH)
```
For example: [0.08, 0.44]
             [0.78]




   [poly]: <https://github.com/memona008/Polygon_Manager>



## License
MIT
