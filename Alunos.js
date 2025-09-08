let aluno = "Robson";
let nota1 = 80;
let nota2 = 70;
let nota3 = 50;
let nota4 = 90;
let media = 0;
let result = "";

media = (nota1+nota2+nota3+nota4)/4;
if (media >=70){
    result = "Aprovado"
} else {
    result = "Reprovado"
}

console.log("O aluno "+aluno+" tem a média "+ media + " e está: "+result);
