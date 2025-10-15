import Quadradinho from "../Quadradinho/Quadradinho";
import "./Tabuleiro.css"
import { useState } from "react";

//Sortear quem vai começar
const sortearTurnoInicial = () => {
    return Math.random() >= 0.5;
}

export default function Tabuleiro(){

    const [quadrados, setQuadrados] = useState(Array(9).fill(""))
    const [xProximo, setXProximo] = useState(sortearTurnoInicial())

    //Função de clique dos botões do tabuleiro para atribuir valores
    function handleClick(i){

        //Caso o quadrado já tenha valor ou haja um vencedor
        if (quadrados[i] || calcularVencedor(quadrados)) {
            return;
        }

        const next = quadrados.slice()
        
        if(xProximo){
            next[i] = "X"
        } else {
            next[i] = "O"
        }

        setQuadrados(next)

        setXProximo(!xProximo)
    }

    //Reiniciar o jogo
    function reiniciarJogo() {
        setQuadrados(Array(9).fill(""));
        setXProximo(sortearTurnoInicial());
    }

    //Alterar classe de estilo de acordo com o valor do quadrado
    function determinarClasse(valor){
        if(valor === "X"){
            return "quadradinVerde";
        } else if (valor === "O"){
            return "quadradinLaranja";
        } else {
            return "quadradin";
        }
    }

    //Verificar o vencedor de acordo com todas as condições de vitória
    function calcularVencedor(quadrados) {
        const linhas = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];
        for (let i = 0; i < linhas.length; i++) {
            const [a, b, c] = linhas[i];
            if (quadrados[a] && quadrados[a] === quadrados[b] && quadrados[a] === quadrados[c]) {
                return quadrados[a];
            }
        }
        return null;
    }

    //Verificações de vencedor ou empate
    const vencedor = calcularVencedor(quadrados);
    let status;
    if(vencedor){
        status = "Vencedor: "+vencedor
    } else {
        if (!quadrados.includes("")) {
             status = "Empate";
        } else {
             status = "Próximo jogador: " + (xProximo ? "X" : "O");
        }
    }

    return(
        //Conteúdo geral, com o status, botão de reiniciar e tabuleiro
        <div className="general">
            <div className="statusContainer">
                <div className="status">{status}</div>
                <button 
                    className="botaoReiniciar" 
                    onClick={reiniciarJogo}
                >
                    Reiniciar Jogo
                </button>
            </div>
                <div className="tabuleiro">
                <div className="fileira">
                    <Quadradinho value={quadrados[0]} onQuadradoClick = {() => handleClick(0)} classe={determinarClasse(quadrados[0])}/>
                    <Quadradinho value={quadrados[1]} onQuadradoClick = {() => handleClick(1)} classe={determinarClasse(quadrados[1])}/>
                    <Quadradinho value={quadrados[2]} onQuadradoClick = {() => handleClick(2)} classe={determinarClasse(quadrados[2])}/>
                </div>
                <div className="fileira">
                    <Quadradinho value={quadrados[3]} onQuadradoClick = {() => handleClick(3)} classe={determinarClasse(quadrados[3])}/>
                    <Quadradinho value={quadrados[4]} onQuadradoClick = {() => handleClick(4)} classe={determinarClasse(quadrados[4])}/>
                    <Quadradinho value={quadrados[5]} onQuadradoClick = {() => handleClick(5)} classe={determinarClasse(quadrados[5])}/>
                </div>
                <div className="fileira">
                    <Quadradinho value={quadrados[6]} onQuadradoClick = {() => handleClick(6)} classe={determinarClasse(quadrados[6])}/>
                    <Quadradinho value={quadrados[7]} onQuadradoClick = {() => handleClick(7)} classe={determinarClasse(quadrados[7])}/>
                    <Quadradinho value={quadrados[8]} onQuadradoClick = {() => handleClick(8)} classe={determinarClasse(quadrados[8])}/>
                </div>
            </div>
        </div>    
    )
}