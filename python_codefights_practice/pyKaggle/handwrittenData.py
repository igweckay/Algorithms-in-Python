import pandas as pd 
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm
#%matplotlib inline

labeled_images = pd.read_csv('/Users/kigwe/Desktop/pyKaggle/train.csv')
images = labeled_images.iloc[0:5000,1:]
labels = labeled_images.iloc[0:5000,:1]
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, train_size=.8, random_state=0) #always make the assignment random

#View images
for image_id in range(2,3):
	img = train_images.iloc[image_id].as_matrix() #as_matrix converts to a numpy_array datastructure not numpy_matrix
	img = img.reshape((28,28)) #make array into a 28by28
	plt.imshow(img,cmap='gray')#make it gray scaled
	plt.title(train_labels.iloc[1,0])
	#plt.show()
	plt.hist(train_images.iloc[image_id]) #histogram to show range of values for each number
	#plt.show()
clf = svm.SVC()
clf.fit(train_images, train_labels.values.ravel())
print (clf.score(test_images, test_labels))
