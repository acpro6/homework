import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import math

float_formatter = lambda x: "%.3f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})

# �������ݼ�
data = np.loadtxt("magic04.txt",
                  delimiter=",", usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
print("Row Data��ԭʼ���ݼ���:\n", data)

col_num = np.size(data, axis=1)  # ��ȡ����������
row_num = np.size(data, axis=0)  # ��ȡ��������

mean_vector = np.mean(data, axis=0).reshape(col_num, 1)  # ����Mean Vector
print("Mean Vector����ֵ������:\n", mean_vector)

t_mean_vector = np.transpose(mean_vector)  # ת��Mean Vector
centered_data_matrix = data - (1 * t_mean_vector)  # ����Centered Data Matrix
print("Centered Data Matrix���������ݾ���:\n", centered_data_matrix, "\n")

t_centered_data_matrix = np.transpose(centered_data_matrix)  # ת��Centered Data Matrix
covariance_matrix_inner = (1 / row_num) * np.dot(t_centered_data_matrix, centered_data_matrix)
# ��������Э�������
print("���������ݾ�����Ϊ�ڳ˻�������Э�������\n",
      covariance_matrix_inner, "\n")


# �����������ݵ�ĺ�
def sum_of_centered_points():
    sum = np.zeros(shape=(col_num, col_num))
    for i in range(0, row_num):
        sum += np.dot(np.reshape(t_centered_data_matrix[:, i], (-1, 1)),
                      np.reshape(centered_data_matrix[i, :], (-1, col_num)))
    return sum


covariance_matrix_outer = (1 / row_num) * sum_of_centered_points()
print("����Э���������Ϊ�������ݵ�֮��������\n",
      covariance_matrix_outer, "\n")

vector1 = np.array(centered_data_matrix[:, 1])
vector2 = np.array(centered_data_matrix[:, 2])


# �������������ĵ�λ����
def unit_vector(vector):
    return vector / np.linalg.norm(vector)


# ������������֮��ļн�
def angle_between(v1, v2):
    u_v1 = unit_vector(v1)
    u_v2 = unit_vector(v2)
    return np.arccos(np.clip(np.dot(u_v1, u_v2), -1.0, 1.0))


correlation = math.cos(angle_between(vector1, vector2))  # ��������Լ�������
print("����1��2֮�������ԣ� %.5f" % correlation, "\n")

variance_vector = np.var(data, axis=0)  # ����һ����������
max_var = np.max(variance_vector)  # ������󷽲�
min_var = np.min(variance_vector)  # ������С����

for i in range(0, col_num):  # �ҳ���󷽲�����������
    if variance_vector[i] == max_var:
        max_var_index = i

for i in range(0, col_num):  # �ҳ���С��������������
    if variance_vector[i] == min_var:
        min_var_index = i

print("Max variance = %.3f (Attribute %d )" % (max_var, max_var_index))
print("Min variance = %.3f (Attribute %d )\n" % (min_var, min_var_index))

covariance_matrix = np.cov(data, rowvar=False)  # ����Э�������
max_cov = np.max(covariance_matrix)  # �ҳ�Э��������е����ֵ
min_cov = np.min(covariance_matrix)  # �ҳ�Э��������е���Сֵ

# ����forѭ���ҳ������Сֵ������
for i in range(0, col_num):
    for j in range(0, col_num):
        if covariance_matrix[i, j] == max_cov:
            max_cov_attr1 = i
            max_cov_attr2 = j

for i in range(0, col_num):
    for j in range(0, col_num):
        if covariance_matrix[i, j] == min_cov:
            min_cov_attr1 = i
            min_cov_attr2 = j

print("Max Covariance = %.3f (Between Attribute %d and %d)" % (max_cov, max_cov_attr1, max_cov_attr2))
print("Min Covariance = %.3f (Between Attribute %d and %d)" % (min_cov, min_cov_attr1, min_cov_attr2))


