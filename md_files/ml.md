# Machine Learning (ML) Notes

## What is Machine Learning?
Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed.

## Types of Machine Learning

### 1. Supervised Learning
- Uses labeled data
- Examples: spam detection, house price prediction

### 2. Unsupervised Learning
- Uses unlabeled data
- Examples: clustering, anomaly detection

### 3. Reinforcement Learning
- Learns through rewards and penalties
- Examples: game AI, robotics

## Machine Learning Workflow
1. Collect data
2. Preprocess data
3. Feature engineering
4. Split data into training and testing sets
5. Train model
6. Evaluate model
7. Tune hyperparameters
8. Deploy model

## Important Terms

### Features
Input variables used by the model.

### Label / Target
The value the model predicts.

### Dataset
Collection of data used for training and testing.

## Regression vs Classification

### Regression
Predicts continuous values.

**Example:** House prices

### Classification
Predicts categories.

**Example:** Spam or Not Spam

## Overfitting
Model memorizes training data and performs poorly on unseen data.

### Signs
- High training accuracy
- Low testing accuracy

## Underfitting
Model fails to learn important patterns from data.

### Signs
- Low training accuracy
- Low testing accuracy

## Common Algorithms

### Linear Regression
Used for predicting continuous values.

### Logistic Regression
Used for binary classification.

### Decision Trees
Rule-based learning algorithm.

### Random Forest
Collection of decision trees.

### Support Vector Machine (SVM)
Finds the best boundary between classes.

### Neural Networks
Inspired by the human brain and used extensively in deep learning.

## Evaluation Metrics

### Regression Metrics
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

### Classification Metrics
- Accuracy
- Precision
- Recall
- F1 Score

## Data Preprocessing
- Handle missing values
- Remove duplicates
- Encode categorical variables
- Normalize or standardize data
- Handle outliers

## Feature Engineering
Creating useful features from raw data.

### Examples
- Extract month from a date
- Calculate age from birth year
- Combine multiple columns

## Hyperparameters
Settings chosen before training.

### Examples
- Learning rate
- Batch size
- Number of trees
- Tree depth

## Bias-Variance Tradeoff

### High Bias
- Model too simple
- Causes underfitting

### High Variance
- Model too complex
- Causes overfitting

Goal: Balance bias and variance.

## Deep Learning
A subset of ML that uses neural networks with many layers.

### Applications
- Computer Vision
- NLP
- Speech Recognition

## Popular Python Libraries

### NumPy
Numerical computations

### Pandas
Data manipulation

### Matplotlib
Visualization

### Scikit-learn
Traditional ML algorithms

### TensorFlow
Deep learning framework

### PyTorch
Deep learning framework

## Real-World Applications
- Recommendation Systems
- Fraud Detection
- Medical Diagnosis
- Chatbots
- Search Engines
- Self-driving Cars
- Predictive Maintenance

## AI vs ML vs Deep Learning

AI
└── Machine Learning
    └── Deep Learning

- AI: Broad field of intelligent systems
- ML: Systems that learn from data
- Deep Learning: Neural-network-based ML

## Quick Interview Questions

1. What is Machine Learning?
2. Difference between supervised and unsupervised learning?
3. What is overfitting?
4. What is underfitting?
5. Difference between regression and classification?
6. What is feature engineering?
7. What is train-test split?
8. What is precision and recall?
9. What is a hyperparameter?
10. What is the bias-variance tradeoff?