from flask import Flask, render_template,request
import csv
import os
import logging
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("sign-in.html")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/log-in", methods=["GET", "POST"])
def lo():
    if request.method == "POST":
        name= request.form.get("nome")
        password = request.form.get("senha")
        with open("usuarios.csv", mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for line in reader:
                if line["name"] == name and line["password"] == password:
                    return render_template("index.html")
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/sign-in", methods=["GET", "POST"])
def si():
    print(os.listdir())
    if request.method == "POST":
        
        
        with open("usuarios.csv", mode="r", encoding="utf-8") as csv_file:
            reader = list(csv.reader(csv_file))
            last_id = 0

            if len(reader) > 1:
                last_row = reader[-1]
                if last_row:
                    last_id = int(last_row[0])

            next_id = last_id + 1

            novo_usuario = [
            next_id,
            request.form.get("nome"),
            request.form.get("senha"),
            request.form.get("nivel"),
            request.form.get("preference"),
            ]

        
        with open("usuarios.csv", mode="a", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(novo_usuario)

        return render_template("login.html")

    else:
        return "Erro no sign in."
    

@app.route("/adicionar", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name= request.form.get("nome")
        url = request.form.get("imagem")
        description = request.form.get("descricao")


        return f"Encontro adicionado."

    else:
        return "Erro ao adicionar."
    

    
if __name__ == "__main__":
    app.run(debug = True) 