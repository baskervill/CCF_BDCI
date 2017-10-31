#!/usr/bin/env python
# coding:utf-8

#from xml.etree.ElementTree import Element, SubElement, tostring
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString

classes_name = {"1":"huochuan", "2":"youlun", "3":"youting", "4":"yuting"}
input_file = open('./data/merge.txt')
for line in input_file.readlines():
    line = line.strip()
    ss = line.split(' ')
    #print ss[0][-10:]
    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'fangyi'
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = ss[0][-10:-4]
    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = '1024'

    node_height = SubElement(node_size, 'height')
    node_height.text = '1024'
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'
    i = 0
    while i + 1 < len(ss):
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = classes_name[ss[5]]
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = ss[1 + i]
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = ss[2 + i]
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = ss[3 + i]
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = ss[4 + i]
        i = i + 5
    output_file = open(ss[0][-10:-4]+'.xml','w')
    xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
    dom = parseString(xml)
    print xml
    output_file.write(xml)
    output_file.close()
    dom.unlink()
