export function somar(a, b) {
  return a + b;
}

export function subtrair(a, b) {
  return a - b;
}

export function multiplicar(a, b) {
  return a * b;
}

export function dividir(a, b) {
  if (b === 0) {
    console.log("⚠️ Não é possível dividir por zero!");
    return null;
  }
  return a / b;
}