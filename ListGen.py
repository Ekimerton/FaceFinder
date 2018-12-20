import cognitive_face as CF
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO
import requests

CF.face_list.create(LIST_NUMBER)

LIST_NUMBER = 10

with open("BigList.txt") as f:
    content = f.readlines()
    for line in content:
        try:
            line = line[:(len(line) - 1)]
            CF.face_list.add_face(line, LIST_NUMBER, line + "", None)
        except:
            x = 1
