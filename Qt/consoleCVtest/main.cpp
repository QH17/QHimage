#include <QCoreApplication>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>

using namespace cv;

Rect        g_rectangle;
bool        g_dDrawingBox = false;
RNG         g_rng(12345);

void DrawRectangle( cv::Mat& img, cv::Rect box);
void ShowHelpText();
void on_MouseHandle(int event, int x, int y, int flags, void* param);


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    g_rectangle = Rect(-1,-1,0,0);

    Mat srcImage(600,800,CV_8UC3), tempImage;

    srcImage.copyTo(tempImage);

    g_rectangle = Rect(-1,-1,0,0);
    srcImage = Scalar::all(0);

    namedWindow("WINDOW_NAME");
    setMouseCallback("WINDOW_NAME",on_MouseHandle,(void*)&srcImage);

    while(1)
    {
        srcImage.copyTo(tempImage);

        if(g_dDrawingBox )
        {
            DrawRectangle(tempImage,g_rectangle);
        }

        imshow( "WINDOW_NAME",tempImage);

        if(waitKey(10) == 'q')
        {
            destroyAllWindows();
            break;
        }
    }
    return a.exec();
}

void on_MouseHandle(int event, int x, int y, int flags, void* param)
{
    Mat& image = *(cv::Mat*) param;
    switch(event)
    {
        case EVENT_MOUSEMOVE:
        {
            if(g_dDrawingBox)
            {
                g_rectangle.width = x-g_rectangle.x;
                g_rectangle.height = y-g_rectangle.y;
            }
        }
        break;

        case EVENT_LBUTTONDOWN:
        {
            g_dDrawingBox = true;
            g_rectangle = Rect(x,y,0,0);
        }
        break;

        case EVENT_LBUTTONUP:
        {
            g_dDrawingBox = false;

            if(g_rectangle.width < 0)
            {
                g_rectangle.x += g_rectangle.width;
                g_rectangle.width *= -1;
            }

            if(g_rectangle.height < 0)
            {
                g_rectangle.y += g_rectangle.height;
                g_rectangle.height *= -1;
            }

            DrawRectangle(image, g_rectangle);
        }
        break;
    }
}

void DrawRectangle( cv::Mat& img, cv::Rect box)
{
    rectangle(img,box.tl(),box.br(),Scalar(g_rng.uniform(0,255),
                                           g_rng.uniform(0,255),
                                           g_rng.uniform(0,255)));
}
