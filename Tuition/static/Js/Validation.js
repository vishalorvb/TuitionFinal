 
 function containsOnlyNumbers(str) {
    return /^[0-9]+$/.test(str);
  }
 
 function validateForm(names, cname) {
    console.log("vlaidation called")
    let status = true
    names.forEach(element => {
        let collection = document.getElementsByName(element)
        for (let i = 0; i < collection.length; i++) {
            if (collection[i].value == undefined || collection[i].value.trim() == "") {
                collection[i].className += ` ${cname}`
                status = false; 
            }
            if((collection[i].name.includes("phone")) && !(containsOnlyNumbers(collection[i].value))){
                collection[i].className += ` ${cname}`
                status = false;
            }
        }
    });
    return status;
}

// comment