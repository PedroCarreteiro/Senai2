import { useState } from 'react'
import './App.css'

import Tabuleiro from './components/Tabuleiro/Tabuleiro'
import Instrucao from './components/Instrucao'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <main>
        {/* <Instrucao /> */}
        <div className="tabuleiroBackground">
          <Tabuleiro className="tabuleiro"/>
        </div>
      </main>
    </>
  )
}

export default App
