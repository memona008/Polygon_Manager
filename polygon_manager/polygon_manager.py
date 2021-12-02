from shapely.geometry import Point
from shapely.geometry import Polygon
import os.path
import cv2
import numpy as np
import pickle
from polygon_manager.pickle_handler import load_pickle, save_pickle
class PolygonManager:
    '''
    class to manage the points for a polygon
    '''
    def __init__(self, windowname="Capture Polygon Points in clock or anti-clock wise", polygons_file_name="polygons_config.pkl"):
        self.windowname = windowname
        self.points = []
        self.polygons_file_name = polygons_file_name
        # if file does not exist, create one with empty dict
        if not os.path.exists(self.polygons_file_name):
            save_pickle(self.polygons_file_name,{})


    def create_new_polygon(self, camera_no, vid_path):
        if camera_no and vid_path:
            self.img = self.__get_first_frame(vid_path)
            self.img1 = self.img.copy()
            cv2.namedWindow(self.windowname, cv2.WINDOW_GUI_NORMAL)

        self.polygons_dict = load_pickle(self.polygons_file_name)
        points, event  = self.__draw_polygon_points(camera_no, vid_path)
        self.points = []
        if event == 32: # SPACE PRESSED
            self.__save_polygon(camera_no, vid_path, self.img1, points)


    def __get_first_frame(self, videofile):
        vidcap = cv2.VideoCapture(videofile)
        success = False
        while not success:
            success, image = vidcap.read()
        if success:
            return image
        return None


    def __click_event(self, event, x, y, flags, params):
        font = cv2.FONT_HERSHEY_SIMPLEX
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append([x, y])
        elif event == cv2.EVENT_RBUTTONDOWN:
            if len(self.points):
                self.points.pop()

        if self.img1 is not None:
            drawn_frame = self.img1.copy()
            if len(self.points) >=1:
                x = self.points[0][0]
                y = self.points[0][1]
                cv2.putText(drawn_frame, "Press Space to save...", (10, 20), font,
                            0.5, (255, 0, 0), 2)
                cv2.putText(drawn_frame, "Press any other key to cancel...", (10, 40), font,
                            0.5, (255, 0, 0), 2)
                cv2.putText(drawn_frame, str(x) + ',' + str(y), (x, y), font,
                            1, (255, 0, 0), 2)
            if len(self.points) >= 2:
                for i in range(1,len(self.points)):
                    x = self.points[i][0]
                    y = self.points[i][1]
                    cv2.putText(drawn_frame, str(x) + ',' +
                                str(y), (x, y), font,
                                1, (255, 0, 0), 2)
                    drawn_frame = cv2.line(drawn_frame, self.points[i-1], self.points[i],color=(255, 0, 0),thickness=2)

            cv2.imshow(self.windowname, drawn_frame)


    def __draw_polygon_points(self, camera_no, vid_path):
        '''
        returns : A list of points that creates a polygon
        '''
        if not camera_no and not vid_path:
            raise Exception("Please provide video link and camera name/number")
        cv2.imshow(self.windowname, self.img)
        cv2.setMouseCallback(self.windowname, self.__click_event)
        k = cv2.waitKey(0)
        cv2.destroyAllWindows()
        return self.points, k

    def __get_drawn_polygon(self, pic, pts, color=(0, 255, 0)):
        if type(pts) is dict:
            pts_arr = pts.values()
        else:
            pts_arr = [pts]

        image = pic
        for pts in pts_arr:
            pts = np.array(pts, np.int32)
            pts = pts.reshape((-1, 1, 2))
            is_closed = True
            thickness = 2
            image = cv2.polylines(pic, [pts],
                                  is_closed, color,
                                  thickness)

        return image

    def __save_polygon(self, key, link, image, polygon):
        self.polygons_dict[key] = {
            'polygon':polygon,
            'image': image,
            'vid_link': link
        }
        with open(self.polygons_file_name, 'wb') as handle:
            pickle.dump(self.polygons_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def get_polygon_points(self, camera_no):
        polygons_dict = load_pickle(self.polygons_file_name)
        if camera_no in polygons_dict.keys():
            pts = polygons_dict[f'{camera_no}']['polygon']
            return pts

        raise Exception(f"No polygon is present for camera {camera_no}")


    def view_polygons(self, camera_no=None):
        polygons_dict = load_pickle(self.polygons_file_name)
        if camera_no in polygons_dict.keys():
            image = polygons_dict[f'{camera_no}']['image']
            link = polygons_dict[f'{camera_no}']['vid_link']
            pts  = polygons_dict[f'{camera_no}']['polygon']
            image = self.__get_drawn_polygon(image,pts,(0,0,255))
            cv2.imshow(f"{camera_no}", image)
            cv2.waitKey(0)
        elif not camera_no:
            for camera_no in polygons_dict.keys():
                image = polygons_dict[camera_no]['image']
                link = polygons_dict[camera_no]['vid_link']
                pts = polygons_dict[camera_no]['polygon']
                image = self.__get_drawn_polygon(image, pts, (0, 0, 255))
                cv2.imshow(f"{camera_no}", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        else:
            raise Exception(f"No polygon is present for camera {camera_no}")



    def is_point_in_polygon(self, point, polygon_name):
        polygons_dict = load_pickle(self.polygons_file_name)
        if polygon_name in polygons_dict.keys():
            polygon = polygons_dict[f'{polygon_name}']['polygon']
            _point = Point(point)
            _polygon = Polygon(polygon)
            return _polygon.contains(_point)
        else:
            raise Exception(f"No polygon is present for camera {polygon_name}")


    def delete_polygon(self, polygon_name):
        polygons_dict = load_pickle(self.polygons_file_name)
        if polygon_name in polygons_dict.keys():
            del polygons_dict[polygon_name]
            save_pickle(self.polygons_file_name,polygons_dict)
            return False if polygon_name in polygons_dict.keys() else True
        else:
            raise Exception(f"No polygon with name {polygon_name} exists in file")















