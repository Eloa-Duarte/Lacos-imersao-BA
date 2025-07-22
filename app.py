from flask import Flask, render_template,request
import csv
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("sign-in.html")


@app.route("/log-in", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name= request.form.get("nome")
        password = request.form.get("senha")

        return f"Log in bem sucedido."

    else:
        return "Erro no log in."
    

@app.route("/sign-in", methods=["GET", "POST"])
def addd():
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
            request.form.get("preferences"),
            ]

        with open("usuarios.csv", mode="a", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(novo_usuario)




        return f"Sign in bem sucedido."

    else:
        return "Erro no sign in."
    

    
if __name__ == "__main__":
    app.run(debug = True) 