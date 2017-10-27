
## OpenCV����

���������Ҫѧϰ��OpenCV�е���ѧ���������ˣ��Ƚ���Ҫ�����Ե�����һƪ��

### ͼ����֮�ı�ɫ�ʿռ�

��OpenCV����150���ɫ�ʿռ�ת���ķ�������������ֻ����������Ӧ����㷺�ģ���BGR<-->GRAY��BGR<-->HSV��

����֮ǰҲ�ù������ķ�������

```python
>>> img = cv2.imread('../sources/img_small.jpg')
>>> imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

ɫ��ת������ʹ��`cv2.cvtColor(input_image, flag)`����������`flag`��ֵȡ������Ҫת�������͡�

����Ǵ�BGR-->GRAY����`flag`Ϊ`cv2.COLOR_BGR2GRAY`��  
ͬ������Ǵ�BGR-->HSV����Ϊ`cv2.COLOR_BGR2HSV`��
  
Ҫ��֪������������ʲô`flag`ȡֵ�����԰����²����鿴

```python
>>> import cv2
>>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')
>>> print flags
```

#### ����׽

�������ǿ��Դ�BGRת����HSVɫ�ʿռ䣬����ȡ��ɫ����

��Ϊ��HSV�У���ʾ��ɫ����BGRɫ�ʿռ��б�ʾ��ɫ�����ף����������������г�����ȡһ����ɫ�Ķ��󣨳Ǳ���

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����HSV����ȡ��ɫ����

import cv2
import numpy as np

img = cv2.imread('../../sources/castle.jpg', 1)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.uint8([0, 50, 50])
upper_yellow = np.uint8([34, 255, 255])

mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

������£�

![Image_02_01](./pics/Image_02_01.jpg)

*Ps. ��Ȼ�������򵥵Ŀٳ������Ǻ������ģ����кܶ�������Ǻ������������δ���*

**����HSVɫ�ʿռ�֪ʶ**

HSV(hue,saturation,value)��ɫ�ռ��ģ�Ͷ�Ӧ��Բ������ϵ�е�һ��Բ׶���Ӽ���Բ׶�Ķ����Ӧ��V=1. ������RGBģ���е�R=1��G=1��B=1 �����棬���������ɫ������

ɫ��H����V�����ת�Ǹ�������ɫ��Ӧ�� �Ƕ�0�� ����ɫ��Ӧ�ڽǶ�120�㣬��ɫ��Ӧ�ڽǶ�240�㡣��HSV��ɫģ���У�ÿһ����ɫ�����Ĳ�ɫ���180�� ��

���Ͷ�Sȡֵ��0��1������Բ׶����İ뾶Ϊ����

HSV��ɫģ�����������ɫ����CIEɫ��ͼ��һ���Ӽ������ ģ���б��Ͷ�Ϊ�ٷ�֮�ٵ���ɫ���䴿��һ��С�ڰٷ�֮�١�

��Բ׶�Ķ���(��ԭ��)����V=0,H��S�޶��壬 �����ɫ��Բ׶�Ķ������Ĵ�S=0��V=1,H�޶��壬�����ɫ���Ӹõ㵽ԭ��������Ƚ����Ļ�ɫ�������в�ͬ �ҶȵĻ�ɫ��������Щ�㣬S=0,H��ֵ�޶��塣����˵��HSVģ���е�V���Ӧ��RGB��ɫ�ռ��е����Խ��ߡ� ��Բ׶�����Բ���ϵ���ɫ��V=1��S=1,������ɫ�Ǵ�ɫ��HSVģ�Ͷ�Ӧ�ڻ�����ɫ�ķ����������øı�ɫŨ�� ɫ��ķ�����ĳ�ִ�ɫ��ò�ͬɫ������ɫ����һ�ִ�ɫ�м����ɫ�Ըı�ɫŨ�������ɫ�Ըı�ɫ�ͬʱ ���벻ͬ�����İ�ɫ����ɫ���ɻ�ø��ֲ�ͬ��ɫ����

![Image_02_02](./pics/Image_02_02.jpg)

![Image_02_03](./pics/Image_02_03.jpg)

**RGB-->HSV**ɫ��ģʽֵ��ת����ʽ���£�

```c
var_R = ( R / 255 ) //RGB from 0 to 255
var_G = ( G / 255 )
var_B = ( B / 255 )

var_Min = min( var_R, var_G, var_B ) //Min. value of RGB
var_Max = max( var_R, var_G, var_B ) //Max. value of RGB

del_Max = var_Max - var_Min //Delta RGB value

V = var_Max

