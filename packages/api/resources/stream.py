import mimetypes
from resources import Resource
from services import ServiceManager


class StreamResource(Resource):
    route = '/stream'

    def __generator(self, frame_response):
        return (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_response.data + b'\r\n\r\n')

    def on_get(self, request, response):
        camera = ServiceManager.get('camera')
        stream_response = camera.getStream(camera.messages.StreamRequest())

        response.content_type = 'multipart/x-mixed-replace; boundary=frame'
        response.stream = map(self.__generator, stream_response)
