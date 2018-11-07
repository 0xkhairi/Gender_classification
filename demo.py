from sklearn import tree

# [hight, weight, shoe size]
x = [[159,58,38],[181,80,44],[177,70,43],[145,45,73],
[166,65,40],[175,64,39],[190,90,45],[181,80,44],
[177,76,40],[171,75,42],[150,55,38]]
y = ['female', 'male','male','female','female','male','male','male','female','male','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[150,70,38]])

print(prediction)