if ( del_Max == 0 ) //This is a gray, no chroma...
{
    H = 0 //HSV results from 0 to 1
    S = 0
}
else //Chromatic data...
{
    S = del_Max / var_Max
   
    del_R = ( ( ( var_Max - var_R ) / 6 ) + ( del_Max / 2 ) ) / del_Max
    del_G = ( ( ( var_Max - var_G ) / 6 ) + ( del_Max / 2 ) ) / del_Max
    del_B = ( ( ( var_Max - var_B ) / 6 ) + ( del_Max / 2 ) ) / del_Max

    if ( var_R == var_Max ) H = del_B - del_G
    else if ( var_G == var_Max ) H = ( 1 / 3 ) + del_R - del_B
    else if ( var_B == var_Max ) H = ( 2 / 3 ) + del_G - del_R

    if ( H < 0 ) ; H += 1
    if ( H > 1 ) ; H -= 1
}
```

#### ����ҵ���Ҫ���ٵ�HSVֵ

���Ǵ�ɲ���ʹ������������㣬����ֻ���г����������˽�һ�¼��ɡ�

ʵ���ϣ�������Ȼ��`cv2.cvtColor()`���������ҳ���Ҫ��HSVֵ��ֻ�����Ǵ���Ĳ���ͼ�񣬶���һ��BGR��ֵ��

��������Ҫ����ɫ�ģ�Green�������԰���������ʾ

```python
>>> green = np.uint8([[[0, 255, 0]]])
>>> hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]
```

���У�`hsv_green`������ɫ��ֵ�ˣ����ǻ������԰�������`[H - 10, 100, 100]`������`[H + 10, 255, 255]`�����Ϊ��Χ�ˡ���Ȼ��Ҳ����ʹ��ͼ��༭���������ȡHSV��ֵ�����Ҫ�ǵ������һ���ķ�ΧŶ��

### ͼ����֮ͼ����ֵ��/��ֵ��

#### ����ֵ��

�ܼ򵥣����һ�����ص����һ����ֵ�����Ǹ�������һ��ֵ�������ǰ�ɫ�������򣬸���������һ��ֵ�������Ǻ�ɫ����

������Ҫ�õĵķ�����`cv2.threshold()`�������ĸ�����

1. ԭͼ��**����Ҫ�ǻҶ�GRAYͼ��**��
2. �����綨����ֵ����ֵ
3. �����ص�ֵ���ڣ���ʱ����С�ڣ���ֵʱ����ֵ
4. ��ֵ��������

���е��ĸ���������OpenCV�У��ṩ���¼�����ͬ�����ͣ��Լ����ǵĲ��ԣ�dst��Ŀ������

- `cv2.THRESH_BINARY`

![Image_02_04](./pics/Image_02_04.jpg)

- `cv2.THRESH_BINARY_INV`
    
![Image_02_05](./pics/Image_02_05.jpg)

- `cv2.THRESH_TRUNC`

![Image_02_06](./pics/Image_02_06.jpg)

- `cv2.THRESH_TOZERO`

![Image_02_07](./pics/Image_02_07.jpg)

- `cv2.THRESH_TOZERO_INV`

![Image_02_08](./pics/Image_02_08.jpg)


�÷����᷵���������󣬵�һ����`retval`���Ժ���˵���ڶ���`thresholded image`����������ֵ�����ͼ���ˡ�

����ʹ��һ����������ʾһ�¸������͵���ֵ�����������Թٷ��ĵ���

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ��ʾ�������͵ĵ���ֵ������

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_gray = cv2.imread('../../sources/gradient.jpg', 0)

ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img_gray, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

���н�����£����Ժ����Կ����������͵�����

![Image_02_09](./pics/Image_02_09.jpg)

#### ����Ӧ��ֵ��

����������ָ��һ����ֵ����������������С�ھ���������ô���ڹ��߲��õ���Ƭ��˵���ͻ�������������������

������ǰ���ֵ��С�ˣ�����һ����ͼ�����壬��������ˣ��ֻ�չʾ��ȫ�����v=50, �ұ�v=100����

![Image_02_10](./pics/Image_02_10.jpg)

����������Ҫ��������һ��С��������ļ�����ֵ����������ǵ�����Ӧ��ֵ��

���ܺܺõĴ���ͬ�����µ�ͼ��

��OpenCV�У���������`cv2.adaptiveThreshold()`�������յĲ�����`cv2.threshold()`����ָ������ֵû���⣬���������������⡱�Ĳ�����

- `Adaptive Method`����Ӧ��������������μ�����ֵ�����õ�ֵ����  
    1. `cv2.ADAPTIVE_THRESH_MEAN_C`����ֵ����Ϊ���������ƽ��ֵ  
    2. `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`����ֵ����Ϊ��������ĸ�˹��Ȩƽ��ֵ  

- `Block Size`����������������Ĵ�С  

- `C`������ֻ�����õ�һ��ƽ��ֵ���Ȩƽ��ֵ��ȥ��һ������  

���������ô�������ʾһ������Ӧ��ֵ���ͼ���ֵ���������Լ���ʹ����ֵ���в�ͬ����������

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ��������Ӧ��ֵ�������ı���

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_gray = cv2.imread('../../sources/sudoku.jpg', 0)
#img_gray = cv2.medianBlur(img_gray, 3)

# ����ֵ��
ret, thresh1 = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

# ����Ӧ��ֵ����ƽ��ֵ
thresh2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
# ����Ӧ��ֵ������˹��Ȩƽ��ֵ
thresh3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

titles = ['Original Image', 'Simple Thresholding(v=100)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img_gray, thresh1, thresh2, thresh3]

for i in xrange(4):
    plt.subplot(2,2,(i+1)), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
```

