from IpcamController import IpCamController
import time
if __name__ =="__main__":
    client =  IpCamController()

    ip = '192.168.1.106'
    client.search_ip_cameras()  # search available onvif device on the network by sending probe msg

    if ip not in client.available_ipcam : # make sure the ipcam is on the network 
        print(f" {ip} is not on the network")
        exit()

    client.config(
                    ip       = ip,
                    username = 'admin',
                    password = 'test_password!'
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