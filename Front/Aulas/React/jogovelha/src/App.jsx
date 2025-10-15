import './App.css'

import Tabuleiro from './components/Tabuleiro/Tabuleiro'

function App() {

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
