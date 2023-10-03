// Creamos un objeto utilizando los literales {}
var perro = {
    nombre: "Milo",
    edad: 12,
    muerde: true,
    color: "Blanco",

    //Metodos
    quienSoy(){
        return "Soy "+ this.nombre
    },
    ladrar(){return this.nombre+" dice guau!"},
}

//Main: muesto resultados
 console.log(perro.nombre, "tiene", perro.edad, "años")
 console.log(perro.quienSoy())

 if(perro.muerde){
    console.log(perro.ladrar())
 }

