from flask import Flask, render_template , jsonify , request
from flask_pymongo import PyMongo
import openai
import os
from dotenv import load_dotenv

load_dotenv()


AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

client = openai.AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=API_VERSION
)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://pavan:charan12@microblog.afyjl.mongodb.net/"
mongo = PyMongo(app)

# Getting chats history from mongodb database
@app.route("/")
def hello_world():
    chats = mongo.db.chat.find({})
    x = mongo.db
    myChats = [chat for chat in chats]
    return render_template("index.html",myChats = myChats)


@app.route("/api",methods = ["GET","POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")

        chat = mongo.db.chat.find_one({"question":question})
        if chat:
            data = {"answer":f"{chat['answer']}"}
            return jsonify(data)
        else :
            # Obtaining the response from GPT-3.5 OpenAI model
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
            data = {"answer" : response.choices[0].message.content}
            # Storing each QA in mongodb database
            mongo.db.chat.insert_one({"question":question , "answer" : response.choices[0].message.content})
            return jsonify(data)
    data = {"result":"Hello! How can I assist you today?"}
    return jsonify(data)

app.run(debug=True)