import os
import csv
import platform
import time
import cv2


def get_tianchi_train_dataset():
    t0 = time.time()
    print("loading annotations")
    dataset = []
    machine_name = platform.node()
    print(machine_name)
    if machine_name == "P100v0":
        dataset_dir = "/home/sk49/workspace/dataset/tianchi_clothes/train"
        ann_path = os.path.join(dataset_dir, "Annotations", "traindiv.csv")
    elif machine_name == "Lenovo-PC":
        dataset_dir = r"./data/train_1"
        ann_path = "./preprocessing/train_2.csv"
    else:
        dataset_dir = "/home/sk49/workspace/dataset/tianchi_clothes/train"
        ann_path = os.path.join(dataset_dir, "Annotations", "train.csv")

    with open(ann_path, "r") as f:
        r = csv.reader(f)
        first_line = next(r)
        # print(first_line)
        # aid(int), joints(list), imgpath(str), headRect(numpy.ndarray), bbox(list),
        # imgid(int), segmentation(list)
        for line in r:
            if len(line) == 0:
                continue
            img_dict = {}
            img_name = line[0].strip().split("/")
            img_cat = line[1]
            joints = []
            for l in line[2:-5]:
                l_temp = list(map(int, l.split("_")))
                joints.extend(l_temp)
            # print(joints)
            bbox=line[-5:-1]


            img_path = os.path.join(dataset_dir, img_name[0], img_name[1], img_name[2])
            print(img_path)
            img = cv2.imread(img_path)
            h, w, c = img.shape
            for i in range(0,3):
                img_dict={}
                img_dict["imgpath"] = img_path
                img_dict["joints"] = joints
                img_dict["bbox"] = [0,0,w,h]
                img_dict["score"] = 1
                img_dict["operation"]=int(i)
                dataset.append(img_dict)
    print("load ends, total", time.time() - t0, "s")

    return dataset

def get_tianchi_val_dataset():
    t0 = time.time()
    print("loading annotations")
    dataset = []
    machine_name = platform.node()
    print(machine_name)
    if machine_name == "P100v0":
        dataset_dir = "/home/sk49/workspace/dataset/tianchi_clothes/train"
        ann_path = os.path.join(dataset_dir, "Annotations", "valdiv.csv")
    elif machine_name == "Lenovo-PC":
        dataset_dir = r"./data/train_1"
        ann_path = "./preprocessing/train_2.csv"
    else:
        dataset_dir = "/home/sk49/workspace/dataset/tianchi_clothes/train"
        ann_path = os.path.join(dataset_dir, "Annotations", "train.csv")


    with open(ann_path, "r") as f:
        r = csv.reader(f)
        first_line = next(r)
        # print(first_line)
        # aid(int), joints(list), imgpath(str), headRect(numpy.ndarray), bbox(list),
        # imgid(int), segmentation(list)
        for line in r:
            if len(line) == 0:
                continue
            img_dict = {}
            img_name = line[0].strip().split("/")
            img_cat = line[1]
            joints = []
            for l in line[2:-5]:
                l_temp = list(map(int, l.split("_")))
                joints.extend(l_temp)
            # print(joints)
            bbox=line[-5:-1]


            img_path = os.path.join(dataset_dir, img_name[0], img_name[1], img_name[2])
            print(img_path)
            img = cv2.imread(img_path)
            h, w, c = img.shape
            img_dict["imgpath"] = img_path
            img_dict["joints"] = joints
            img_dict["bbox"] = [0,0,w,h]
            img_dict["score"] = 1
            dataset.append(img_dict)
    print("load ends, total", time.time() - t0, "s")

    return dataset

def get_tianchi_test_dataset():
    t0 = time.time()
    print("loading annotations")
    dataset = []
    machine_name = platform.node()
    print(machine_name)
    if machine_name == "P100v0":
        dataset_dir = "/home/sk49/workspace/dataset/tianchi_clothes/fashionAI_key_points_test_a_20180227/test"
        ann_path = "/home/sk49/workspace/dataset/tianchi_clothes/fashionAI_key_points_test_a_20180227/merge1.csv"
    elif machine_name == "Lenovo-PC":
        dataset_dir = r"./data/train_1"
        ann_path = "./test1.csv"
    else:
        dataset_dir = "/home/sk49/workspace/dataset/tianchi_clothes/train"
    # ann_path = os.path.join(dataset_dir, "Annotations", "train.csv")
    #
        ann_path = "/home/sk49/workspace/dataset/tianchi_clothes/fashionAI_key_points_test_a_20180227/test.csv"
    with open(ann_path, "r") as f:
        r = csv.reader(f)
        first_line = next(r)
        # print(first_line)
        # aid(int), joints(list), imgpath(str), headRect(numpy.ndarray), bbox(list),
        # imgid(int), segmentation(list)
        for line in r:
            if len(line) == 0:
                continue
            img_dict = {}
            img_name = line[0].strip().split("/")
            img_cat = line[1]
            # joints = []
            # for l in line[2:]:
            #     l_temp = list(map(int, l.split("_")))
            #     joints.extend(l_temp)
            # print(joints)

            img_path = os.path.join(dataset_dir, img_name[0], img_name[1], img_name[2])
            print(img_path)
            img = cv2.imread(img_path)
            h, w, c = img.shape
            img_dict["imgid"] = img_name = line[0]
            img_dict["imgpath"] = img_path
            #img_dict["joints"] = joints
            img_dict["category"] = img_cat
            img_dict["bbox"] = [0,0,w,h]
            img_dict["score"]= 1
            dataset.append(img_dict)
    print("load ends, total", time.time() - t0, "s")

    return dataset

if __name__ == '__main__':
    get_tianchi_train_dataset()