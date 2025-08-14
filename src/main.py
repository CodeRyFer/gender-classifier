from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

# [[height(inches), weight(pounds), shoe size]]
x = [[72, 180, 11], [75, 200, 12], [56, 120, 8], [54, 110, 7], [67, 145, 10], [66, 135, 9]]
y = ['male', 'male', 'female', 'female', 'female', 'male']

