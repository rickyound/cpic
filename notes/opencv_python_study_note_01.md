
## OpenCV����

### ��ȡͼƬ

��һ���Ƕ�ȡͼƬ��OpenCV����ͨ��`cv2.inread()`��������ȡ���ҵڶ�����������ָ��3�ֶ�ȡ��ʽ��

```python
import cv2

# cv2.IMREAD_COLOR���Բ�ɫͼƬ��ʽ���أ�����͸������Ϣ����ΪĬ�ϵķ�ʽ
img = cv2.imread('../sources/IMG_20171011_173400.jpg', cv2.IMREAD_COLOR)
# or
img = cv2.imread('../sources/IMG_20171011_173400.jpg', 1)

# cv2.IMREAD_GRAYSCALE���ԻҶ�ģʽ����ͼƬ�������ɫ�ʺ�͸������Ϣ
img = cv2.imread('../sources/IMG_20171011_173400.jpg', cv2.IMREAD_GRAYSCALE)
# or
img = cv2.imread('../sources/IMG_20171011_173400.jpg', 0)

# cv2.IMREAD_UNCHANGED������alphaͨ����Ϣ�ļ���ͼƬ(��͸������Ϣ)
img = cv2.imread('../sources/IMG_20171011_173400.jpg', cv2.IMREAD_UNCHANGED)
# or
img = cv2.imread('../sources/IMG_20171011_173400.jpg', -1)
```

Ps.
�и�����Ҫ˵һ�£����������������ͼƬ�����ڣ���������������ˣ����������κη�Ӧ�����ᱨ��ֱ�ӷ���һ��None��

### չʾͼƬ

��ʾͼ������ʹ��`cv2.imshow()`�������÷�����ʹ�ñ��ش���չʾһ��ͼƬ�����Զ���Ӧ��ͼƬ�Ĵ�С��

����������������һ���Ǵ������ƣ��ڶ�������������Ҫչʾ��ͼƬ����

*���ǿ��Դ������չʾ���ڣ����ǲ�������*

```python
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

��ע��  
����ʾ���е�`cv2.waitKey(0)`��һ����������󶨺������������Ǻ������о���  
`cv2.destroyAllWindows()`�ǽ����п����Ĵ��ھ����٣������Ҫ�ر�ָ���Ĵ��ڣ����Դ��봰�����ƵĲ�����

ͬ���ڵ���`cv2.imshow()`֮ǰ�����Զ���һ�����壬������ָ�������Ƿ�ɵ�����С��ʹ�õ���`cv2.namedWindow()`��������Ҳ����������������һ���Ǵ������ƣ��ڶ����Ǳ�־��`cv2.WINDOW_AUTOSIZE`��Ĭ�ϵģ�����ʾ������ӦͼƬ���Ҵ��ڴ�С�����Զ���������������Ҫ���Ե����Ĵ��ڣ���ô����ָ��`cv2.WINDOW_NORMAL`��־��

*���������˴��壬��ôչʾ��ͼƬҲ���������*

```python
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

��ע��  
����ʾ���е�`cv2.namedWindow()`��`cv2.imshow()`�еĴ���������Ҫ����һ�£������һ������ô���൱�ڴ������������ڣ����ҵ�һ����һ���յĴ��壬�ڶ�����Ĭ�ϵĴ��塣

����а�װMatplotlib����ôҲ����ʹ������չʾͼ�����������ʾ��������������̽��

```python
from matplotlib import pyplot as plt

plt.inshow(img, camp='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y aixs
plt.show()
```

### д��ͼƬ

д��ͼƬ��������ͼƬ������ʹ��`cv2.imwrite()`���ɣ��÷�����һ���������ļ����ƣ��ڶ�����������Ҫ�洢��ͼƬ������

```python
cv2.imwrite('messigray.png', img)
```

*��������Ὣ`img`��PNG��ʽ�洢�ڵ�ǰĿ¼�����ļ�����Ϊ`messigray.png`��*

### ������չʾ��дͼƬ������

����ʾ����һ���ٷ��ĵ��е�ʾ����������ȡһ��ͼƬ��չʾ�����ҵ��㰴`s`��ʱ���ᱣ��ͼƬ������`Esc`ʱ�����ᱣ��ֱ���˳�

```python
import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
```

### ��ͼ��Ļ�������

OpenCV���и��࣬������������׽ͼ�񡢲�����Ƶ����ͼ����ˢ����ɫ��ȵȡ�  
�����뱾��Ŀ��ʱû��ʲô�����������Ȳ�̽����������ϵͳ�о���

����������������β���ͼ����Ҫ�����¼��㣺

- ���ʺ��޸����ص�ֵ
- ����ͼƬ������
- ����ͼ�������
- ��ֺͺϲ�ͼƬ

*���½ڼ������ǻ���Numpy��������OpenCV�������˽�Numpy�ܸ��õ�ʹ��OpenCVд�����롣*

#### ���ʺ��޸����ص�ֵ

�����ȼ��ز�ɫ��ͼƬ(��Ĭ�ϵı�־�Ϳ�����)

