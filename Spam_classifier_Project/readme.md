# Spam Classifier Using Machine Learning
## Spam Classifier
This repository consists of files required for end to end implementation and deployment of Machine Learning Spam Classifier web application created with Flask and deployed on the Heroku platform.

## CountVectorizer:

The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary.

## TF-IDF Vectorizer
Tf-idf is a method which gives us a numerical weightage of words which reflects how important the particular word is to a document in a corpus. A corpus is a collection of documents. Tf is Term frequency, and IDF is Inverse document frequency. This method is often used for information retrieval and text mining.

#### Term Frequency:

Term frequency is defined as the number of times a word (i) appears in a document (j) divided by the total number of words in the document.
inverse document frequecy | Bag-of-words vs TFIDF vectorization

![image](https://user-images.githubusercontent.com/93968656/141609082-c3dd68c0-5860-422d-a602-149d816cef66.png)


#### Inverse Document Frequency:

Inverse document frequency refers to the log of the total number of documents divided by the number of documents that contain the word. The logarithm is added to dampen the importance of a very high value of IDF.
log of idf

![image](https://user-images.githubusercontent.com/93968656/141609074-128b69bc-3e78-4b5c-b1e1-d57605c54350.png)


TFIDF is computed by multiplying the term frequency with the inverse document frequency.
Tfidf | Bag-of-words vs TFIDF vectorization

![image](https://user-images.githubusercontent.com/93968656/141609069-1054a80d-1c3b-4514-9bf5-f1c7a1165eb4.png)

## Project Explanation
The Spam Classifier is a Flask web application which predicts if a message E-mail/SMS is a spam message or not. The dataset is available at Kaggle, and it's provided by UCI Machine Learning.

## Dataset link
Spam Classifier Dataset https://www.kaggle.com/uciml/sms-spam-collection-dataset

## Screenshot
#### Home page 
![home page](https://user-images.githubusercontent.com/93968656/141608503-3f5ee35f-63cb-4532-9e41-b8a597feb8a3.png)


##### Spam Message
![flask spam 1](https://user-images.githubusercontent.com/93968656/141608440-b94777b6-0983-42ce-b6d5-0c3f360101a8.png)
![flask spam 2](https://user-images.githubusercontent.com/93968656/141608448-67327b3c-068b-43ed-a863-286e3158df19.png)

##### Ham Message (not spam)

![flask ham 1](https://user-images.githubusercontent.com/93968656/141608456-e7acc362-16b0-4096-b25a-3e69ee861646.png)
![flask ham 2](https://user-images.githubusercontent.com/93968656/141608464-81c27124-1ed5-450b-91a2-3303f2807c63.png)

## Technologies Used

![Flask and python](https://user-images.githubusercontent.com/93968656/141474681-ea61de53-c27e-4818-b0a8-379371f84da0.png)
![image](https://user-images.githubusercontent.com/93968656/141649883-b4a3b95a-1687-4eec-a94b-3350a2fc501b.png)



## Deployement on Heroku

##### Login or signup in order to create virtual app. You can either connect your github profile or download Heroku cli to manually deploy this project.
![image](https://user-images.githubusercontent.com/93968656/141474123-3dc0d678-af4b-4527-92af-17d05a5d0481.png)

##### The next step would be to follow the instruction given in the Heroku Documentation to deploy a web app.

## How to run the project on local system?
##### 1. Clone this repository in your local system.
##### 2. Open your IDE from your project directory and Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt.
##### 3. Run the app.py file by clicking the run button.
##### 4. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
##### Hurray! That's it.


## Link to the application
Check out the live demo: https://spam-classifier-flaskapp.herokuapp.com/

### Note:
#### On clicking the app link you might land on the page that shows
![internal error](https://user-images.githubusercontent.com/93968656/141607689-dcb16a81-b01f-4174-b9ce-27c9b0842521.png)

#### This problem is taken in consideration and we are working to fix this issue.
#### Sorry for the Inconvenience.

