import PointPicker
import ProjectiveDistortion
import DrawPolygon
import ProjectiveRectification
import OpenCVRectification

def main():
    pointsEuc = PointPicker.PointPicker()
    pointsDis = ProjectiveDistortion.ProjectiveDistortion(pointsEuc)
    DrawPolygon.DrawPolygon(pointsDis)
    Hp = ProjectiveRectification.ProjectiveRectification(pointsDis)
    print('The projective rectification is ')
    print(Hp)
    H = OpenCVRectification.OpenCVRectification(pointsDis, pointsEuc)
    print('The homography is ')
    print(H)
if __name__=="__main__":
    main()
