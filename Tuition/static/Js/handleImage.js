function previewImage(event) {
    var input = event.target;
    var reader = new FileReader();
  
    reader.onload = function() {
      var imgElement = document.getElementById("preview-image");
      imgElement.src = reader.result;
    };
  
    reader.readAsDataURL(input.files[0]);
  }