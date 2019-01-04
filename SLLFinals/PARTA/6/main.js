function calculate() {
  var number1 = parseInt(document.getElementById("num1").value)
  var number2 = parseInt(document.getElementById("num2").value)
  if (document.getElementById("add").checked) {
    document.getElementById("result").innerText = number1 + number2
  } else if (document.getElementById("sub").checked) {
    document.getElementById("result").innerText = number1 - number2
  } else if (document.getElementById("mul").checked) {
    document.getElementById("result").innerText = number1 * number2
  } else {
    if (number2 == 0) {
      alert("Trying to Divide by 0, huh? I got YOU!")
    } else {
      document.getElementById("result").innerText = number1 / number2
    }
  }
}