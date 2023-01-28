from flask import Flask,request,render_template
import numpy as np
import pickle
import sqlite3
import ast
labels=[
'Age', 'Gender', 'HS Type', 'Scholarship Type',
       'Working', 'Extra-curricular', 'Romantic relationship', 'Salary',
       'Transpotation mode', 'Accommodation type', 'Mother_edu', 'Father_edu',
       'Siblings', 'Parental_status', 'Mother_occu', 'Father_occu',
       'Study_hours', 'Reading(non-scientific)', 'Reading(scientific)',
       'Seminars/Conference', 'Project impact', 'Attendance',
       'Preparation method', 'Preparation date', 'Notes', 'Listening',
       'Discussion impact', 'Flip-cr', 'CGPA in last sem', 'CGPA expected'
]
displaydata=[
    {1: '18-21', 2: '22-25', 3: 'above 26'},
    {1: 'female', 2: 'male'},
    {1: 'private', 2: 'state', 3: 'other'},
    {1: 'None', 2: '25%', 3: '50%', 4: '75%', 5: 'Full'},
    {1: 'Yes', 2: 'No'},
{1: 'Yes', 2: 'No'},
{1: 'Yes', 2: 'No'},
    {1: 'USD 135-200', 2: 'USD 201-270', 3: 'USD 271-340', 4: 'USD 341-410', 5: 'above 410'},
    {1: 'Bus', 2: 'Private car/taxi', 3: 'bicycle', 4: 'Other'},
    {1: 'rental', 2: 'dormitory', 3: 'with family', 4: 'Other'},
    {1: 'primary school', 2: 'secondary school', 3: 'high school', 4: 'university', 5: 'MSc.', 6: 'Ph.D.'},
{1: 'primary school', 2: 'secondary school', 3: 'high school', 4: 'university', 5: 'MSc.', 6: 'Ph.D.'},
    {1: '1', 2: '2', 3: '3', 4: '4', 5: '5 or above'},
    {1: 'married', 2: 'divorced', 3: 'died - one of them or both'},
    {1: 'retired', 2: 'housewife', 3: 'government officer', 4: 'private sector employee', 5: 'self-employment', 6: 'other'},
{1: 'retired', 2: 'housewife', 3: 'government officer', 4: 'private sector employee', 5: 'self-employment', 6: 'other'},
    {1: 'None', 2: '<5 hours', 3: '6-10 hours', 4: '11-20 hours', 5: 'more than 20 hours'},
    {1: 'None', 2: 'Sometimes', 3: 'Often'},
{1: 'None', 2: 'Sometimes', 3: 'Often'},
{1: 'Yes', 2: 'No'},
    {1: 'positive', 2: 'negative', 3: 'neutral'},
{1: 'Always', 2: 'Sometimes', 3: 'Never'},
    {1: 'alone', 2:' with friends', 3: 'not applicable'},
    {1:' closest date to the exam', 2: 'regularly during the semester', 3: 'never'},
    {1: 'never', 2: 'sometimes', 3: 'always'},
{1: 'never', 2: 'sometimes', 3: 'always'},
{1: 'never', 2: 'sometimes', 3: 'always'},
    {1: 'not useful', 2: 'useful', 3: 'not applicable'},
    {1: '<2.00', 2: '2.00-2.49', 3: '2.50-2.99', 4: '3.00-3.49', 5: 'above 3.49'},
    {1: '< 2.00', 2: '2.00 - 2.49', 3: '2.50 - 2.99', 4: '3.00 - 3.49', 5: 'above 3.49'},
]


def insertdata(post):
    try:
        connection = sqlite3.connect('studentdb.db')


        # with open('schema.sql') as f:
        #     connection.executescript(f.read())

        cur = connection.cursor()

        cur.execute("INSERT INTO posts (question, description,like_count,comment_count) VALUES (?, ?,?,?)",
                    (post[0],post[1],post[2],post[3])
                    )

        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
    return True
def retrieve(id):
    connection = sqlite3.connect('studentdb.db')
    # with open('schema.sql') as f:
    #     connection.executescript(f.read())

    cur = connection.cursor()
    query = f"select * from students where ID='{str(id)}';"
    print(query)
    cur.execute(query)
    stud_details = cur.fetchall()
    print(stud_details)
    connection.close()
    return list(stud_details)

def update(i,newdata,s_id):
    try:
        connection=sqlite3.connect('studentdb.db')
        index=['Working', 'Romantic relationship', 'Salary', 'Transpotation mode',
           'Siblings', 'Reading(non-scientific)', 'Seminars/Conference',
           'Project impact', 'Attendance', 'Preparation date', 'Notes',
           'Listening', 'Discussion impact', 'Flip-cr', 'CGPA in last sem',
           'CGPA expected']
        cur=connection.cursor()
        query=f"update students set {index[i]}={newdata} where id={s_id};"
    except Exception as e:
        print(e)
        return render_template('error.html',exception=e)

def classifier(x):
    model=pickle.load(open('pickledmodel1.pkl','rb'))
    return model.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1]])

def cluster(x):
    clus = pickle.load(open('pickledmodel2.pkl', 'rb'))
    return clus.predict([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


app=Flask(__name__)
app.jinja_env.filters['zip'] = zip

@app.route('/',methods=['GET','POST'])
def home():
    # if request.method=='POST':
        test = []
        a = request.form.get('id')
        # post = ast.literal_eval(vals)
        print("Hiv",a)
        di = retrieve(a)
        di = list(di[0])
        di.pop(0)
        print(displaydata[0][1])
        for i in range(30):
            test.append(displaydata[i][di[i]])
        test2=np.reshape(test,(10,3))
        print(test2)
        return render_template('home.html',labels=np.reshape(labels,(10,3)),results=test2)
    # else:
        return render_template('home.html')

@app.route('/predict')
def predict():
    test=[]
    di=retrieve('STUDENT11')
    di=list(di[0])
    di.pop(0)
    print(displaydata[0][1])
    for i in range(30):
        test.append(displaydata[i][di[i]])
    print(test)
    return "Predict"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
