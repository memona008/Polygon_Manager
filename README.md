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

#### To view all polygons
```
pm.view_polygons()
```

#### To view some specific polygon pass the camera name/number
```
pm.view_polygons('10')
```

#### To get polygon points to use it anywhere else 
```
pm.get_polygon_points('10')
```

   [poly]: <https://github.com/memona008/Polygon_Manager>

