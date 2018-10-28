#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mydialog.h"
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

//用于设置形态学滤波中的Blur函数。
void MainWindow::on_actionblur_B_triggered()
{
    D_blur = new MyDialog(this);

    D_blur->setModal(true);         //模态显示

    D_blur->show();
}
