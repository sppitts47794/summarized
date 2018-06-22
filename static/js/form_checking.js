function formValidation(){
  var urlForm = document.forms['inputform']['url-field'].value;
  var bulletPointForm = document.forms['inputform']['quantity'].value;
  if (urlForm == ""){
    alert('Please enter URL to be summarized!');
    return false;
  }
  if (bulletPointForm == ""){
    alert('Please choose # of bullet points you want URL to be summarized in.');
    return false;
  }
}
