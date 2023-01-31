# **Go Idento**: Helps you identify how to improve yourself...

## A project made in <u>BitNBuild hackathon</u> 2k23 by team Terminal Evolvers


### Project Description
To understand the student's rate of progress, it is crucial to forecast their performance. "Prevention is better than cure," goes the saying. The success of students can be significantly increased with early identification of at-risk students and preventive actions. The recommended task is utilized to assess a student's performance right now and forecast their outcomes in the future. Every year, many kids fall behind because of inadequate supervision and assistance. Based on the results, teachers can concentrate on the students who are more likely to receive lower grades in the final semester and can also help the student by identifying needs for the final exams.

### Contents of this repository
This project uses 
* for front-end:
  * `HTML`
  * `CSS`
  * `JavaScript`
  * `Flask`
* for back-end:
  * `sqlite3`
* for prediction model:<br>
Each of these models spit out a single prediction which is then combined to give a final prediction which also states a reason for the student's specific predicted     outcome.
  * a `classification` model using scikit-learn.
  * a `clustering` model using scikit-learn. <br>

* for dataset:
  * `'Higher Education Students Performance Evaluation Dataset'` from UCIML repository.
* for deployement:
  * `Vercel`

### How to Use the Project
A  student, registered with the database, only needs to put in the unique student ID, the model automatically fetches data from the database to predict their future outcome. If the student does not have his/her details stored in the database, the student will have to fill in all the details before getting a predcition. This details will get stored in the database automatically for use in the future. Students also have the feature to edit certain attributes that get changed over time.
