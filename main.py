from flask import Flask, request, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('principal.html')

@app.route('/funcion1', methods=['GET', 'POST'])
def funcion1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        Vtarros = tarros * 9000
        if edad >= 18 and edad <= 30:
            pdescuento = Vtarros*0.15
        elif edad > 30:
            pdescuento = Vtarros*0.25
        elif edad < 18:
            pdescuento = Vtarros*0
        pfinal = Vtarros - pdescuento
        print(nombre, edad, tarros, Vtarros, pfinal)
        return render_template('funcion1.html', nombre=nombre, Vtarros=Vtarros, pdescuento=pdescuento, pfinal=pfinal)
    return render_template('funcion1.html')

@app.route('/funcion2', methods=['GET', 'POST'])
def funcion2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        if nombre == "juan" and contrasena=="admin":
            tipo = "administrador"
            return render_template('funcion2.html', nombre=nombre, tipo=tipo)

        elif nombre == "pepe" and contrasena == "user":
            tipo = "usuario"
            return render_template('funcion2.html', nombre=nombre, tipo=tipo)

        else:
            error = "Usuario o contraseña incorrectos."
            return render_template('funcion2.html', error=error)

    return render_template('funcion2.html')

if __name__ == '__main__':
    app.run(debug=True)