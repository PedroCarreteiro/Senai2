// //sync
// function resultado (resultado){
//     console.log("O resultado é ",resultado);
// }

// function soma (n1, n2, callback){
//     let resultado = n1 + n2;
//     callback(resultado);
// }

// soma(1, 2, resultado)

// //async
// const loginUser = (usuario, senha, callback) => {
//     setTimeout(() =>{
//         console.log("user logged!")
//         callback({usuario})
//     }, 1500)

//     console.log("After setTimeout")
// }

// const user = loginUser("pedro", 1234, (user) => {
//     console.log({user})
// })

// //promise
// function prometa(sucesso){
//     return new Promise ((resolve, reject) => {
//         setTimeout(()=>{
//             if(sucesso === "labubu"){
//                 resolve(console.log("Sucesso total"))
//             } else {
//                 reject(console.log("Não sucesso total"))
//             }
//         }, 2000)
//     })
// }
//prometa("labubu")

fetch("https://pokeapi.co/api/v2/pokemon/ditto")
.then(res=> res.json())
.then(dados => {
    console.log(dados)
})
.catch(err => console.error("Não foi possível achar o caminho",err))
// .then(mensagem => console.log(mensagem))
// .catch(erro => console.log(erro))