#include "mydialog.h"
#include "ui_mydialog.h"
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

MyDialog::MyDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::MyDialog)
{
    ui->setupUi(this);
}

MyDialog::~MyDialog()
{
    delete ui;
}

void MyDialog::on_ConfirmButton_clicked()
{
    bool    ok;

    //用来传输卷积核长度的类
    QString tempLen;

    //用来传输卷积核宽度的类
    QString tempWide;

    //接收用户输入的长度
    QString valueLen = ui->Len_lineEdit->text();

    //接收用户输入的宽度
    QString valueWide = ui->Wide_lineEdit->text();

    //将长度值和宽度值转换成整型
    int     LenInt  =   valueLen.toInt(&ok);
    int     WideInt =   valueWide.toInt(&ok);

    //如果没有设定卷积核或卷积核输入非法
    if((LenInt == 0)||(WideInt == 0))
    {
        //重置卷积核大小为默认值
        LenInt  = 3;
        WideInt = 3;
    }

    //开始获取视频
    VideoCapture    capture(0);

    while(1)
    {
        Mat frame;
        Mat dst;

        //获取视频信息
        capture >> frame;

        //进行均值滤波
        blur(frame,dst,Size(LenInt,WideInt));

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
