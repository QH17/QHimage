#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <mydialog.h>

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
    void on_actionblur_B_triggered();

private:
    Ui::MainWindow *ui;
    MyDialog    *D_blur;    //建立一个私有成员：*D_blur用于显示对话框
};

#endif // MAINWINDOW_H
