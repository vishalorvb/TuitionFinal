console.log("carsousel javascript working")
let slideIntervalTime = 2500
let currentSlide = 0
let slide = document.querySelectorAll('.slides')
slide[currentSlide].style.display = 'block'



function changeSlide() {
    console.log("inside change slide")
    console.log("currentSlide ==="+currentSlide)

    if (currentSlide+1  >= slide.length) {
        console.log("inside IF")
        slide[slide.length - 1].style.display = 'none'
        currentSlide = 0
        slide[currentSlide].style.display = 'block'
    }
    else{
        console.log("inside ELSE")
        slide[currentSlide].style.display = 'none'
        currentSlide += 1 
        slide[currentSlide].style.display = 'block'
    }
}

let timeout = setInterval(changeSlide,slideIntervalTime)

function stopSlide(){
    clearInterval(timeout)
}
function restartSlide(){
    timeout = setInterval(changeSlide,slideIntervalTime)
}



