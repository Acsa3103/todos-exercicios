function somar() {
    const num1 = parseFloat (document.getElementById("numero1").value);
    const num2 = parseFloat (document.getElementById("numero2").value);
    const soma = num1 + num2; document.getElementById ("resultado") .textContent = "A soma é:" + soma;
}

function subtrair() {
    const num1 = parseFloat (document.getElementById("numero1").value);
    const num2 = parseFloat (document.getElementById("numero2").value);
    const subtração = num1 - num2; document.getElementById ("resultado2") .textContent = "A subtração é:" + subtração;
}

function dividir() {
    const num1 = parseFloat (document.getElementById("numero1").value);
    const num2 = parseFloat (document.getElementById("numero2").value);
    const divisão = num1/num2; document.getElementById ("resultado3") .textContent = "A divisão é:" / divisão;
}

function multiplicação() {
    const num1 = parseFloat (document.getElementById("numero1").value);
    const num2 = parseFloat (document.getElementById("numero2").value);
    const divisão = num1/num2; document.getElementById ("resultado3") .textContent = "A divisão é:" / divisão;
}

