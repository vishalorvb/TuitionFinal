 function validateForm(names, cname) {
    let status = true
    names.forEach(element => {
        let collection = document.getElementsByName(element)
        for (let i = 0; i < collection.length; i++) {
            if (collection[i].value == undefined || collection[i].value.trim() == "") {
                collection[i].className += ` ${cname}`
                status = false;
                console.log("error")
                console.log(element.value)
            }
        }
    });
    return status;
}