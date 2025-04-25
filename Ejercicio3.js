function diasParaArequipa() {
    const hoy = new Date();
    const esteAnio = hoy.getFullYear();
    const fiesta = new Date(`${esteAnio}-08-15`);

    if (hoy > fiesta) {
        fiesta.setFullYear(esteAnio + 1);
    }

    const diff = fiesta - hoy;
    const dias = Math.ceil(diff / (1000 * 60 * 60 * 24));
    return dias;
}

console.log(`Faltan ${diasParaArequipa()} días para el día de Arequipa`);