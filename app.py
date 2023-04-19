from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

model_checkpoint = "bert-finetuned-squad/checkpoint-33276"
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


# @app.route('/qa-pdf', methods=['GET', 'POST'])
# def qa_pdf():
#     if request.method == 'POST':
#         pdf_document = PyPDF2.PdfFileReader(request.files['file'])
#
#         question = request.form['question']
#         print(question)
#
#         context = ''
#         for i in range(pdf_document.numPages):
#             page = pdf_document.getPage(i)
#             context += page.extractText()
#         print(context)
#
#         return question_answerer(question=question, context=context)
#     else:
#         return render_template('qa-pdf.html')


if __name__ == '__main__':
    app.run(debug=True)
