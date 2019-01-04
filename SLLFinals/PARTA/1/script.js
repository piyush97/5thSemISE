function check() {
  var number = document.getElementById("number").value
  if (isNaN(number)) {
    alert("Enter a number");
  } else if (number % 3 == 0 || number % 7 == 0) {
    document.getElementById("result").innerHTML = "Divisible by 3 or 7"
  } else {
    document.getElementById("result").innerHTML = "Not Divisible"
  }
}
