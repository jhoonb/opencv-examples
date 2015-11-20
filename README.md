
### Python usado: Python3.4 (OpenCV não compativel ainda com Python3.5)

### Bibliotecas analisadas. 


- OpenCV - http://docs.opencv.org/3.0-last-rst/ # em uso
- Mahotas - http://mahotas.rtfd.org / https://github.com/luispedro/mahotas # mesma funcionalidade do pillows, é mais simples de usar.
- SimpleCV - http://tutorial.simplecv.org/en/latest/ # Apenas Python 2 :(
- Numpy - https://docs.scipy.org/doc/numpy/reference/ # algoritmos dessa biblioteca são usados no core do OpenCV

### OpenCV básico. 

- importando a biblioteca:
```python
import cv2
```

- carregando uma imagem
```python
image = cv2.imread('caminho/da/imagem/imagem.jpg')
```

- salvando [escrevendo] uma imagem
```python
cv2.imwrite('caminho/da/imagem/imagem.jpg', image) # retorna bool
```

- recuperando um pixel da imagem (técnica de slicing)
```python
pixel = image[0, 0] # retorna um numpy.adarray(R, G, B)
```

- recuperando um um dos canais RGB
```python
canal_g = image[0, 0, 1] # canais 0, 1, 2 em ordem inversa [B, G, R]
```

- recuperando uma região da imagem (técnica de slicing)
```python
parte_image = image[0:10, 0:10] # retorna um numpy.adarray
```

- recuperando uma região da imagem em um dos canais RGB especifico
```python
parte_image_R = image [0:200, 1:100, 2] # retorna um numpy.adarray
```

- recuperando a imagem completa apenas em um canal
```python
image_canal_R = image[:,:,2] # retorna um numpy.adarray
```

- informação: toda manipulação de imagem em OpenCV é feita pela biblioteca numpy (Em Python).
uma imagem é um numpy.ndarray (N-dimensional array) de 3 dimensoes> com largura, altura e canal RGB(uma tupla).
Ou seja, sempre que for feito ações sobre matrizes e vetores estará sendo usado numpy.

- Por ser usado matriz, os loops podem ser demorados, * uma ideia seria transformar uma matriz em um vetor
e utilizar tecnicas com lazy avaluation para iterar sobre dados *

- Sempre que manipular os np.adarrays utilizar a tecnica de slicing do Python ao inves de funções de acesso.
* Numpy que é o core base de OpenCV ele é otimizado para fazer slicing.

- Evitar ao máximo loops com "for" ou "while", motivo: toda vez que efetua iterações sobre arrays
com for ou while Python constroi todos os arrays na hora, causa perfomance mais baixa e cust alto de memória,
solução é usar tecnicas de programação funcional como map, reduce, all, any, list comprehension com generators & iterators
pois são lazy evaluation.
