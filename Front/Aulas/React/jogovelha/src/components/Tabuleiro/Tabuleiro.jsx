import Quadradinho from "../Quadradinho/Quadradinho";
import "./Tabuleiro.css"
import { useState } from "react";

export default function Tabuleiro(){

    const[quadrados, setQuadrados] = useState(Array(9).fill(" "))
    const [xProximo, setXProximo] = useState(true)
    const [classe, setClasse]

    function handleClick(i){
        const next = quadrados.slice()
        
        //Verificar o conteúdo e só alterar se o que já estiver for " "
        if(next[i]===" "){
            //Jogar de forma alternada, atribuindo os valores alternadamente
            if(xProximo){
                next[i] = "X"
                setClasse = "quadradinVerde"
            } else {
                next[i] = "O"
            }
        }

        //Setar o valor
        setQuadrados(next)

        //Alterar o turno
        setXProximo(!xProximo)
    }

    return(
        <>
            <div className="fileira">
                <Quadradinho value={quadrados[0]} onQuadradoClick = {() => handleClick(0)}/>
                <Quadradinho value={quadrados[1]} onQuadradoClick = {() => handleClick(1)}/>
                <Quadradinho value={quadrados[2]} onQuadradoClick = {() => handleClick(2)}/>
            </div>
            <div className="fileira">
                <Quadradinho value={quadrados[3]} onQuadradoClick = {() => handleClick(3)}/>
                <Quadradinho value={quadrados[4]} onQuadradoClick = {() => handleClick(4)}/>
                <Quadradinho value={quadrados[5]} onQuadradoClick = {() => handleClick(5)}/>
            </div>
            <div className="fileira">
                <Quadradinho value={quadrados[6]} onQuadradoClick = {() => handleClick(6)}/>
                <Quadradinho value={quadrados[7]} onQuadradoClick = {() => handleClick(7)}/>
                <Quadradinho value={quadrados[8]} onQuadradoClick = {() => handleClick(8)}/>
            </div>
        </>     
    )
}