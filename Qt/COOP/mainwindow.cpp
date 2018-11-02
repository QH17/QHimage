#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>

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

void MainWindow::on_actionimage_P_triggered()
{

}

void MainWindow::on_actionvideo_V_triggered()
{

}

void MainWindow::on_actionblur_B_triggered()
{

}

void MainWindow::on_actionmid_M_triggered()
{

}

void MainWindow::on_actiongauss_G_triggered()
{

}

void MainWindow::on_actioncanny_C_triggered()
{

}
