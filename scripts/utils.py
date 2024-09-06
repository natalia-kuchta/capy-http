import re
import glob
import os
from uu import Error

codes = [
    (100, 'Continue'),
    (101, 'Switching Protocols'),
    (102, 'Processing'),
    (103, 'Early Hints'),
    (200, 'OK'),
    (201, 'Created'),
    (202, 'Accepted'),
    (203, 'Non-authoritative Information'),
    (204, 'No Content'),
    (205, 'Reset Content'),
    (206, 'Partial Content'),
    (207, 'Multi-Status'),
    (208, 'Already Reported'),
    (214, 'Transformation Applied'),
    (226, 'IM Used'),
    (300, 'Multiple Choices'),
    (301, 'Moved Permanently'),
    (302, 'Found'),
    (303, 'See Other'),
    (304, 'Not Modified'),
    (305, 'Use Proxy'),
    (307, 'Temporary Redirect'),
    (308, 'Permanent Redirect'),
    (400, 'Bad Request'),
    (401, 'Unauthorized'),
    (402, 'Payment Required'),
    (403, 'Forbidden'),
    (404, 'Not Found'),
    (405, 'Method Not Allowed'),
    (406, 'Not Acceptable'),
    (407, 'Proxy Authentication Required'),
    (408, 'Request Timeout'),
    (409, 'Conflict'),
    (410, 'Gone'),
    (411, 'Length Required'),
    (412, 'Precondition Failed'),
    (413, 'Payload Too Large'),
    (414, 'Request-URI Too Long'),
    (415, 'Unsupported Media Type'),
    (416, 'Requested Range Not Satisfiable'),
    (417, 'Expectation Failed'),
    (418, 'I\'m a teapot'),
    (420, 'Enhance Your Calm'),
    (421, 'Misdirected Request'),
    (422, 'Unprocessable Entity'),
    (423, 'Locked'),
    (424, 'Failed Dependency'),
    (425, 'Too Early'),
    (426, 'Upgrade Required'),
    (428, 'Precondition Required'),
    (429, 'Too Many Requests'),
    (431, 'Request Header Fields Too Large'),
    (444, 'No Response'),
    (450, 'Blocked By Windows Parental Controls'),
    (451, 'Unavailable For Legal Reasons'),
    (497, 'HTTP Request Sent To HTTPS Port'),
    (498, 'Token Expired/Invalid'),
    (499, 'Client Closed Request'),
    (500, 'Internal Server Error'),
    (501, 'Not Implemented'),
    (502, 'Bad Gateway'),
    (503, 'Service Unavailable'),
    (504, 'Gateway Timeout'),
    (505, 'HTTP Version Not Supported'),
    (506, 'Variant Also Negotiates'),
    (507, 'Insufficient Storage'),
    (508, 'Loop Detected'),
    (509, 'Bandwidth Limit Exceeded'),
    (510, 'Not Extended'),
    (511, 'Network Authentication Required'),
    (521, 'Web Server Is Down'),
    (522, 'Connection Timed Out'),
    (523, 'Origin Is Unreachable'),
    (525, 'SSL Handshake Failed'),
    (530, 'Site Frozen'),
    (599, 'Network Connect Timeout Error'),
]

base_target_dir = "../public/capy"
base_media_dir = "../src/assets/capy-media"
base_official_dir = "../src/assets/capy-official"
base_content_dir = "../src/content/posts"

files = [os.path.basename(file) for file in glob.glob(base_media_dir + "/*")]


def pattern_for_code(code):
    return re.compile(''.join(['^Capy', str(code[0]), '\.', '(jpg|jpeg|webp|webm|mp4|gif|avif|png)$']))

def pattern_for_code_img_only(code):
    return re.compile(''.join(['^Capy', str(code[0]), '\.', '(jpg|jpeg|webp|gif|avif|png)$']))

def pattern_for_code_video_only(code):
    return re.compile(''.join(['^Capy', str(code[0]), '\.', '(webm|mp4)$']))


def get_size(file, base=base_media_dir):
    return os.path.getsize(base + '/' + file)

import shutil

def publish(file):
    src = base_media_dir + '/' + file
    dst = base_official_dir + '/' + file
    if os.path.exists(dst):
        return
    shutil.copyfile(src, dst)

import cv2
import PIL
from PIL import Image

def get_resolution(file, ext, base=base_media_dir):
    if ext == '.mp4':
        vid = cv2.VideoCapture(base + '/' + file)
        hgt = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        wid = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        return wid, hgt

    img = PIL.Image.open(base + '/' + file)
    wid, hgt = img.size
    return wid, hgt

def list_file_and_extensions_for_codes():
    results = []

    for (code) in codes:
        pattern = pattern_for_code(code)
        match = 0
        file_name = ''
        for file in files:
            if pattern.match(file):
                match += 1
                file_name = file
        if match != 1:
            raise Exception(f"Wrong matches for {code[0]}")

        extension = os.path.splitext(file_name)[1]

        results.append((code[0], code[1], file_name, extension))

    return results