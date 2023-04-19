from transformers import pipeline

# Replace this with your own checkpoint
model_checkpoint = "bert-finetuned-squad/checkpoint-33276"
question_answerer = pipeline("question-answering", model=model_checkpoint)

context = """
chen is handsome.
"""
question = "who is handsome?"
print(question_answerer(question=question, context=context))
