from resources import Resource
from services import ServiceManager


class NoteResource(Resource):
	route = '/notes'

	def on_get(self, request, response):
		camera = ServiceManager.get('camera')
		frame_response = camera.getFrame(camera.messages.FrameRequest())
		
		with open('image' + frame_response.type, 'wb') as f:
			f.write(frame_response.data)

		response.body = 'OK'

