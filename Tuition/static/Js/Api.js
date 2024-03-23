var inputField = document.getElementById("searchInput")
var suggestionList = document.getElementById("suggestionList");
var listItems = suggestionList.getElementsByTagName("li");
var searchType = document.getElementById("searchType")

searchType.addEventListener("change", (e) => {
    suggestionList.innerHTML = ""
    inputField.value=""
    document.getElementById("inputLabel").textContent = e.target.value == 1 ? "Pincode" : "City"
})

inputField.addEventListener("focus", (e) => {
    document.getElementById("suggestionListdiv").style.display = "block"
})

inputField.addEventListener("blur", (e) => {
    setTimeout(() => {
        document.getElementById("suggestionListdiv").style.display = "none"
    }, 100);
})
inputField.addEventListener("input", (e) => {
    if(searchType.value == '1' && e.target.value.length > 2){
        getPincode(e.target.value)
    }
    if(searchType.value == '2'){
        getCity(e.target.value)
    }
})


for (var i = 0; i < listItems.length; i++) {
    listItems[i].addEventListener("click", function () {
        inputField.value = this.textContent
    });
}




function getPincode(pin) {
    suggestionList.innerHTML = ""
    axios.get(`http://127.0.0.1:8000/getPincode?pincode=${pin}`).then(res => {
        res.data.forEach(element => {
            var newLi = document.createElement("li");
            newLi.textContent = element.Pincode;
            suggestionList.appendChild(newLi);
        });
        for (var i = 0; i < listItems.length; i++) {
            listItems[i].addEventListener("click", function () {
                inputField.value = this.textContent
            });
        }
    })
}

function getCity(city) {
    suggestionList.innerHTML = ""
    axios.get(`http://127.0.0.1:8000/getCity?city=${city}`).then(res => {
        res.data.forEach(element => {
            var newLi = document.createElement("li");
            newLi.textContent = element.city;
            suggestionList.appendChild(newLi);
        });
        for (var i = 0; i < listItems.length; i++) {
            listItems[i].addEventListener("click", function () {
                inputField.value = this.textContent
            });
        }
    })
}