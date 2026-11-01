##AI Engineering Lab — Day 1 Answers##
1. How to prepare a Python development environment?
A Python development environment is a setup that allows us to write, execute, test and manage Python programs.

Steps to prepare it:
1. Install Python from the official Python website.
2. Install Visual Studio Code (VS Code) as the code editor.
3. Install Git for version control.
4. Create a project folder.
5. Create a virtual environment using:
python -m venv .venv


6. Activate the environment:
.\.venv\Scripts\Activate.ps1


7. Install the required Python libraries.

Why is it important?

It provides an organized workspace, manages dependencies and helps developers build AI and machine learning applications.
2. How to install and use Python libraries?
Python libraries are collections of pre-written code that help developers perform specific tasks without implementing everything from scratch.

We use pip, Python's package installer, to install libraries.

Example:
pip install numpy pandas matplotlib scikit-learn


Some important libraries:
Library	Purpose
NumPy	Mathematical calculations and arrays
Pandas	Data manipulation and analysis
Matplotlib	Data visualization and graphs
Scikit-learn	Machine learning algorithms
Jupyter	Interactive coding and experiments

Example of using a library:
import numpy as npnumbers = np.array([10, 20, 30, 40])print(np.mean(numbers))



Output:
25.0


Here, NumPy calculates the average of the numbers.
3. How does a machine learning model learn from data?
Machine learning is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions or decisions.

A machine learning model generally learns through these steps:
1. Data collection: Collect relevant information.
2. Data preparation: Clean and organize the data.
3. Training: Provide the data to the learning algorithm.
4. Prediction: The model generates outputs.
5. Error calculation: Compare predictions with actual answers.
6. Optimization: Adjust model parameters to reduce errors.
Machine learning process
Training data

Machine learning algorithm

Predictions

Calculate errors and improve
 Repeat training


Example: A model learns the relationship between study hours and exam scores using previously collected student data.
4. How does linear regression make predictions?
Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value based on input data.

It finds a mathematical relationship between input and output variables.

Its equation is:
\[
\hat y=wx+b
\]

Where:
- \(x\) = Input value.
- \(w\) = Weight or slope.
- \(b\) = Bias or intercept.
- \(\hat y\) = Predicted output.
Example:

Suppose a student studies for 5 hours. A trained model uses the learned weight and bias to estimate the student's exam score.


\(\hat{y} = b_0 + b_1x\)

\(\hat{y} = \text{8.49} - \text{0.54}x\)
Estimated intercept · R-squared = 0.72

Fit
InterceptThrough origin




Focus
DataLinePredictionsResiduals






Generate new data




Drag a point to refit the line.
2468102468PredictorResponse





Give feedback

In our Day 1 project, we used study hours as input and exam scores as output.

The model learned a regression line and used it to predict a score for 7.5 study hours.
5. What are weight, bias, loss and gradient descent?
These are important concepts used in machine learning.

A. Weight

Weight determines how strongly an input variable influences the prediction.

For example, in linear regression, a higher positive weight means the predicted score increases more for each additional study hour.

B. Bias

Bias is an additional parameter that shifts the prediction up or down.

It allows the model to fit the data more accurately.

C. Loss

Loss measures the difference between the model's predictions and actual values.

One commonly used loss function is Mean Squared Error (MSE):
\[
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
\]

A smaller loss generally indicates better predictions on the training data.

D. Gradient Descent

Gradient descent is an optimization algorithm that adjusts weight and bias to reduce the loss.

It repeatedly updates the model parameters in the direction that reduces the error.

In simple words, it helps the model improve its predictions during training.
6. How does learning rate affect model training?
Learning rate is a hyperparameter that determines the size of each update to the model's parameters during gradient descent.

Think of it as the step size the model takes while trying to reduce its error.
Learning rate	Effect
0.001	Smaller updates; learning may be slower
0.01	Larger updates; potentially faster learning
0.1	Large updates; may cause unstable training

Our Day 1 experiment:

We tested two learning rates.
Parameter	0.001	0.01
Weight	8.07	7.97
Bias	6.25	6.94
Predicted score	66.79	66.74

Both models successfully trained.

Conclusion: Choosing a suitable learning rate is important because it affects training speed and stability.
7. How to publish your code using GitHub?
GitHub is an online platform used to store, manage, share and collaborate on software projects.

Git is a version control system that tracks changes in code.

Steps we followed:
1. Created a GitHub account.
2. Created a repository named ai-engineering-lab.
3. Initialized Git in our local project.
4. Added project files.
5. Created our first commit.
6. Connected the local project to GitHub.
7. Pushed the code to the remote repository.
Important Git commands:
Command	Purpose
git init	Initializes a Git repository
git add .	Stages project files
git commit -m "message"	Saves a version of the project
git branch -M main	Names the main branch
git remote add origin URL	Connects the GitHub repository
git push -u origin main	Uploads code to GitHub

Our first repository:
AI Engineering Lab — GitHub Repository8. What did we achieve in Day 1?
We completed our first practical AI Engineering session.
Achievement	Status
Python environment setup	Completed
Python library installation	Completed
Linear regression implementation	Completed
Weight and bias understanding	Introduced
Gradient descent	Introduced
Learning-rate experiment	Completed
Regression graph visualization	Completed
GitHub repository creation	Completed
First project upload	Completed


Final revision — Important concepts to remember
Concept	Remember it as
Python	                               Programming language
NumPy	                               Numerical calculations
Pandas   	                           Data handling
Matplotlib	                           Graphs and visualization
Machine Learning	                   Learning patterns from data
Linear Regression                      Predicting numerical values
Weight	                               Influence of input
Bias	                               Prediction adjustment
Loss	                               Prediction error
Gradient Descent	                   Reducing prediction error
Learning Rate	                       Size of parameter updates
GitHub	                               Code hosting and collaboration