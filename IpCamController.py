from onvif import ONVIFCamera
import zeep

class IpCamController:
    def __init__(self, ip, port, username, password):
        self.ip             = ip
        self.port           = port
        self.username       = username
        self.password       = password
        self.XMAX           =  1
        self.XMIN           = -1
        self.YMAX           =  1
        self.YMIN           = -1

        self.request        = None 
        self.ptz            = None 


    def zeep_pythonvalue(self, xmlvalue):
        return xmlvalue


    def perform_move(self, ptz, request):
        ptz.ContinuousMove(request)


    def stop_motion(self,ptz,request):
        ptz.Stop({'ProfileToken': request.ProfileToken})


    def move_up(self, ptz, request):
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMAX
        self.perform_move(ptz, request)


    def move_down(self, ptz, request):
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMIN
        self.perform_move(ptz, request)


    def move_right(self, ptz, request):
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request)


    def move_left(self, ptz, request):
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request)

    def zoom_up(self, ptz, request):
        print('Zoom up')
        request.Velocity.Zoom.x = 1
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request)

    def zoom_down(self, ptz, request):
        print('Zoom down')
        request.Velocity.Zoom.x = -1
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request)

    def config(self):
        camera = ONVIFCamera(self.ip, self.port, self.username, self.password)
        media = camera.create_media_service()
        self.ptz = camera.create_ptz_service()

        zeep.xsd.simple.AnySimpleType.pythonvalue = self.zeep_pythonvalue
        media_profile = media.GetProfiles()[0]

        self.request = self.ptz.create_type('GetConfigurationOptions')
        self.request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = self.ptz.GetConfigurationOptions(self.request)

        self.request = self.ptz.create_type('ContinuousMove')
        self.request.ProfileToken = media_profile.token
        self.ptz.Stop({'ProfileToken': media_profile.token})

        if self.request.Velocity is None:
            self.request.Velocity = self.ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            self.request.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
            # Ensure Zoom is initialized
            if self.request.Velocity.Zoom is None:
                self.request.Velocity.Zoom = self.ptz.GetStatus({'ProfileToken': media_profile.token}).Position.Zoom
                if len(ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace) != 0:  # make sure that the camera supporte zoom
                    self.request.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        self.XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

