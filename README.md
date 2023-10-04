# JOB RECOMMENDATION MODEL

## Overview
This project aims to provide job recommendations based on user responses to a quiz. Users answer a series of questions, and a job role is recommended according to their responses.

## Data Description
The dataset comprises the following questions:

- Did you do web development during college time?
- Are you good at Data analysis?
- Reading and writing skills.
- Are you a tech person?
- Were you in a non-tech society?
- Are you good at coding?
- Have you developed mobile apps?
- Are you good at communication?
- Do you have specialization in security?
- Have you ever handled large databases?
- Do you have knowledge of statistics and data science?
- Are you proficient in English?
- Have you ever managed some event?
- Do you write technical blogs?
- Are you into marketing?
- Are you an ML expert?
- Do you have a lot of connections?
- Have you ever built a live project?

Based on these questions, one of the following job roles is assigned:

- Management
- Developer
- Marketing
- Network Engineer
- Data Engineer
- Content Writer
- ML Engineer
- Data Analyst
- Computer Analyst
- Security

## Exploratory Data Analysis (EDA) and Feature Engineering
- Missing values were removed from the dataset.
- One-hot encoding was applied to the input variables.
- Label encoding was performed for the target variable.
  
## Model Training
The data was split into training and testing sets. Two machine learning models were trained:

- Decision Tree Classifier (using both Gini Index and Information Gain).
- Support Vector Machine (SVM).

The trained models were saved as pickle files for later use.

## Deployment
The model is deployed as a web application using Flask. Users can access the application through a user-friendly interface where they answer the quiz questions. After submitting their responses, the application provides a job recommendation based on their inputs.

## Preview
<img width="600" alt="image" src="https://github.com/Ria2810/job-recommendation/assets/67699993/2beb261a-620a-42b4-a195-121bb0eafd49"> <img width="600" alt="image" src="https://github.com/Ria2810/job-recommendation/assets/67699993/3491037c-268b-450c-b91c-6617dbf98867">

## Project Structure
The project directory contains the following files and folders:

- app.py: The Flask application for serving the model and user interface.
- career_svm.pkl: The trained SVM model saved as a pickle file.
- templates/: This folder contains HTML templates for rendering the web pages.
- static/: This folder contains CSS and other static files for styling the web pages.

## Usage
- To run the application locally:

- Clone this repository to your local machine.

- Ensure you have Python and Flask installed.

- Open a terminal in the project directory.

- Run the following command to start the Flask server:
<code>python app.py</code>
- Access the application by opening a web browser and navigating to http://localhost:5000.


Feel free to explore and use the project to get personalized job recommendations based on your quiz responses.

#### Note: This project serves as a demonstration of using machine learning for job recommendation and web deployment. The dataset and models are for demonstration purposes only and may not provide accurate job recommendations in real-world scenarios.
