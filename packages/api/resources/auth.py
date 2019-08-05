from resources import Resource
from services import ServiceManager


class AuthResource(Resource):
	route = '/user'

	def on_get(self, request, response):
		auth = ServiceManager.get('auth')
		request = auth.messages.QueryUserRequest()
		query_response = auth.currentUser(request)

		response.body = query_response.token 
