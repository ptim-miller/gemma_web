function showProgress() {
  var x = document.getElementById("progress");
  var y = document.getElementById("answerBlock");
  x.style.display = "block";
  y.innerHTML = "";
}
 document.registrationForm.baseForm.onchange = function(){
    document.registrationForm.baseForm.value = document.registrationForm.baseForm.value;
 }
 function grabText(ele) {
    if(event.key === 'Enter') {
       document.getElementById("bSubmit").click();
    }
}