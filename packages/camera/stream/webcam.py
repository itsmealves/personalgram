import cv2
from threading import Thread
from stream import StreamStrategy


class WebcamStream(StreamStrategy):
	def __init__(self, camera_id=0, width=1920, height=1080):
		self.__stream = cv2.VideoCapture(camera_id)
		self.__stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
		self.__stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

		self.__stream.read()

		self.__stopped = False
		self.__thread = Thread(target=self.__update)
		self.__thread.start()

	def __update(self):
		while not self.__stopped:
			self.__stream.grab()

	def read(self):
		_, frame = self.__stream.retrieve()
		return frame

	def read_bytes(self):
		ext = '.png'
		_, buf = cv2.imencode(ext, self.read())
		return buf.tostring(), ext

	def release(self):
		self.__stopped = True
		self.__thread.join()
		self.__stream.release()
