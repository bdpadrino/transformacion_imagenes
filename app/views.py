import cv2
import numpy as np
import urllib.request

from django.shortcuts import render
from .crud import create_historial, finish_historial, add_log

#PASO1
def invert_colors(url_image):
    '''METODO PARA INVERTIR LOS COLORES DE UNA IMAGEN'''
    try:
        image = cv2.imread(url_image)
        color_inverted = np.invert(image)
        cv2.imwrite('media/output/1_color_inverted.jpg', color_inverted)
    except Exception as e:
        print("Error {} ".format(e))  
        add_log(1, e)
    
#PASO2 
def gray_scale2(url_image):
    '''METODO PARA CONVERSION DE IMAGEN EN ESCALA DE GRISES'''
    try:
        image = cv2.imread(url_image,0)
        cv2.imwrite('media/output/2_gray_scale.jpg', image)
    except Exception as e:
        print("Error {} ".format(e))  
        add_log(2,e) 
    
#PASO3
def rotate_image(url_image):
    '''METODO PARA ROTAR IMAGEN 90 GRADOS'''
    try:
        image = cv2.imread(url_image)
        ancho = image.shape[1] #columnas
        alto = image.shape[0] # filas
        M = cv2.getRotationMatrix2D((ancho//2,alto//2),90,1)
        imageOut = cv2.warpAffine(image,M,(ancho,alto))
        cv2.imwrite('media/output/3_rotation_image.jpg', imageOut)
    except Exception as e:
        print("Error {} ".format(e))  
        add_log(3,e)

#PASO4
def invert_y(url_image):
    '''METODO DE INVERSION DE IMAGENES EN EL EJE Y'''
    try:
        image = cv2.imread(url_image)
        flip = cv2.flip(image,1)
        cv2.imwrite('media/output/4_invert_y.jpg', flip)
    except Exception as e:
        print("Error {} ".format(e))  
        add_log(4,e)
        
def process_image(url_image, id_img):
    '''METODO PRINCIPAL PARA EL MANEJO DE LA IMAGEN'''
    #serializer.data['id']
    if 'http' in url_image:
        req = urllib.request.urlopen(url_image)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1) # 'Load it as it is'
        cv2.imwrite('media/output/0_original.jpg', img)
        url_image = 'media/output/0_original.jpg'

    step = 1
    create_historial(id_img, step)
    invert_colors(url_image)
    finish_historial(id_img, step)

    step = 2
    create_historial(id_img, step)
    gray_scale2('media/output/1_color_inverted.jpg')
    finish_historial(id_img, step)

    step = 3
    create_historial(id_img, step)
    rotate_image('media/output/2_gray_scale.jpg')
    finish_historial(id_img, step)

    step = 4
    create_historial(id_img, step)
    invert_y('media/output/3_rotation_image.jpg')
    finish_historial(id_img, step)

def principal(request):
    #process_image('media/guacamayos.jpg', 1) 
    #process_image('C:\\Users\\e10375\\Downloads\\Guacamayas2.jpg', 1) 
    process_image('https://variety.com/wp-content/uploads/2021/12/doctor-strange.jpg?w=681&h=383&crop=1&resize=681%2C383', 1) 
    
    return render(request,"app/test.html",{})