```python
>>> import cv2
>>> import numpy
>>> img = cv2.imread('../sources/IMG_20171011_173400.jpg')
```

���ǿ���ͨ�����е����꣬����������ֵ

```python
>>> px = img[100, 100]
```

����BGRͼ����˵�����᷵��һ����ɫ����ɫ����ɫ��ֵ�����飬��

```python
>>> print px
[178 162 150]
```

�����ڻҶ�ͼ����˵�������ص�����Ӧ��ǿ��ֵ

```python
>>> print px
160
```

���ԣ��������Ǿ����Ƴ����ǲ��ǿ����������޸�����ֵ�أ�

���ǵ�Ȼ���ԣ���

```python
>>> img[100, 100] = [255, 255, 255]
>>> print img[100, 100]
[255 255 255]
```

*�������ǲ������򵥵ķ���ÿ������Ȼ������޸ģ���Ӧ���ÿ������м�����Ż���Numpy������*

���õ�һ�����ط���/�޸ķ�����ʹ��`item`������

```python
# ��������10,10���صĺ�ɫֵ
>>> img.item(10, 10, 2)
147

# �޸ĸ����ص��ɫ��ֵΪ90
>>> img.itemset((10, 10, 2), 90)
>>> img.item(10, 10, 2)
90
```

#### ����ͼƬ������

ͼ������԰�����������������ͨ��ֵ��ͼ���������͡��������ȵȡ�

����ͼ�����״���ݣ�����ͨ��`shape`���ԣ�

����ǲ�ɫͼ����ô������һ�������С������С�ͨ����Ԫ�飻

����ǻҶ�ͼ����ô������һ�������С������е�Ԫ�顣

```python
>>> img.shape
(2976, 3968, 3)
>>> imggray.shape
(2976, 3968)
```

*Ps. ���ûҶ�ͼ��ֻ�������������������ԣ��������ø��������жϼ��ص��ǲ�ɫͼ���ǻҶ�ͼ��*

�ܹ�������������ͨ��`size`���Է���

```python
>>> img.size
35426304
>>> imggray.size
11808768
```

*Ps. 2976*3968=11808768����Ϊʲô��ɫ��ͼ�����ʾ��ô���أ���Ϊ3ͨ����...��11808768*3=35426304��*

ͼ����������Ϳ���ͨ��`dtype`���Է���

```python
>>> img.dtype
dtype('uint8')
>>> imggray.dtype
dtype('uint8')
```

*Ps. `uint8`����8λ�޷���int���������Ա�ʾ��ֵ��ΧΪ0~255�������ǳ�����RGBֵ�ķ�Χ*

*������ο���*

*https://docs.scipy.org/doc/numpy/user/basics.types.html*

*http://www.cnblogs.com/denny402/p/5122328.html*


**`img.dtype`�ڵ���ʱ�ǳ���Ҫ����ΪOpenCV-Python�����еĴ�������������Ч������������ġ�**

#### ͼ�������

ROI��Region Of Image��

��ʱ�����Ǳ������ĳЩȷ�������ͼ�� ������ͼ���е��۾����������ȶ�ͼ��ִ��������⣬�ҵ�����֮���������������������۾������ַ��������׼ȷ�ԣ���Ϊ�۾�����������:D���ͱ��֣���Ϊ��������һ��С���򣩡�

ROI��Ȼ��ѭNumpy��������Ƭ�����£����ǽ�ͼƬ�е�һ����������1000�����ص���һ������

```python
>>> flag = img[646:1282, 2466:3046]
>>> img[646:1282, 1466:2046] = flag
```

*Ps. Numpy������Ƭ��������ô��⣺`646:1282`��ʾ��646�е�1282�У�`2466:3046`��ʾ��2466�е�3046�С�*

#### ���/�ϲ�ͼ���ͨ��

������Ҫ��ʱ��һ��ͼ��BGRͨ�����Բ�ֳɵ�����һ�棻��Ȼ����Щ������ͨ��Ҳ���Է��������һ��BGR��ͼ�������±�

```python
>>> b, g, r = cv2.split(img)
>>> img = cv2.merge((b, g, r))

# or
>>> b = img[:, :, 0]
```

���ڣ���������Ҫ����ͼ���еĺ�ɫ����ͨ��ȫ����Ϊ0�������Ȳ�֣�Ȼ������0���ٺϲ���
���ǿ���ֱ��ʹ��Numpy�������ø��죬��

```python
>>> img[:, :, 2] = 0
```

*Ps. ��ʱ���������ǣ�`cv2.split()`�����ĺܴ�ģ����Էǵ��򲻵��Ѳ�ʹ�ã�������ʹ��Numpy indexing��*

#### Ϊͼ�������߿���䣩

���������ҪΪͼ������һ���߿�������������֣����ǿ���ʹ��`cv2.copyMakeBorder()`������

�������и���ĸ������㡢������Ӧ�ã������յĲ������£�

