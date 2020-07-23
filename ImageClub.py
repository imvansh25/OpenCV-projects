import cv2


def hconcat_resize_min(im_list,name, interpolation=cv2.INTER_CUBIC):
    img_list=[]
    for img in im_list:
        img_list.append(cv2.imread(img))

    h_min = min(im.shape[0] for im in img_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in img_list]


    im_h_resize = cv2.hconcat(im_list_resize)
    cv2.imwrite(name, im_h_resize)
    return name


def vconcat_resize_min(im_list,name, interpolation=cv2.INTER_CUBIC):
    img_list = []
    for img in im_list:
        img_list.append(cv2.imread(img))

    w_min = min(im.shape[1] for im in img_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in img_list]
    
    im_v_resize = cv2.vconcat(im_list_resize)
    cv2.imwrite(name, im_v_resize)
    return name


