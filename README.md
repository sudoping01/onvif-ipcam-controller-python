# IpCamController

`IpCamController` is a Python class designed for discovering and controlling ONVIF-compatible IP cameras. It enables you to search for ONVIF devices on your network and perform essential PTZ (Pan-Tilt-Zoom) operations such as moving the camera up, down, left, and right.

## Features

- **Discover ONVIF Devices:** Automatically find ONVIF-compatible devices on the local network.
- **Connect to ONVIF Cameras:** Easily connect to an ONVIF camera using its IP address, port, username, and password.
- **Control Camera Movements:** Perform PTZ operations including moving the camera left, right, up, and down.
- **Stop Camera Motion:** Stop the camera's motion with a simple command.

## Installation

Ensure you have the necessary dependencies installed:

```sh
pip install onvif-zeep wsdiscovery
```
**Example** :

```python 
from IpCamController import IpCamController
import time

if __name__ =="__main__":
    client =  IpCamController()

    ip = '192.168.1.101'
    client.search_onvif_device()  # search available onvif device on the network by sending probe msg

    if ip not in client.available_onvif_device : # make sure the ipcam is on the network 
        print(f" {ip} is not on the network")
        exit()

    client.config(
                    ip       = ip,
                    username = 'admin',
                    password = 'TestPassword',
                    port     = 80
                  )
    

    while True: 
        choice = input(" Choice a Motion : \n l : left \n r : right \n d: down \n u: down \n : ")

        if choice == "l" : 

            client.move_left(client.ptz, client.request)
            time.sleep(0.25)
            client.stop_motion(client.ptz, client.request)
        elif choice == 'r':
            client.move_right(client.ptz, client.request)
            time.sleep(0.25)
            client.stop_motion(client.ptz, client.request)
        elif choice == "u":
            client.move_up(client.ptz, client.request)
            time.sleep(0.25)
            client.stop_motion(client.ptz, client.request)
        elif choice == "d":
            client.move_down(client.ptz, client.request)
            time.sleep(0.25)
            client.stop_motion(client.ptz, client.request)
