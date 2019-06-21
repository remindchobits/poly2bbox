import numpy as np

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def bbox_gen(load_dict):
    img_w = load_dict['imageWidth']
    img_h = load_dict['imageHeight']
    obj = load_dict['shapes'][0]['points']
    obj = np.array(obj)
    obj = np.asarray(obj)
    x_cor = []
    y_cor = []
    for i in range(obj.shape[0]):
        x_cor.append(obj[i][0])
    for i in range(obj.shape[0]):
        y_cor.append(obj[i][1])
    x_min = np.min(x_cor)
    x_max = np.max(x_cor)
    y_min = np.min(y_cor)
    y_max = np.max(y_cor)
    b = (x_min,x_max,y_min,y_max)
    bb = convert((img_w,img_h),b)
    return bb
