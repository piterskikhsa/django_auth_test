document.addEventListener("DOMContentLoaded",function(){
    var password = document.getElementById("passw"),
        confirm_password = document.getElementById("passw-c");

function validatePassword(){
  if(password.value === confirm_password.value && password.value != '') {
    if (confirm_password.classList.contains('warning')){
        confirm_password.classList.remove('warning');
    }
    password.classList.add('success')
    confirm_password.classList.add('success')
  } else {
        confirm_password.classList.add('warning');
        if (confirm_password.classList.contains('success')){
            confirm_password.classList.remove('success');
            if (password.classList.contains('success')){
                password.classList.remove('success');
            }
        }
  }
}

password.addEventListener('keyup', validatePassword)
confirm_password.addEventListener('keyup', validatePassword)

});