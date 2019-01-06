  function lenstr() {
    var s = document.getElementById("t").value;
    m = 0;
    x = " ";
    p = s.split(" ");
    for (i = 0; i < p.length; i++) {
      if (m < p[i].length)
        m = p[i].length;
      x = p[i];
    }
    document.getElementById("l").innerHTML = m;
  }