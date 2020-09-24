import math as m
import time as t

from PIL import Image


def fractal_builder(set_type, max_iter, exponent,
                    const_real = 0, const_imaginary = 0,
                    img_w = 900, img_h = 900,
                    x_begin = -2.5, x_end = 1.5,
                    y_begin = -2, y_end = 2):
    """
    fractal_builder(set_type, max_iter, exponent,
                    const_real = 0, const_imaginary = 0,
                    img_w = 900, img_h = 900,
                    x_begin = -2.5, x_end = 1.5,
                    y_begin = -2, y_end = 2)):

    set_type - type of the set you want to build, possible variables :
               'mandelbrot' or 'julia';
    max_iter - maximum number of iterration (z_k = z_(k-1)**(exponent) + c);
    exponent - the number of exponent for z_k = z_(k-1)**(exponent) + c;
    const_real, const_imaginary - real and imaginary parts, needed only for the
                                  julia set constant;
    img_w, img_h - the resolution of an image: img_w x img_h;
    x_begin, x_end - x є [x_begin; x_end];
    y_begin, y_end - y є [y_begin; y_end].

    """

    start = t.time()

    image = Image.new("RGB", (img_w, img_h))
    z = 0

    if set_type != 'mandelbrot' and set_type != 'julia':
        raise Exception('ERROR! Wrong type of set was inputted.')

    for x in range(img_w):
        real = x * (x_end - x_begin) / (img_w - 1) + x_begin
        for y in range(img_h):
            imaginary = y * (y_end - y_begin) / (img_h - 1) + y_begin
            z = complex(real, imaginary)
            if set_type == 'mandelbrot':
                c = z
            elif set_type == 'julia':
                c = complex(const_real, const_imaginary)
            for i in range(max_iter):
                if abs(z) > 2:
                    break
                z = z**(exponent) + c
            image.putpixel((x, y), (i * 16, i * 8, i * 4))
            #image.putpixel((x, y), (i * 8, i * 4, i * 2))

    stop = t.time()
    execution_time = stop - start
    print('Program building {} set [z^({}) + c], {}x{} pixels, '
          'with {} maximum iterations '
          'execution time: {}.'.format(set_type, exponent,
                                       img_w, img_h, max_iter, execution_time))
    if set_type == 'mandelbrot':
        image.save('{}_{}_{}.bmp'.format(set_type, exponent, max_iter), 'bmp')
    elif set_type == 'julia':
        image.save('{}_{}_{}_r={}_i={}.bmp'.format(set_type, exponent, max_iter,
                                                   const_real, const_imaginary),
                   'bmp')
    fractal = image.show()

    return fractal


fractal_builder('mandelbrot',100,2)
#fractal_builder('mandelbrot',10,2)
#fractal_builder('mandelbrot',25,2)
#fractal_builder('mandelbrot',100,2)
#fractal_builder('mandelbrot',1000,2)

#fractal_builder('mandelbrot',100,3)
#fractal_builder('mandelbrot',100,4)
#fractal_builder('mandelbrot',100,5)

#fractal_builder('julia',10,2,-0.111,0.151)
fractal_builder('julia',100,2,-0.111,0.151)
#fractal_builder('julia',250,2,-0.111,0.151)
#fractal_builder('julia',500,2,-0.111,0.151)
#fractal_builder('julia',1000,2,-0.111,0.151)

#fractal_builder('julia',10,3,-0.111,0.151)
#fractal_builder('julia',100,3,-0.111,0.151)
#fractal_builder('julia',10,4,-0.111,0.151)
#fractal_builder('julia',100,4,-0.111,0.151)
#fractal_builder('julia',10,5,-0.111,0.151)
#fractal_builder('julia',100,5,-0.111,0.151)

#fractal_builder('julia',100,2,0,1)     #dendrite fractal
#fractal_builder('julia',100,3,0,1)
#fractal_builder('julia',100,4,0,1)
#fractal_builder('julia',100,5,0,1)

#fractal_builder('julia',100,2,1,0)
#fractal_builder('julia',100,3,1,0)
#fractal_builder('julia',100,4,1,0)
#fractal_builder('julia',100,5,1,0)

fractal_builder('julia',100,2,-0.123,0.745)     #Douady's rabbit fractal
#fractal_builder('julia',100,2,-0.75)       #San Marco fractal
fractal_builder('julia',100,2,-0.391,-0.587)    #Siegel disk fractal

# fractal_builder('mandelbrot',100,1)
