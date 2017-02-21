set.seed(5000)
library(randomForest)
library(plotly)

wine.url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine.raw <- read.csv(wine.url, header=FALSE, sep=",")

colnames(wine.raw) <- c("Type"
                    , "Alcohol"
                    , "Malic_Acid"
                    , "Ash"
                    , "Alcalinity_of_Ash"
                    , "Magnesium"
                    , "Total_phenols"
                    , "Flavanoids"
                    , "Nonflavanoid_phenols"
                    , "Proanthocyanins"
                    , "Color_Intensity"
                    , "Hue"
                    , "OD280_OD315_of_diluted_wines"
                    , "Proline")


# bestmtry <- tuneRF(wine.raw[-1],as.factor(wine.raw$V1),ntreeTry=100,
#                    stepFactor = 1.5,improve = 0.01,trace = TRUE,plot = TRUE,doBest = FALSE)

bestmtry <- tuneRF(wine.raw[-1],as.factor(wine.raw$Type),ntreeTry=100,
                  stepFactor = 1.5,improve = 0.01,trace = TRUE,plot = TRUE,doBest = FALSE)

#bestmtry = 2 or 4

#rf <- randomForest(as.factor(V1) ~.,data = wine.raw, importance = TRUE, ntree=500, mtry = 2)

rf <- randomForest(as.factor(Type) ~.,data = wine.raw, ntree=500, importance = TRUE)


rf

importance(rf)
varImpPlot(rf)

##################
#K-mean

myvars <- c("Proline", "Color_Intensity", "Flavanoids")

winecluster <- kmeans(wine.raw[myvars], 3, nstart = 20) #3 is number of cluster

#table(winecluster$cluster, wine.raw$V1)

winecluster$cluster <- as.factor(winecluster$cluster)

#ggplot(wine.raw, aes(V8, V11, V14, color = as.factor(V1))) + geom_point()
# ggplot(wine.raw, aes(x=V8, y=V11, z=V14, color = winecluster$cluster)) + geom_point()


#### kmeans plot 3d graph


plot_ly(wine.raw, x = ~Proline, y = ~Color_Intensity, z = ~Flavanoids, color = ~winecluster$cluster, text = "test")


#########################
#BIRCH



