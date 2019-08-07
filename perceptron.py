import numpy as np
import matplotlib.pyplot as plt

#Numpy:
    #nparray.shape:  indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m).
    #.reshap(dimensional, row, column): creating type of the matrix we want(except 1D matrix). For example, .reshape(3,5) will create a matrix with 3 row and 5 columns.
    #np.zeros: creating an array full of zeros, the function ones creates an array full of ones
    #np.exp: hàn mũ

def draw(x1, x2): #nối 2 điểm x1, x2 để tạo thành 1 đường thẳng phân biệt 2 phần cần tác biệt
    ln = plt.plot(x1,x2)
    plt.pause(0.001) # dừng lại 0,0001s trước khí xóa đừng thẳng đó.
    ln[0].remove() # 0 là đối số bắt buộc của .remove() 

def error_function(score): #đây là hàm logistic chỉ ra xác suất dự đoán dự trên hàm tuyến tính (w1*x1 + w2*y +b) thứ chỉ cho ra kết qua CÓ hoặc Không
    return 1/(1 + np.exp(-score))

def calculate_error(line_parameters, all_points, y): # y = label (1 or 0)
    m = all_points.shape[0]
    p = error_function(all_points * line_parameters) # p = probability   
    cross_entropy = -(1/m)*(np.log(p).T * y + np.log(1-p).T * (1 - y)) # -(1/m)sigma{y*ln(P) + (1-y)*ln(1-P)}
    return cross_entropy    


def gradient_descent(line_parameters, all_points, y, alpha):#using gradient descent to minimize the error
    n = all_points.shape[0] #số phần tử thứ 0 trong mảng có tên  all_points
    for _ in range(500):
        p = error_function(all_points * line_parameters)
        gradient = all_points.T * (p - y) * (alpha / n) # alpha slows the finding down, just down make it so fast
        line_parameters = line_parameters - gradient

        w1 = line_parameters.item(0)
        w2 = line_parameters.item(1)
        b = line_parameters.item(2)

        x1 = np.array([all_points[:, 0].min(),all_points[:, 0].max() ]) #tọa độ trục hoành từ điểm nhỏ nhất đến lớn nhất
        x2 = -b/w2 + (x1 * (-w1/w2)) #w1*x1 + w2*y +b = 0
        draw(x1,x2)
    
n_points = 100 #số điểm trên đồ thị
np.random.seed(0) # tránh tình trạng việc chọn ngẫu nhiên bị trùng giữa hai phần TOP & BOTTOM
bias = np.ones(n_points) 
#chọn ngẫu nhiên các điểm chia thành 2 phần khác nhau, gọi là TOP và BOTTOM
top_region = np.array([np.random.normal(10, 2, n_points), np.random.normal(12, 2, n_points), bias]).T
bottom_region = np.array([np.random.normal(5, 2, n_points), np.random.normal(6, 2, n_points), bias]).T
all_points = np.vstack((top_region, bottom_region))#.vstack: chồng 2 mảng khác nhau để tạo thày một mảng mới
line_parameters = np.matrix([np.zeros(3)]).T # Weights but finding Weight is job of Computer, declare a matrix of zeros
y = np.array([np.zeros(n_points), np.ones(n_points)]).reshape(n_points * 2, 1) # label(x) = 1/0


_, ax = plt.subplots(figsize = (4,4))#subplots: which simply allows you to display multiple plots on the same figure
ax.scatter(top_region[:, 0], top_region[:, 1], color = 'r') #.scatter: is a library of matplotlib which plot of y vs x with varying marker size and/or color. 
ax.scatter(bottom_region[:, 0], bottom_region[:, 1], color = 'b')#[:, 0]: take ever value in column nu 0 
ax.scatter(4, 5, color = 'g', marker = 5)
calculate_error(line_parameters,all_points,y)
gradient_descent(line_parameters, all_points, y, 0.06)
plt.show()
