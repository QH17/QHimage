#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actionimage_P_triggered();

    void on_actionvideo_V_triggered();

    void on_actionblur_B_triggered();

    void on_actionmid_M_triggered();

    void on_actiongauss_G_triggered();

    void on_actioncanny_C_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
