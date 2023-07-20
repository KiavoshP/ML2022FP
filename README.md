# ML Team 35 Project Final Report
## Introduction

Guessing a league champion or team’s performance has been an annual event that excites many soccer fans since the establishment of soccer leagues. However, these predictions often have low accuracy since they only take limited information into account. Our team aims to improve these predictions, by gathering data, and building a machine learning model. 

Studies have been done to improve sports forecasting measures. Bohumir[1]  attempted to bring in the Lichtman forecasting procedure which proved its effectiveness in different fields. Vaughan and his colleagues[2] also examined a few different prediction methodologies and suggested using Elo-based rating to predict Tennis match results. Likewise, predicting the outcome in sports fields has been drawing a great amount of attention worldwide. Our team is willing to follow this trend and propose our own model with high accuracy and reliability.

## Problem Definition
Sports are difficult to predict, and there is a large market of people interested in tools to help them predict outcomes. Our team will collect data depicting performances of soccer teams in several national leagues and analyze various factors that affect wins and losses. Based on such analysis, we aim to forecast the results of upcoming games. These predictions will be helpful for sports fans, sports bettors to predict the results of games, and also for coaches to plan out appropriate strategies. 

## Data Preprocessing
Our original dataset contained information about location of a game, game statistics within the game, referees in play, and the betting odds in various formats on the results of a game. This was generated from combining datasets from Leagues in England, France, Italy, Germany, Spain into one dataset with the same features. For our initial attempts, we have limited the data to numerical features only, to allow us to get early results more easily. This means that we have dropped the names of referees, and the physical location of soccer matches from our data set. In addition to this, the betting odds were also removed, as this data is the results of other professional algorithms designed to predict outcomes. Including this data therefore, would bias our results too easily. We want our predictions to be based on match performance as much as possible. 

After removing those features, what remained were the results of each soccer match (win, loss, or draw), and the numerical performances of each team within the game. Shots on goal, goals made, corners, fouls, etc. Obviously, using these performance metrics of a single game to predict the outcome of that same game does not have as much value (as the team with more goals will naturally win). But this data is still useful for showing the performance of each team against another. We wanted to use this data to predict games, but without using the direct results of one game to predict the result of that one game. 

To get around this, we computed a rolling average of performance for each team for each numerical feature over an entire season. Thereby transforming goals into average goals, and corners into average corners and so on. We did this for every game up to but not including the game in question, so the third match played by a team includes the features of average performance of games 1 and 2, but not including game 3. In this way, we can calculate the performance of the team, and use it to make a prediction against another, but without “cheating” by using that particular game's stats. Games with no historical data were then dropped from our database. We also generated a new feature of win percentages, to calculate the historical probability of a team winning a game. We theorize that the addition of this data will improve results by giving our predictions essentially a Bayesian prior. As a final step, the data is standardized using sklearn’s standard scalar fitting, prior to inputting our data into our feature reduction methods, in order to ensure proper functioning of our models.  

Before cleaning the data, total of 74 columns

 <img src="https://user-images.githubusercontent.com/44371962/161821624-ef54f896-0e78-49d4-889d-d6a260016e17.png" width="100%" style = "text-align:center;">

#### Cleaned and Preprocessed data, around 20 features:

 <img src="https://user-images.githubusercontent.com/44371962/161821220-4f790bd1-8d34-4f5c-bddb-ddebaab8cec5.png" width="100%" style = "text-align:center;">
 
## Methods
### Principal Component Analysis

We first used the PCA to reduce the dimensionality of the cleaned dataset which initially had more than 20 features. PCA is a technique used to reduce the dimensionality of a large dataset by combining correlated variables into a principal component that maximizes the variance of data points. During the process, some insignificant features are also removed from the dataset. PCA generally helps to find a trend that is hard to be recognized in a high-dimensional data set. By implementing the PCA, our team aimed to observe the trend between the features and the result of the game more clearly that would eventually help us generate better prediction models. We determined the number of components we should use by plotting ‘accuracy of the model vs number of components to pick out the best number of components that brings the most reasonable/reliable results while minimizing any information loss.

### Logistic Regression
After reducing the dimensionality of the dataset, we implemented the logistic regression to predict wins/losses of the home team. The (binary) logistic regression model is the regression analysis conducted to predict the outcome when there are two labels/classes. Since our dataset had two discrete labels depicting whether or not the home team won. The training dataset was created based on the data of leagues from 2012/13 to 2017/18, and the testing dataset was created based on the data of leagues from 2018/19. Using the model we built, when we tested with the test data, we obtained a score measuring how accurately the model predicted the result/outcome of 0.67, which was slightly less than what we expected but was reasonable. 

### Neural Network

Then we moved towards building a neural network model. The configuration is 5 fully connected layers, each with the count of our features as the number of neurons. Followed by 1 half sized fully connected layer, followed by our sigmoid single unit output layer. Finally, in all experiments we used binary cross-entropy for the model loss function and ‘adam’ for the optimizer. 

