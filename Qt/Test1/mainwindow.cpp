#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

const static double PI=3.1416;
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

void MainWindow::on_pushButton_clicked()
{
    bool ok;
    QString tempStr;
    QString valueStr=ui->radius_lineEdit->text ();
    int valueInt=valueStr.toInt(&ok);
    double area =valueInt*valueInt*PI;
    ui->Area_lineEdit->setText(tempStr.setNum(area));

}

void MainWindow::on_radius_lineEdit_textChanged(const QString &arg1)
{
    bool ok;
    QString tempStr;
    QString valueStr=ui->radius_lineEdit->text ();
    int valueInt=valueStr.toInt(&ok);
    double area =valueInt*valueInt*PI;
    ui->Area_lineEdit->setText(tempStr.setNum(area));


}