- src: �����ͼ�����
- top, bottom, left, right: ��Ӧ�ߵ����ؿ��
- borderType: ����������Ҫ���ʲô���͵ıߵı�־������ֵ����
     - cv2.BORDER_CONSTANT: һ���������ı߿���ֵӦ������һ����������
     - cv2.BORDER_REFLECT: �᾵��ӳ���Ԫ�صı߿�������: fedcba|abcdefgh|hgjedcb
     - cv2.BORDER_REPLICATE: ��ʼ���յĸ������һ����Ԫ�أ�������: aaaaaa|abcdefgh|hhhhhh
     - cv2.BORDER_WRAP: ���Ͳ����ˣ���������: cdefgh|abcdefgh|abcdefg
- value: ���borderType��`cv2.BORDER_CONSTANT`����ô����������������ɫֵ

�������ùٷ��ĵ��е�һ����ʾʾ����˵���������͵ı��֣���Ϊ�ǲ���Matplotlib��չʾ�ģ�ͼ�еĺ�ɫRED����ɫBLUE�������

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
```

![border](./pics/Image_01_01.jpg)

### ͼ����������

#### ͼ�����

���ǿ���ͨ��OpenCV��`cv2.add()`����������ʹ��Numpyֱ�Ӳ���`res = img1 + img2`���ⶼҪ������ͼ����ͬ�Ĵ�С����Ⱥ�ͨ����

��Ȼ���ַ���������ӣ������������в�ͬ�ģ�OpenCV�ķ�ʽ�������ӣ���Numpy�������ȡ�࣬������ʾ��

```python
>>> x = np.uint8([250])
>>> y = np.uint8([10])

>>> print cv2.add(x, y)  # 250 + 10 = 260 => 255
[[255]]

>>> print x+y            # 250 + 10 = 260 % 256 => 4
[4]
```

ֱ��ͨ��������ͬ��С��ͨ����ͼƬ��ʾ���������ԣ��������Ž�ͼ��������Ӻ�image1������ʾ��OpenCV����ӣ�image2������ʾ��Numpy����ӣ�

![add01](./pics/Image_01_02.png)

![add02](./pics/Image_01_03.png)

*�ɴ˿��Կ�����OpenCV������ṩ�˸��Ӻ�һЩ�Ľ�������Լ��ʹ��OpenCV�ܸ��á�*

#### ͼ����ں�

����ʵҲ��һ��ͼ����ӣ�ֻ������ÿ��ͼ���䲻ͬ�ı��أ���ô����ȥ�����ںϻ���͸���ˣ�ͼ��ᰴ�����·�����ӣ�

![formula01](./pics/Image_01_06.png)

���е� ![formula02](./pics/Image_01_07.png) ȡֵ��0 --> 1������������ͼƬ֮����һ���ܿ�Ĺ��ɡ�

OpenCV�е�`cv2.addWeighted()`�ṩ�����·�����ӣ�

![formula03](./pics/Image_01_08.png)

����������һ�£���һ��Ч����������ͼƬΪ���������һ����ͼƬ����һ��ռ��0.7���ڶ���ռ��0.3�� ![formula04](./pics/Image_01_09.png) ��ֵ0��

```python
>>> img1 = cv2.imread('../sources/opencv-logo.jpg', 1)
>>> img2 = cv2.imread('../sources/ewm.jpg', 1)

>>> dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
```

�������

![result](./pics/Image_01_04.png)

#### ��λ����

��λ����������(And)����(Or)����(Not)�����(XOR)��

����ʹ������ʾ������ʾ����OpenCV��logo��ȡ�������ǵ���һ��ͼ�ϣ�͸������Ϣ�ȱ��ֲ��䣺

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# ��������ͼƬ
img01 = cv2.imread('../sources/castle.jpg', 1)
#img02 = cv2.imread('../sources/opencv-logo.jpg', 1)
# ��ͼ�ñ���Ϊ͸������������һЩ������Ҫ��opencv-logo-white.pngͼƬ���Լ���ͼ������ɫ����
img02 = cv2.imread('../sources/opencv-logo-white.png', 1)

# ��Ϊ��Ҫ��logo�������Ͻǣ����Ը���img02�ĳߴ紴��һ��ROI
rows, cols, channels = img02.shape
roi = img01[0:rows, 0:cols]

# ���ڴ���һ��logo���ɰ�����ķ�ת�ɰ�
img02gray = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img02gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Ȼ��logo�е�ROI�����ڹ�
img01_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# ����logo��ȡ��logo����
img02_bg = cv2.bitwise_and(img02, img02, mask=mask)

# ��logo����ROI�У������޸���ͼ����Ӧ����
dst = cv2.add(img01_bg, img02_bg)
img01[0:rows, 0:cols] = dst

# չʾ��Ч��
cv2.imshow('img01_bg', img01_bg)
cv2.imshow('img02_bg', img02_bg)
cv2.imshow('image', img01)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

�����Ƿֱ�չʾ��`img01_bg`��`img02_bg`�����յ�`img01`���ͼ��

![contrast](./pics/Image_01_05.png)

### �����Ż�

������������Ҫ�������������ˡ�

*Ps. ����������ʱ�Ȳ����ǣ�ʵ����˵��*

