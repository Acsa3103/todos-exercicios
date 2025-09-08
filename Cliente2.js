const cliente = {
    nome: "Robson",
    idade: 29,
    cpf: "05086678086",
    email: "robinho@polo.com.br",
  };

  const cliente2 = {
    nome: "Nãosei",
    idade: 50,
    cpf: "12345678998",
    email: "vaisaber@polo.com.br"
  }

  const cliente3 = {
    nome: "Marcos",
    idade: 11,
    cpf: "12345678998",
    email: "vaisaber@polo.com.br"
  }

  const cliente4 = {
    nome: "Isa",
    idade: 40,
    cpf: "12345678998",
    email: "vaisaber@polo.com.br"
  }

  const chaves = ["nome", "idade", "cpf", "email"];
  chaves.forEach((chave) => {
    console.log(`O campo ${chave} tem valor ${cliente[chave]}`);
  });

  const tabela = ["nome", "idade", "cpf", "email"];
  tabela.forEach((tabela) => {
    console.log(`O campo ${tabela} tem valor ${cliente2[tabela]}`);
  });

  const chaves_s = ["nome", "idade", "cpf", "email"];
  chaves.forEach((chaves_s) => {
    console.log(`O campo ${chaves_s} tem valor ${cliente3[chaves_s]}`);
  });
  
  const chaves_E = ["nome", "idade", "cpf", "email"];
  chaves.forEach((chaves_E) => {
    console.log(`O campo ${chaves_E} tem valor ${cliente4[chaves_E]}`);
  });
