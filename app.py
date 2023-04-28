from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

model_checkpoint = "roberta-finetuned-squad/checkpoint-33213"
question_answerer = pipeline("question-answering", model=model_checkpoint)


@app.route('/qa-text', methods=['POST'])
def qa_text():
    question = request.form['question']
    print(question)

    context = request.form['context']
    print(context)

    res = question_answerer(question=question, context=context)
    res['context'] = context
    return res


if __name__ == '__main__':
    app.run(debug=True)
