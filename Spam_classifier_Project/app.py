import nltk
from flask import Flask, request ,render_template
import re
import pickle
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()

app = Flask(__name__)


def convert(sentences):
    corpus=[]
    for i in range(len(sentences)):
        review=re.sub('[^A-Za-z0-9]+',' ',sentences[i])
        review=review.lower()
        review=review.split()
        review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review= ' '.join(review)
        corpus.append(review)
    return corpus


tfidf=pickle.load(open('vectorizer.pkl','rb'))

model=pickle.load(open('model.pkl','rb'))



@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def result():
    if (request.method == 'POST'):
        # 0.Get the input from html page
        input_sms = str(request.form["input_sms"])
        # 1.Preprocess the input
        converted_sentence = convert([input_sms])
        # 2.Vectorize the preprocessed input
        vectorized_sms = tfidf.transform(converted_sentence).toarray()
        # 3.Model
        prediction = model.predict(vectorized_sms)[0]
        # 4.Display Result
        if prediction == 0:
            final_result = "Not Spam"
        else:
            final_result = "Spam"

        return render_template('prediction.html',prediction=final_result)


if __name__ == '__main__':
    app.run(debug=True)

