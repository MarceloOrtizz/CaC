//Creamos un objeto utilizando los literales {}

var persona = {
    nombre: "Juan",
    apellido: "Paz",
    dni: 11223344,
}

// Main: Muestro los resultados

console.log(persona) // Imprime el objeto
console.log(persona.nombre)
console.log(persona.dni)

// Puedo modificar propiedades, utilizando corchetes

persona['nombre']="Pepe"
console.log(persona.nombre)