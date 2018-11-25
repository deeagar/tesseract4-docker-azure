FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install sudo -y
RUN sudo apt install tesseract-ocr -y
RUN sudo apt install libtesseract-dev -y
RUN sudo apt install python3-pip -y
RUN sudo pip3 install pytesseract
RUN sudo pip3 install opencv-python
RUN sudo apt install libsm6 -y
RUN sudo pip3 install azure.storage.blob

COPY . .
ENTRYPOINT ["/usr/bin/python3"]
CMD ["main.py"]