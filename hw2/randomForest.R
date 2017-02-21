set.seed(2222)
library(mlbench)
library(caret)
library(randomForest)

wine.url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine.raw <- read.csv(wine.url, header=FALSE, sep=",")
#define the control using a random forest selection function
control <- rfeControl(functions=rfFuncs, method="cv", number=5)
#run the RFE algorithm in caret lib
results <- rfe(wine.raw[,2:14],as.factor(wine.raw[,1]), sizes=c(2,14), rfeControl=control)
#summarize the results
print(results)
#list the chosen features
predictors(results)
plot(results, type=c("g","o"))

#V11, V8, V14

# control <- trainControl(method="repeatedcv", number=10, repeats=3)
# # train the model
# model <- train(diabetes~., data=PimaIndiansDiabetes, method="lvq", preProcess="scale", trControl=control)
# # estimate variable importance
# importance <- varImp(model, scale=FALSE)
# # summarize importance
# print(importance)
# # plot importance
# plot(importance)