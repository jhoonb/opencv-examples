#
# testes para reconhecer se uma imagem é preta ou branca
# exemplos força bruta e com matriz minima (grid sobre imagem principal)
# usando diversos loops e abordagens
# experiencias com usa do numpy e opencv
#
"""
para reconhecer se uma imagem é preta (TOTALMENTE)
é necessário verificar se cada pixel (canal rgb)
tenha o valor 0. Cada ponto na imagem é um vetor
com valor (0, 0, 0), podemos aceitar um valor entre
0 e 5, em qualquer canal e pixel para ser a imagem preta.
Dependendo o tamanho da imagem a matriz para se processar
é muito custosa, processo:
pega a matriz 3-D transforma em um array 1-D
e verifica se todos os elementos estão entre 0 e 1.
[força bruta]...

tempo:
identificar imagem preta:
1 loops, best of 3: 21.6 s per loop

identificar q não é preta:
1 loops, best of 3: 4.41 s per loop
==============
outro método, é no lugar de analisar a matriz num todo
apenas verificamos um canal de cada vez dos 3 que existem.

matrix - 3D, - > matrix 2-D -> array 1-D.

tempo:
identificar imagem preta:
1 loops, best of 3: 27.6 s per loop

identificar q não é preta:
1 loops, best of 3: 1.88 s per loop

=================
link: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate

método lendo a matrix toda porem usando generator, iterators e high order function
usando ndenumerate: (loop na matriz) generator.
tempo:
identificar imagem preta:
1 loops, best of 3: 26.4 s per loop

identificar q não é preta:
1 loops, best of 3: 5.36 s per loop

==================
método lendo a matrix toda porem usando loop em
cima matrix (loop for normal)

tempo:
identificar imagem preta:
1 loops, best of 3: 24.5 s per loop

identificar q não é preta:
1 loops, best of 3: 5.07 s per loop

==========================
usando list comprehension e high order function(all, map, etc...), com np.nditer

tempo:
identificar imagem preta:
1 loops, best of 3: 16.7 s per loop

identificar q não é preta:
1 loops, best of 3: 3.53 s per loop

==========================
usando loop normal (for) com np.nditer

tempo:
identificar imagem preta:
1 loops, best of 3: 16.8 s per loop

identificar q não é preta:
1 loops, best of 3: 3.57 s per loop


============================
usando a função is_black() só com list comprehension

identificar imagem NÃO preta:
10 loops, best of 3: 141 ms per loop

identificar imagem preta:
10 loops, best of 3: 144 ms per loop


============================
usando a função is_black() só com map, reduce, filter

identificar imagem NÃO preta:
In [5]: %timeit z = r.is_black(d.format('16'))
10 loops, best of 3: 141 ms per loop

identificar imagem preta:
In [6]: %timeit z = r.is_black(d.format('1'))
10 loops, best of 3: 144 ms per loop
"""

import numpy as np
import cv2

# DON'T TOUCH
def _check_all_255(line):
	"""
	R,G,B -> (x, x, x) -> white
	x between 245 and 250
	"""
	_check_255 = lambda x: x >= 245 and x <= 255
	# matrix to array
	line = np.asarray(line).ravel()
	return all(map(_check_255, line))


def _check_all_0(line):
	"""
	R,G,B -> (x, x, x) -> black
	x between 0 and 5
	"""
	_check_0 = lambda x: x >= 0 and x <= 5
	# matrix to array
	line = np.asarray(line).ravel()
	return all(map(_check_0, line))


