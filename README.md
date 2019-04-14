# ust-machine-learning-project

#### University of St. Thomas (Data Science M.S. Program) - Machine Learning Class Project

#### Group Members
| Name | github |
| ---- | ------ |
|      |        |
| Logan Butler  | [lbutlr093](https://github.com/lbutlr093) |
|   Yee Lee     | [overwear](https://github.com/overwear)   |
| Rijesh Kumar  | [rijesh4](https://github.com/rijesh4)     |

## Project Proposal
NFL Game Play Prediction

Our team will be working with NFL data. This dataset comes from Kaggle, where it was originally scraped using an API hosted by the NFL, for the years 2009 to 2018. The raw dataset has 103 attributes with over 250,000 instances with each instance representing a single play. The dataset consists of 4 types of variables. Examples of these types include: yardln (yard line the play starts on - numerical continuous), playtype (run, pass, kick - categorical nominal), pass type (short, deep - categorical binary), and timeunder (remaining time in the quarter - numerical discrete).

We believe the main complexity is feature selection as there are 103 features in this dataset. We will initially choose features which we think are significant to determine the outcome of a play and then compare that to choosing statistically significant features by applying feature selection algorithms. Another challenge will be working with this data as time-series data. This means that the time on the clock, and previous actions may determine future plays. In order to work with these time data, we may add in additional features to indicate what happened on recent plays since we believe the action of a play may be dependent on previous (recent) plays.

Our first goal is to predict, on any given play, whether our opponent will run or throw the ball. Our next goal will be determining which direction the ball is run (left or right), or how far the ball will be thrown (short or deep). By taking the result from the first prediction, we can use the pipeline feature to feed results into predicting how the play will turn out. We believe this is similar to what a real-world example of analyzing this data may look like. Our first prediction will give us the most important information on how to defend against any given play, with the second prediction allowing us to position the run/pass defense in the correct positions.

We hope to achieve that by doing the following steps:
1.	Merge the separate data sets into one data set by concatenating 10 seasons.
2.	Select most significant columns as per task at hand.
3.	Fill in null numerical values with imputed mean/mode if required.
4.	Label Encode/One Hot Encode the categorical values
5.	Normalize selected numerical features
6.	Split the data
7.	Use a machine learning model (or models) to predict and analyze.  
8.	Repeat and adjust above steps with a different models. 

The two techniques we want to initially use to analyze this data are Decision Trees and Naive Bayes Classifier. With an understanding of how the game functions, a decision tree seems to be a great initial approach to classifying whether the throw or run the ball. We believe that the Naive Bayes classifier is another great approach as this data set will be prone to overfitting given the circumstances of the gameplay. With the Naive Bayes classifier approach, we are assuming that each feature is independent of each other and have independent probabilistic contributions to whether the play was a throw or a run.
