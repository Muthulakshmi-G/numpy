import numpy as np
import skimage.data  #image read panrom

img=skimage.data.chelsea()

img=skimage.color.rgb2gray(img)  #rgb imagea gray imagea mathurom

#preparing filters
l1_filter=np.zeros((2,3,3)) #2 filters,3 rows,3columns

l1_filter[0,:,:]=np.array([[[-1.0.1],[-1,0,1],[-1,0,1]]])

l1_filter[1,:,:]=np.array([[[1,1,1],[0,0,0],[-1,-1,-1]]])

l1_feature_map=conv(img,l1_filter)


def conv(img,conv_filter):
    if len(img.shape)>2 or len(conv_filter.shape)>3:
        if img.shape[-1]!=conv_filter.shape[-1]:
            print("error:number of channels in both image")
            sys.exit()
    if conv_filter.shape[1]!=conv_filter.shape[2]:
        print("error:filter must be a square matrix.number of rows and columns must match")
            sys.exit()
    
    if conv_filter.shape[1]%2==0:
        print("error:filter must have an odd size.number of rows and columns must be odd") 
        sys.exit()


feature_maps=np.zeros((img.shape[0]-conv_filter.shape[1]+1,img.shape[1]-conv_filter.shape[1]+1,conv_filter.shape[0]))






