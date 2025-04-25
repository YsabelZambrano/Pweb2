function crearTabla(cantidad) {
    const tabla = document.getElementById('tabla');
    tabla.innerHTML = '';
    for (let i = 0; i < cantidad; i++) {
        const fila = document.createElement('tr');
        const celda = document.createElement('td');
        const input = document.createElement('input');
        input.type = 'number';
        input.value = Math.floor(Math.random() * 100);
        input.classList.add('valor');
        celda.appendChild(input);
        fila.appendChild(celda);
        tabla.appendChild(fila);
    }
}

function sumarValores() {
    const valores = document.querySelectorAll('.valor');
    let suma = 0;
    valores.forEach(input => suma += Number(input.value));
    document.getElementById('resultado').textContent = `Suma: ${suma}`;
}
