window.onload = function () {

  var teslaModels = [{
      "model": "modelS",
      "name": "Model S",
      "price": 69200,
      "year": 2016,
      "image": "s.png"
    },
    {
      "model": "modelX",
      "name": "Model X",
      "price": 83700,
      "year": 2017,
      "image": "x.png"
    },
    {
      "model": "model3",
      "name": "Model 3",
      "price": 35000,
      "year": 2017,
      "image": "3.png"
    },
  ];

  //Generate HTML for Menu Bar
  teslaModels.forEach(function (item, index) {
    listElemet = document.createElement("th")
    listElemet.onmouseover = function () {
      document.getElementById("name").innerHTML = teslaModels[index].name;
      document.getElementById("price").innerHTML = teslaModels[index].price;
      document.getElementById("year").innerHTML = teslaModels[index].year;
      document.getElementById("image").src = teslaModels[index].image;
    };
    listElemet.innerHTML = item.name
    document.getElementById("menu").appendChild(listElemet)
  })
}