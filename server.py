from flask import Flask,render_template,redirect,session,request

app = Flask (__name__)
app.secret_key = "estoessecreto"
lista=[]

@app.route('/',methods=['GET'])
def paginaPrincipal():
    return render_template('index.html', count=len(lista))


@app.route('/nuevo',methods=['POST'])
def nuevaSesion():
    var=1
    lista.append(var)   
    return redirect( '/' )


@app.route( '/salir', methods=["GET"] )
def Reset():
    lista.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run(debug=True)