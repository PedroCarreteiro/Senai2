import Image from "./image";
import './style.css';

export default function Profile(){
    return(
        <>
            <link rel="stylesheet" href="style.css"/>
            <article className="perfil">
                <Image></Image>
                <h1>COISA RUIM (Max Verstappen)</h1>
                <p>É o COISA RUIM não tem jeito</p>
            </article>
        </>
    );
}