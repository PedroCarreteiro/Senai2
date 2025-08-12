let cats = ["Kuromi", "Kitty", "Purim", "Roll", "Retsuko"];
let info = "Meus gatos chamam: ";

for (let i = 0; i < cats.length; i++){
    //if e else para tirar a ultima virgula
    if(i != cats.length-1){
        info += cats[i] + ", ";
    } else {
        info += cats[i]
    }
    console.log("contador: "+i);
    console.log("gatos: "+cats[i])
}

console.log(info);