import numpy as np
import scipy as sp

def main():
    a=np.array([[3 , 0 , -1 , 0 ],\
                [0 , 3 , -1 , 0 ],\
                [-1 , -1 , 3 , -1 ],\
                [0 , 0 , -1 , 3 ]])
    b=np.array([[150 , 70],
                [100 , 40],\
                [0 , 0],\
                [50 , 130]])
    A_inv=np.linalg.inv(a)
    x=np.dot(A_inv,b)
    print(A_inv)
    print(x)
        
if __name__ == "__main__": main()