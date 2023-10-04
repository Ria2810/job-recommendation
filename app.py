from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
with open('C:/Users/riach/Projects/career_recommendation_model/career_svm.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        ques1 = request.form['QUESTION_1']
        if(ques1=='yes'):
            ques1 = 1
        elif(ques1=='no'):
            ques1 = 0

        ques2 = request.form['QUESTION_2']
        if(ques2=='yes'):
            ques2 = 1
        elif(ques2=='no'):
            ques2 = 0
        
        ques3 = request.form['QUESTION_3']
        if(ques3=='excellent'):
            part1 = 1
            part2 = 0
            part3 = 0
        elif(ques3=='medium'):
            part1 = 0
            part2 = 1
            part3 = 0
        elif(ques3=='poor'):
            part1 = 0
            part2 = 0
            part3 = 1

        ques4 = request.form['QUESTION_4']
        if(ques4=='yes'):
            ques4 = 1
        elif(ques4=='no'):
            ques4 = 0

        ques5 = request.form['QUESTION_5']
        if(ques5=='yes'):
            ques5 = 1
        elif(ques5=='no'):
            ques5 = 0

        ques6 = request.form['QUESTION_6']
        if(ques6=='yes'):
            ques6 = 1
        elif(ques6=='no'):
            ques6 = 0
        
        ques7 = request.form['QUESTION_7']
        if(ques7=='yes'):
            ques7 = 1
        elif(ques7=='no'):
            ques7 = 0

        ques8 = request.form['QUESTION_8']
        if(ques8=='yes'):
            ques8 = 1
        elif(ques8=='no'):
            ques8 = 0
        
        ques9 = request.form['QUESTION_9']
        if(ques9=='yes'):
            ques9 = 1
        elif(ques9=='no'):
            ques9 = 0

        ques10 = request.form['QUESTION_10']
        if(ques10=='yes'):
            ques10 = 1
        elif(ques10=='no'):
            ques10 = 0

        ques11 = request.form['QUESTION_11']
        if(ques11=='yes'):
            ques11 = 1
        elif(ques11=='no'):
            ques11 = 0

        ques12 = request.form['QUESTION_12']
        if(ques12=='yes'):
            ques12 = 1
        elif(ques12=='no'):
            ques12 = 0

        ques13 = request.form['QUESTION_13']
        if(ques13=='yes'):
            ques13 = 1
        elif(ques13=='no'):
            ques13 = 0

        ques14 = request.form['QUESTION_14']
        if(ques14=='yes'):
            ques14 = 1
        elif(ques14=='no'):
            ques14 = 0

        ques15 = request.form['QUESTION_15']
        if(ques15=='yes'):
            ques15 = 1
        elif(ques15=='no'):
            ques15 = 0

        ques16 = request.form['QUESTION_16']
        if(ques16=='yes'):
            ques16 = 1
        elif(ques16=='no'):
            ques16 = 0

        ques17 = request.form['QUESTION_17']
        if(ques17=='yes'):
            ques17 = 1
        elif(ques17=='no'):
            ques17 = 0

        ques18 = request.form['QUESTION_18']
        if(ques18=='yes'):
            ques18 = 1
        elif(ques18=='no'):
            ques18 = 0


        prediction = model.predict([[
            ques1,
            ques2,
            part1,
            part2,
            part3,
            ques4,
            ques5,
            ques6,
            ques7,
            ques8,
            ques9,
            ques10,
            ques11,
            ques12,
            ques13,
            ques14,
            ques15,
            ques16,
            ques17,
            ques18
        ]])

        if(prediction==0):
            return render_template("home.html",prediction_text="Recommended job: COMPUTER ANALYST")
        elif(prediction==1):
            return render_template("home.html",prediction_text="Recommended job: CONTENT WRITER")
        elif(prediction==2):
            return render_template("home.html",prediction_text="Recommended job: DATA ANALYST")
        elif(prediction==3):
            return render_template("home.html",prediction_text="Recommended job: DATA ENGINEER")
        elif(prediction==4):
            return render_template("home.html",prediction_text="Recommended job: DEVELOPER")
        elif(prediction==5):
            return render_template("home.html",prediction_text="Recommended job: ML ENGINEER")
        elif(prediction==6):
            return render_template("home.html",prediction_text="Recommended job: MANAGEMENT")
        elif(prediction==7):
            return render_template("home.html",prediction_text="Recommended job: MARKETING")
        elif(prediction==8):
            return render_template("home.html",prediction_text="Recommended job: NETWORK ENGINEER")
        elif(prediction==9):
            return render_template("home.html",prediction_text="Recommended job: SECURITY")
        
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)