���н�����£����Կ���Ч�����Ժúࣺܶ

![Image_02_11](./pics/Image_02_11.jpg)

#### ����㷨��ֵ��

����һ����ţ�Ƶ��㷨����ʱ�Ȳ�����������о���

�ο���  
https://en.wikipedia.org/wiki/Otsu%27s_method  
https://baike.baidu.com/item/otsu/16252828  

### ͼ����֮���α任

#### ͼ������

��OpenCV�У�����ʹ��`cv2.resize()`����������ָ��ͼ���С����

���԰������·�������ͼ��Ŵ�����

```python
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# or

height, width = img.shape[:2]
res = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)
```

#### ͼ��ת��

ת����ת��ͼ���λ�ã� ������֪��Ҫת�Ƶ�`(x, y)`�������꣬��ô�Ϳ���ʹ������ת����������ʾ

![Image_02_12](./pics/Image_02_12.jpg)

�þ���ʹ��Numpy�е�`np.float32`����ʾ����ͨ��OpenCV��`cv2.wrapAffine()`����������ͼ��ת�ƣ���

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����ͼ��ת��

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/castle.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = img_gray.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img_gray, M, (cols, rows))

cv2.imshow('img_gray', img_gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

���н�����£�����`dst`ͼ�����Ͻǵ�����Ϊx=100, y=50��ͼ���С���ֲ��䡣

![Image_02_13](./pics/Image_02_13.jpg)

#### ͼ����ת

����ͨ������ת����������ͼ�������ĵ���ת ![Image_02_14](./pics/Image_02_14.jpg) �Ƕ�

![Image_02_15](./pics/Image_02_15.jpg) 

����OpenCV�ṩ�˿ɵ�����ת���ĵ�������ת���Ա����κ�����ϲ����λ�ý�����ת�����Ծ����Ϊ

![Image_02_16](./pics/Image_02_16.jpg) 

���У�![Image_02_17](./pics/Image_02_17.jpg) 

OpenCV�ṩ��һ������`cv2.getRotationMatrix2D`����ȡ�������

������ʾ������ͼ��Χ��������ת��30�ȣ�û�����κ����ţ�

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����ͼ����ת

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/castle.jpg', 0)
rows, cols = img.shape

# ������ת���ꡢ�Ƕȡ����ű���
M = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

�������

![Image_02_18](./pics/Image_02_18.jpg)

���ǿ��Խ�����ʾ���е�M��ӡ����������䳤ʲô����

```python
print M

[[   0.8660254     0.5         -37.02301144]
 [  -0.5           0.8660254   157.82824024]]
```

#### ����ת��

�ڴ����͵�ת���У�����ԭ��ƽ�е����������Ҳ����ƽ�еģ����ǿ��Կ����ǻ�һ���Ƕȿ����ͼ����ѡ�

Ϊ���ҵ����ת������������Ҫ�ṩ�����㣬�����ͼ��������Ӧ���ڵ���ȷλ�ã�Ȼ��ͨ��`cv2.getAffineTransform()`��������һ��2��3�еľ��󣬴��ݸ�`cv2.warpAffine()`��ת����

��������ʾ��������`pts1`����ԭͼ�ϵĵ㣬�������ͼ���е�`pts2`����

���ڴ����У�ʵ�����൱�ڸ���`[200,50]`�������ת�ˣ�

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����ͼ���Զ���任

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/drawing.jpg')

rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

print M

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
```

![Image_02_19](./pics/Image_02_19.jpg)

ͬ�����������M�鿴

```python
print M

[[  1.26666667   0.6        -83.33333333]
 [ -0.33333333   1.          66.66666667]]
```

#### ͸��ת��

͸��ת�����ǽ�͸����ͼ��ת��Ϊƽ�ӣ����Ƕ���ת��ǰ��ֱ����Ȼ��ֱ�ߣ����ܱ��Ρ�

������Ҫһ��3X3��ת������Ϊ���ҵ��������������Ҫԭͼ�ϵ�4���㣬������������3���㲻��ͬһ��ֱ���ϡ�

Ȼ�����ǾͿ���ͨ��`cv2.getPerspectiveTransform()`��������ȡ�þ���

ͨ��`cv2.warpPerspective()`������Ӧ�øþ����磺

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����ͼ��͸��ת��

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_ori = cv2.imread('../../sources/img_little.jpg')
#img = cv2.imread('../../sources/perspective.jpg')

# OpenCV��ͼ����BGR��Matplotlib�������RGB��������Ҫ����ת��
img = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)

rows, cols, ch = img.shape

pts1 = np.float32([[69, 30], [473, 30], [4, 354], [500, 354]])
pts2 = np.float32([[0, 0], [496, 0], [0, 324], [496, 324]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (496, 324))

plt.subplot(121), plt.imshow(img), plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Output'), plt.xticks([]), plt.yticks([])
plt.show()
```

���н�����£�

![Image_02_20](./pics/Image_02_20.jpg)

