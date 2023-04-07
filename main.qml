import QtQuick 2.0
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ApplicationWindow {
    id: window
    title: qsTr("Una Reader")
    visible: true
    width: 1280
    height: 720
    Material.theme: Material.Dark
    Material.accent: Material.Red

    Item {
        width: 1280
        height: 720

        TabBar {
            id: menuBar
            width: parent.width
            
            TabButton {
                text: qsTr("Recent")
            }
            TabButton {
                text: qsTr("All Books")
            }
            TabButton {
                text: qsTr("Collections")
            }
        }

        StackLayout {
            width: parent.width
            currentIndex: menuBar.currentIndex

            anchors.top : menuBar.bottom
            anchors.margins: 10
            
            Flow {
                id: homeTab

                Item 
                {
                    width: 15
                    height: 15
                }

                /*BookGrid
                {
                    id : currentBookGrid
                }*/

                Text {
                    
                    textFormat: Text.RichText
                    text: "<h1>…Can't upload the file to the cloud?</h1> <p>Han Sooyoung hurriedly checked her Stigma several times at that sudden message.</p>"
                    color: "white"

                    function updateText(newText) 
                    {
                        text = newText
                        return null
                    }
                }

                Item 
                {
                    width: 15
                    height: 15
                }
            }
            Item {
                id: discoverTab
                
                Rectangle {
                    width: 100
                    height: 100
                    color: "red"
                    border.color: "black"
                    border.width: 5
                    radius: 10
                }
            }
            Item {
                id: activityTab

                Rectangle {
                    width: 100
                    height: 100
                    color: "black"
                    border.color: "black"
                    border.width: 5
                    radius: 10
                }
            }
        }
    }
}

