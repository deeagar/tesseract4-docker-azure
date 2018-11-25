import cv2
import pytesseract
import tempfile
import urllib.request
import os
from azure.storage.blob import BlockBlobService

# Path to tesseract
PATH_TO_TESSERACT = '/usr/bin/tesseract'
STORAGE_ACCNT_NAME = 'storageaccountname'
STORAGE_ACCNT_KEY = 'storageacountkey'

if __name__ == '__main__':
	try:
		f = tempfile.mkstemp(suffix=".png")
		urllib.request.urlretrieve(os.environ["blobUrl"], f[1])
		pytesseract.pytesseract.tesseract_cmd = PATH_TO_TESSERACT
		# Define config parameters.
		# '-l eng'  for using the English language
		# '--oem 1' sets the OCR Engine Mode to LSTM only.
		#
		#  There are four OCR Engine Mode (oem) available
		#  0    Legacy engine only.
		#  1    Neural nets LSTM engine only.
		#  2    Legacy + LSTM engines.
		#  3    Default, based on what is available.
		#
		#  '--psm 3' sets the Page Segmentation Mode (psm) to auto.
		#  Other important psm modes will be discussed in a future post.

		config = ('-l eng --oem 1 --psm 3')

		# Read image from disk
		im = cv2.imread(f[1], cv2.IMREAD_COLOR)
		# Run tesseract OCR on image
		text = pytesseract.image_to_string(im, config=config)
		blob_service = BlockBlobService(account_name=STORAGE_ACCNT_NAME,account_key=STORAGE_ACCNT_KEY)
		blob_service.create_blob_from_text(os.environ["outputContainerName"], os.environ["outputFileName"], text)
		os.remove(f[1])
		
	except Exception as ex:
		print("Exception: " + str(ex))


	
