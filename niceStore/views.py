from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from collections import OrderedDict
import base64
import cv2
import numpy as np


def index(request):
    return render(request, 'index.html')


def get_img_tag(img):
    image_bytes = cv2.imencode('.jpg', img)[1].tobytes()
    data_uri = base64.b64encode(image_bytes).decode('utf-8')
    img_tag = f"data:image/png;base64, {data_uri}"

    return img_tag


def nofilter(request):
    image = cv2.imread("data\car.jpg")
    img_tag = get_img_tag(image)

    context = {
        'flag': 'nofilter',
        'img_tag': img_tag,
    }

    return render(request, 'blurring.html', context)


def blurring(request):

    image = cv2.imread("data\car.jpg")
    image_blurred = cv2.blur(image, (11, 11))
    img_tag_blurred = get_img_tag(image_blurred)
    # print(img_tag)
    context = {
        'flag': 'blurred',
        'img_tag_blurred': img_tag_blurred,
    }
    return render(request, 'blurring.html', context)


def hsv(request):

    image = cv2.imread("data\car.jpg")
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    img_hsv_tag = get_img_tag(image_hsv)
    # print(img_tag)
    context = {
        'flag': 'hsv',
        'img_tag_blurred': img_hsv_tag,
    }
    return render(request, 'blurring.html', context)


def gray(request):

    image = cv2.imread("data\car.jpg", 0)
    img_tag = get_img_tag(image)
    # print(img_tag)
    context = {
        'flag': 'gray',
        'img_tag_blurred': img_tag,
    }
    return render(request, 'blurring.html', context)


def matrix(request):

    def gammaTransform(img, gamma):
        norm_img = img.copy()
        norm_img = norm_img / 255
        norm_img = norm_img ** gamma
        norm_img = np.uint8(norm_img * 255)

        return norm_img

    def matrixEffect(img):
        R = img[:, :, 0]
        G = img[:, :, 1]
        B = img[:, :, 2]

        res_R = gammaTransform(R, 3/2)
        res_G = gammaTransform(G, 4/5)
        res_B = gammaTransform(B, 3/2)

        res = np.stack([res_R, res_G, res_B], axis=2)
        res = res.astype(np.uint8)

        return res

    image = cv2.imread("data\car.jpg")
    image_matrix = matrixEffect(image)
    img_matrix_tag = get_img_tag(image_matrix)
    # print(img_tag)
    context = {
        'flag': 'matrix',
        'img_tag_blurred': img_matrix_tag,
    }
    return render(request, 'blurring.html', context)