class Recognize(object):
	"""
	algorithm idea:
	1) take a picture and select a set of horizontal lines and vertical lines.
	like a "grid", now, just check if ALL pixels (R,G,B array) in grid
	using function _check_all_0 is True (for black)
	Recognize:

	rec = Recognize()
	rec.is_black('/home/pic/image.jpg') => True or False
	rec.is_white('/home/pic/image.jpg') => True or False

	and [optional]:
	rec.beta = 0.08
	rec.save_image('/home/folder/folder', 'photo.jpg')

	"""

	def __init__(self):
		# how bigger it's the beta number,
		# fewer lines do you have for recognize
		# less lines more fast.
		# beta 0.07 empirical test
		self.beta = 0.07 # 0.01: slow and >= 0.09 probably false positive
		self._image = None


	def _image_color(self, image_path, color):
		"""
		Return True if the image is [white or black]
		:param image_path: string with path for file
		:type image_path: str
		:param color: string with value "white" or "black"
		:type color: str
		:returns: True or False
		:rtype: bool
		"""
		# define function
		if color == 'black':
			_func = _check_all_0
		else:
			_func = _check_all_255

		# open image
		self._image = cv2.imread(image_path)
		# get length colunns and rows
		ncols, nrows, _ = self._image.shape
		# get step to make the grid
		cols_step = int(ncols * self.beta)
		rows_step = int(nrows * self.beta)
		# get array of pixels in the image
		cols_px = (i for i in range(1, ncols, cols_step))
		rows_px = (i for i in range(1, nrows, rows_step))
		# change channel 0, 1, 2 -> (B, G, R)
		chan = lambda c: {0: 1, 1: 2, 2: 0}[c]
		# colunns
		ch = 2
		# all((_func(self._image[px:px+1, 0:ncols, chan(ch)]) for px in cols_px))
		for px in cols_px:
			ch = chan(ch)
			line = self._image[px:px+1, 0:ncols, ch]
			result = _func(line)
			if not result:
				return False

		# rows
		ch = 2
		# all((_func(self._image[0:nrows, px:px+1, chan(ch)]) for px in rows_px))
		for px in rows_px:
			ch = chan(ch)
			line = self._image[0:nrows, px:px+1, ch]
			result = _func(line)
			if not result:
				return False

		return True

	def is_black2(self, image_path):
		"""
		brutal force...
		"""
		_check_0 = lambda x: x >= 0 and x <= 5
		self._image = cv2.imread(image_path)
		array = np.asarray(self._image).ravel()
		return all(map(_check_0, array))

	def is_black3(self, image_path):
		"""
		brutal force...
		"""
		_check_0 = lambda x: x >= 0 and x <= 5
		self._image = cv2.imread(image_path)

		b = self._image[:, :, 0]
		g = self._image[:, :, 1]
		r = self._image[:, :, 2]

		array = np.asarray(b).ravel()
		resp = all(map(_check_0, array))
		if not resp:
			return False

		array = np.asarray(g).ravel()
		resp = all(map(_check_0, array))
		if not resp:
			return False

		array = np.asarray(r).ravel()
		resp = all(map(_check_0, array))
		if not resp:
			return False

		return True

	def is_black4(self, image_path):
		"""
		brutal force...
		"""
		_check_0 = lambda x,y: y >= 0 and y <= 5
		self._image = cv2.imread(image_path)
		#x, y, _ = self._image.shape
		resp = all((_check_0(i,j) for i,j in np.ndenumerate(self._image)))
		#array = np.asarray(self._image).ravel()
		return resp


	def is_black5(self, image_path):
		"""
		brutal force...
		"""
		_check_0 = lambda y: y >= 0 and y <= 5
		self._image = cv2.imread(image_path)
		for i,j in np.ndenumerate(self._image):
			resp = _check_0(j)
			if not resp:
				return False

		return True

	def is_black6(self, image_path):
		"""
		brutal force...
		"""
		_check_0 = lambda y: y >= 0 and y <= 5
		self._image = cv2.imread(image_path)
		return all((_check_0(x) for x in np.nditer(self._image, order='C')))


	def is_black7(self, image_path):
		"""
		brutal force...
		"""
		_check_0 = lambda y: y >= 0 and y <= 5
		self._image = cv2.imread(image_path)
		for x in np.nditer(self._image, order='C'):
			resp = _check_0(x)
			if not resp:
				return False
		return True

	def is_white(self, image_path):
		"""
		Return True if the image is white
		:param image_path: string with path for file
		:type image_path: str
		:returns: True or False
		:rtype: bool
		"""
		return self._image_color(image_path, "white")

	def is_black(self, image_path):
		"""
		Return True if the image is black
		:param image_path: string with path for file
		:type image_path: str
		:returns: True or False
		:rtype: bool
		"""
		return self._image_color(image_path, "black")

	def save_image(self, path, name):
		"""
		Save image in path
		:param path: path for file
		:type path: str
		:param name: file name
		:type name: str
		:returns: True or False
		:rtype: bool
		"""
		return cv2.imwrite(path+name, self._image)
