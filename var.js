var idade = 67 //a variável idade está armazenando o valor 67
console.log(`Você tem ${idade} anos.`)//exibe a mensagem no console
if (idade < 16) {
    console.log("Não vota.")
} else if (idade < 18 || idade > 65) {
        console.log("Voto opcional.")
    } else {
        console.log("Voto obrigatório.")
    }//o código decide se o voto é não obrigatório, opcional ou obrigatório, com base na idade da pessoa.