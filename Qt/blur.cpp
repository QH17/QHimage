#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

int main(void)
{
    //开始获取视频
    VideoCapture    capture(0);

    while(1)
    {
        Mat frame;
        Mat dst;

        //获取视频信息
        capture >> frame;

        //进行均值滤波
        blur(frame,dst,Size(3,3));

        //对显示文字的字体进行设置
        int font_face = cv::FONT_HERSHEY_COMPLEX;  
        //对显示文字的坐标进行设置
        Point   org;
        org.x = 13;
        org.y = 18;
        //放置文字
        putText(dst,"press Q to exit.",org,font_face,0.5,cv::Scalar(20,30,200),1,8,0);
        imshow("blur",dst);

        //等待用户关闭界面
        if(waitKey(1) == 'q')
        {
            capture.release();

            destroyAllWindows();

            break;
        }
    }
}