/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.11.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionimage_P;
    QAction *actionvideo_V;
    QAction *actionblur_B;
    QAction *actionmid_M;
    QAction *actiongauss_G;
    QAction *actioncanny_C;
    QAction *actionfind_contours_C;
    QAction *actionhuamn_detect_H;
    QAction *actioncamera_on_O;
    QWidget *centralWidget;
    QPushButton *DrawButton;
    QLabel *label;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;
    QMenuBar *menuBar;
    QMenu *menu_O;
    QMenu *menu_B;
    QMenu *menu_F;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(600, 400);
        MainWindow->setMinimumSize(QSize(600, 400));
        MainWindow->setMaximumSize(QSize(600, 400));
        actionimage_P = new QAction(MainWindow);
        actionimage_P->setObjectName(QStringLiteral("actionimage_P"));
        actionvideo_V = new QAction(MainWindow);
        actionvideo_V->setObjectName(QStringLiteral("actionvideo_V"));
        actionblur_B = new QAction(MainWindow);
        actionblur_B->setObjectName(QStringLiteral("actionblur_B"));
        actionmid_M = new QAction(MainWindow);
        actionmid_M->setObjectName(QStringLiteral("actionmid_M"));
        actiongauss_G = new QAction(MainWindow);
        actiongauss_G->setObjectName(QStringLiteral("actiongauss_G"));
        actioncanny_C = new QAction(MainWindow);
        actioncanny_C->setObjectName(QStringLiteral("actioncanny_C"));
        actionfind_contours_C = new QAction(MainWindow);
        actionfind_contours_C->setObjectName(QStringLiteral("actionfind_contours_C"));
        actionhuamn_detect_H = new QAction(MainWindow);
        actionhuamn_detect_H->setObjectName(QStringLiteral("actionhuamn_detect_H"));
        actioncamera_on_O = new QAction(MainWindow);
        actioncamera_on_O->setObjectName(QStringLiteral("actioncamera_on_O"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        DrawButton = new QPushButton(centralWidget);
        DrawButton->setObjectName(QStringLiteral("DrawButton"));
        DrawButton->setGeometry(QRect(480, 290, 93, 28));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(20, 20, 400, 300));
        label->setMinimumSize(QSize(400, 300));
        label->setMaximumSize(QSize(400, 300));
        label->setFrameShape(QFrame::Box);
        label->setFrameShadow(QFrame::Sunken);
        MainWindow->setCentralWidget(centralWidget);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 600, 26));
        menu_O = new QMenu(menuBar);
        menu_O->setObjectName(QStringLiteral("menu_O"));
        menu_B = new QMenu(menuBar);
        menu_B->setObjectName(QStringLiteral("menu_B"));
        menu_F = new QMenu(menuBar);
        menu_F->setObjectName(QStringLiteral("menu_F"));
        MainWindow->setMenuBar(menuBar);

        menuBar->addAction(menu_O->menuAction());
        menuBar->addAction(menu_B->menuAction());
        menuBar->addAction(menu_F->menuAction());
        menu_O->addAction(actionimage_P);
        menu_O->addAction(actionvideo_V);
        menu_B->addAction(actionblur_B);
        menu_B->addAction(actionmid_M);
        menu_B->addAction(actiongauss_G);
        menu_B->addAction(actioncanny_C);
        menu_F->addAction(actionfind_contours_C);
        menu_F->addAction(actionhuamn_detect_H);
        menu_F->addAction(actioncamera_on_O);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionimage_P->setText(QApplication::translate("MainWindow", "image(&P)", nullptr));
        actionvideo_V->setText(QApplication::translate("MainWindow", "video(&V)", nullptr));
        actionblur_B->setText(QApplication::translate("MainWindow", "blur(&B)", nullptr));
        actionmid_M->setText(QApplication::translate("MainWindow", "mid(&M)", nullptr));
        actiongauss_G->setText(QApplication::translate("MainWindow", "gauss(&G)", nullptr));
        actioncanny_C->setText(QApplication::translate("MainWindow", "canny(&C)", nullptr));
        actionfind_contours_C->setText(QApplication::translate("MainWindow", "find contours(&C)", nullptr));
        actionhuamn_detect_H->setText(QApplication::translate("MainWindow", "huamn detect(&H)", nullptr));
        actioncamera_on_O->setText(QApplication::translate("MainWindow", "camera on(&O)", nullptr));
        DrawButton->setText(QApplication::translate("MainWindow", "\346\211\223\345\274\200\347\224\273\346\235\277", nullptr));
        label->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        menu_O->setTitle(QApplication::translate("MainWindow", "\346\211\223\345\274\200(&O)", nullptr));
        menu_B->setTitle(QApplication::translate("MainWindow", "\345\275\242\346\200\201\345\255\246\345\244\204\347\220\206(&B)", nullptr));
        menu_F->setTitle(QApplication::translate("MainWindow", "\345\212\237\350\203\275(&F)", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
