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

And of course Polygon Manager itself is open source with a [https://github.com/memona008/Polygon_Manager][poly]
 on GitHub.

## Installation

Install the package with entering this command in command line interface

```
pip install polygon_manager 
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




#### To get polygon points to use it anywhere else 
```
pm.get_polygon_points('10')
```
For example: [[32, 667], [279, 559], [551, 462], [766, 380], [972, 286], [1191, 204], [1407, 265], [1179, 412], [955, 531], [738, 664], [513, 817], [185, 1007]]

   [poly]: <https://github.com/memona008/Polygon_Manager>

