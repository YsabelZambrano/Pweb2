function getDiaSemana(numeroDia) {
    const dias = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"];
    return dias[numeroDia] || "Dia invalido";
}

console.log(getDiaSemana(new Date().getDay()));