To determine which model brings the highest accuracy, we conducted different experiments on the above architecture where independent variables were (1) whether or not to run PCA on data beforehand, (2) number of components, (3) activation function (Relu or Sigmoid), (4) number of epochs. Below is the summary of experiments conducted.
<p align="center"> </p>

| Method   | PCA (Component Number) | Activation Function     | Epochs    |
| :------:       |    :------:   |    :------:   |  :------: |
| N.N.   | varied       | Sigmoid  | 20 |
| N.N.   | varied       | Relu  | 20 |
| N.N.   | -       | Sigmoid  | 20 |
| N.N.   | -       | Relu  | 20 |
| N.N.   | 4       | Sigmoid  | 20 |
| N.N.   | 4       | Relu  | 20 |
| N.N.   | -       | Relu  | 80 |
| N.N.   | 4       | Relu  | 80 |

We also removed 3 fully connected layers, and ran the model again in the following experiments.This configuration here is 2 fully connected layers, each with the count of our features as the number of neurons. Followed by 1 half sized fully connected layer, followed by our sigmoid single unit output layer. 
<p align="center"> </p>

| Method      | PCA (Component Number) | Activation Function     | Epochs     |
| :---:        |    :----:   |    :----:   |  :---: |
| N.N.   | -       | Sigmoid  | 20 |
| N.N.   | -       | Relu  | 20 |

After passing the data to the resulting neural network model, we examined the accuracy of both training and test dataset to pick the best model. After interpreting results, we move on to SVM as a final method to increase our prediction accuracy

### SVM

Finally, we worked on implementing a support vector machine to attempt to classify upcoming games into wins or losses for the home team. We used different numbers of features to test the accuracy of the algorithm in different cases listed below. 
    1. SVM with 3 PCA components 
    2. SVM with 3 PCA components & Standardization
    3. SVM with 3 PCA components & Normalization
    4. SVM without any preprocessing or PCA
    5. SVM on 4 different kernels (Linear / Poly / RBF / Sigmoid) & 10 different RandStates
<p align="center"> </p>

