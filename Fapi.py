from flask import Flask, jsonify, request
app = Flask(__name__)

languages = ["JS","Python","Ruby"]
# languages = [{"name" : "JS"},{"name" : "Python"},{"name" : "Ruby"}]

@app.route("/lang/<string:name>")
def returnone(name):
    langs = [language for language in languages if language == name]
    return langs[0]

@app.route("/lang")
def returnAll():
    return jsonify(languages)

@app.route("/lang", methods = ['POST'])
def addOne():
    language = request.json['name']

    languages.append(language)
    return jsonify({'languages':languages})

@app.route("/lang/<string:name>",methods=["PUT"])
def editOne(name):
    langs = [language for language in languages if language == name]
    langs[0] = request.json['name']
    return jsonify({'laguages' : langs[0]})

@app.route("/lang/<string:name>",methods=["DELETE"])
def removeOne(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'laguages' : langs[0]})

if __name__ == "__main__":
    app.run(debug=True)