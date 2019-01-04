function by2() {
  var number = document.getElementById("num").value
  var result;
  result = 2 * number;
  document.getElementById("result").innerHTML = result;
}
function byN() {
    var number = document.getElementById("num").value
     number *= number;
    document.getElementById("result").innerHTML = number;
}