| Method      | Standardization | Normalization     | PCA     | PCA (Component #)   |Accuracy*  |
| :---:        |    :----:   |    :----:   |          :---: |          :---: |          :---: |
| SVM   | N        | N   | Y    |3    |0.64958     |
| SVM   | Y        | N      | Y     |3     |0.64450     |
| SVM   | N        | Y      | Y     |3     |0.62535     |
| SVM   | N        | N      | N     |-     |0.64451     |

<p style ="font-size:7pt; text-align:center;">*Rounded Values</p>

## Results and Discussion

### Logistic Regression
Using a logistic regression model to predict the outcome of upcoming games has worked with a decent level of accuracy so far. The model correctly predicts the final result of soccer matches with an accuracy of around 67%. To understand the effect of PCA on the model’s accuracy we varied the number of PCA components used before training the model. The figure below shows that the accuracy fluctuates pretty significantly based on the number of components used. 



<img width="%100" alt="LRvsPCA" src="https://user-images.githubusercontent.com/31297313/161649966-de174901-85de-457f-b3b0-4ab8fb5a3547.PNG">

### Neural Networks
Our initial tests we passed in varying numbers of PCA components to our Neural Network, to see which numbers could be optimal. The first test used a Relu activation function for all layers except the output, which yielded these results:
<p align="center">
 <img src="https://user-images.githubusercontent.com/44371962/165001580-0cc69612-bb78-46ef-b37f-500b3768b907.png" width="60%" align="center" style = "text-align:center;">
</p>
We repeated the experiment for sigmoid:

<p align="center">
 <img src="https://user-images.githubusercontent.com/44371962/165001597-803d9cfe-94e7-44f8-a048-aff1eaf50601.png" width="60%" align="center" style = "text-align:center;">
</p>

As we can see, accuracy peaked at 4 components, but also made a small rebound towards the end. For this reason we continued more experiments with 4 components, or all features directly. Referencing the table from earlier:

| Method      | PCA (Component Number) | Activation Function     | Epochs     | Final Accuracy |
| :---:        |    :----:   |    :----:   |  :---: | :---: |
| N.N.   | varied       | Sigmoid  | 20 | varied  |
| N.N.   | varied       | Relu  | 20 | varied |
| N.N.   | -       | Sigmoid  | 20 | 0.64507 |
| N.N.   | -       | Relu  | 20 | 0.63380 |
| N.N.   | 4       | Sigmoid  | 20 | 0.63943 |
| N.N.   | 4       | Relu  | 20 | 0.64225 |
| N.N.   | -       | Relu  | 80 | 0.61690 |
| N.N.   | 4       | Relu  | 80 | 0.62513 |

As we can see from our trial runs, the Sigmoid and Relu activation functions seem to have very similar results. The choice between the two does not seem to have a significant effect on the outcome, although a Relu does seem to work better for less features. Our accuracy appeared to peak at above 0.645 in the graph of our Relu test at 4 components.However, is still less than our results from logistic regression. We decided to examine the training length, as one final possible adjustment we could make to the hyperparameters. Since our accuracy peaked with a Relu with 4 PCA components, we ran a network again with all features and no PCA for 80 epochs, to see what affect further training would have:

<p align="center">
 <img src="https://user-images.githubusercontent.com/44371962/165001652-95d26af3-9c10-4488-a420-1f74c29f35d8.png" width="60%" align="center" style = "text-align:center;">
</p>

As you can see in the figure above, the accuracy in the training set increased as we increased the training time, but the accuracy of test data actually decreased starting at 40 epochs. This indicates the model had an overfitting problem, and test accuracy was not increasing past 65%. 
Similarly, more training did not seem to improve our 4 component model either with 80 epochs (see below):


<p align="center">
 <img src="https://user-images.githubusercontent.com/44371962/165001664-15373690-6a7c-4bce-848a-6c9245cc1969.png" width="60%" align="center" style = "text-align:center;">
</p>

As a final exploration, we removed 3 fully connected layers, and ran the model again in the following experiments, to check if our model was too complex. The configuration here is 2 fully connected layers, each with the count of our features as the number of neurons. Followed by 1 half sized fully connected layer, followed by our sigmoid single unit output layer. 

| Method      | PCA (Component Number) | Activation Function     | Epochs     | Final Accuracy |
| :---:        |    :----:   |    :----:   |  :---: | :---: |
| N.N.   | -       | Sigmoid  | 20 | 0.63459 | 
| N.N.   | -       | Relu  | 20 | 0.62982 |


This did not seem to improve our results. Clearly then this indicates that we needed more data to feed a neural network model here in order to prevent overfitting, or more or different features to enhance the information given to the model. This would explain why our hyper parameter tuning seems to max out at 65%, and further training does not seem to improve our results. 

### SVM

SVM was implemented using a variety of different parameters. We varied the number of components used in the SVM model to see how the accuracy of the model was affected. 


<img  width="%100" alt="pca ep" src="https://user-images.githubusercontent.com/31297313/164999356-c567db25-1d80-44d5-856f-603493fab680.PNG" width="100%" style = "text-align:center;">

Our best results occurred when we used 3 features and we were able to achieve an accuracy of around 65%. This is a reasonable score but it is still comparable to the accuracy we achieved using the other methods mentioned. We also experimented with different kernel types, we used a linear, polynomial, radial basis function and sigmoid kernels. The best results we got were when we used a linear kernel. Therefore we determined that the best set of parameters for our SVM model was to use 3 features along with a linear kernel. We also generated a confusion matrix for this best case SVM model (shown below). The model tended to predict a win for the home team more often than a loss and this seems to be a large reason why the model struggles, perhaps too much weight is being put on which team is playing at home when predicting the results of the game.


<img  width="%100" alt="pca ep" src="https://user-images.githubusercontent.com/31297313/164999345-9e1059d9-9ded-4878-a19a-5454cd20291c.PNG" width="100%" style = "text-align:center;">
## Conclusion

In this project, we examined the application of machine learning in sports forecasting. Given the test data, our goal was to predict the outcome of the game with decent accuracy. The data we initially collected from soccer leagues in England, France, Italy, Germany, Spain contained lots of information that may/may not be relevant to the outcome of the game. Thus, we first ran PCA on our preprocessed data to reduce the dimensionality. Then we moved onto building our model using Logistic Regression, Neural Network(NN) and Support Vector Machine(SVM) to see what fits the best for our data set.

On the test dataset, we got an accuracy score of 67% for linear regression, 64% for neural network model, and 65% for SVM model. Based on the results we got from PCA, the best number of features was 3, meaning that only a few of the features were good indicators for the game result. Therefore, we came to a conclusion that our data didn’t have enough features for NN or SVM to outperform the logistic regression which generally performs better on data with less features. However, considering the fact that predicting the future with limited dataset is not easy since many other factors that were not part of the data (ex. weather condition) might also have affected the outcome, we concluded that accuracy of 65% on average would be enough to appeal to sports fans or sports betters.

Nonetheless, one limitation of our model is that it did not take ‘draws’ into account. In our current models, losses and draws fall under the same label and are treated simply as ‘~win’, thus the model can only predict whether a team will win the game or not (loss/draw). Therefore, our future research should focus on implementing multi-class classification.




## References 
[1] L. Vaughan Williams, C. Liu, L. Dixon, and H. Gerrard, “How well do elo-based ratings predict professional tennis matches?,” Journal of Quantitative Analysis in Sports, vol. 
17, no. 2, pp. 91–105, 2020.
    
[2] B. Štědroň, “Experiments with the Lichtman forecasting procedure in the sport segment.,” Acta Universitatis Carolinae: Kinanthropologica, vol. 55, no. 1, pp. 49–49, 2019.


[3] C. M. Che Mohd Rosli, M. Z. Saringat, N. Razali, and A. Mustapha, “A comparative study of data mining techniques on football match prediction,” Journal of Physics: Conference Series, vol. 1020, p. 012003, 2018.


