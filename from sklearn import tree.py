from sklearn import tree
# [height, weight, shoe size]
X = [[181,80,44],[177,78,43],[160,60,38],[154,54,37],[166,63,40],[190,90,47],[175,64,39]]
Y = ['m','f','f','f','f','m','f']
clf = tree,DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict(((190,70,43)))
print prediction