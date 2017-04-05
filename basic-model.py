# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 22:45:39 2017
basic model with our own rules
@author: kartkond
"""


import os
import pandas as pd
os.getcwd()
titanic_train = pd.read_csv("train.csv")
titanic_train.shape
titanic_train.info()
titanic_train.describe()
titanic_train['Survived'].value_counts()
titanic_train.groupby('Survived').size()
titanic_train.groupby(['Sex','Survived']).size()
titanic_train.Cabin[titanic_train['Cabin'].isnull()] = str('OOO')
titanic_train.Cabin.apply(lambda x: str(x))
titanic_train.loc[titanic_train.Cabin != '000']
titanic_train.iloc[0:1,10]
titanic_test = pd.read_csv("test.csv")
titanic_test.shape
titanic_test.info()
titanic_test = pd.read_csv("test.csv")
titanic_test.apply(lambda x : sum(x.isnull()))
titanic_test.Fare[titanic_test['Fare'].isnull()] = titanic_test['Fare'].mean()        
X_test = titanic_test[['Sex','Embarked','Pclass','Fare']]
titanic_test['Survived'] = 0
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==1) & (titanic_test.Embarked == "C") ] = 1
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==1) & (titanic_test.Embarked == "S") ] = 1
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==2) & (titanic_test.Embarked == "C") ] = 1
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==2) & (titanic_test.Embarked == "Q") ] = 1
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==2) & (titanic_test.Embarked == "S") ] = 1
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==3) & (titanic_test.Embarked == "C") ] = 1
titanic_test.Survived[(titanic_test.Sex == "female") &  (titanic_test.Pclass ==3) & (titanic_test.Embarked == "Q") ] = 1
titanic_test.Survived[(titanic_test.Sex == "male") &  (titanic_test.Pclass ==1) & (titanic_test.Parch == 2) & (titanic_test.Embarked == "S") ] = 1
titanic_test.Survived[(titanic_test.Sex == "male") &  (titanic_test.Pclass ==3) & (titanic_test.Parch == 1) & (titanic_test.Embarked == "C") ] = 1
titanic_test.to_csv("submission.csv", columns=['PassengerId','Survived'], index=False)

