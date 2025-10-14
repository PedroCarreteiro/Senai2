import { useState } from "react"
import "./Quadradinho.css"

export default function Quadradinho({value, onQuadradoClick, classe}){

    return( 
        <button className={classe}
            onClick={onQuadradoClick}
        >
            {value}
        </button>
    )
}