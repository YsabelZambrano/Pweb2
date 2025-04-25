function obtenerCodigoMeet(url) {
    const partes = url.split('/');
    const codigo = partes[partes.length - 1];
    return codigo.replaceAll('-', '');
}
console.log(obtenerCodigoMeet("https://meet.google.com/abc-def-ghi"));