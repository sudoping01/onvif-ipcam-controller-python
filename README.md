# IpCamController

## Overview

`IpCamController` is a Python class designed to search for ONVIF compatible devices on the network, control IP cameras, and perform motion operations. This class uses various libraries including `onvif_zeep` and `WSDiscovery` to facilitate these functionalities.

## Features

- **Search for IP Cameras**: Discover ONVIF compatible IP cameras on the local network.
- **Control Camera Movement**: Perform pan and tilt operations including move up, down, left, and right.
- **Continuous Move and Stop**: Execute continuous movements and stop the camera motion as needed.
- **Configuration**: Configure the camera with IP, username, and password for establishing a connection.

## Requirements

- `WSDiscovery`
- `onvif_zeep`
- `zeep`

## Installation

To install the required libraries, you can use `pip`:

```bash
pip install -r requirements.txt 
