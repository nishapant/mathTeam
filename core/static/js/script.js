var menu = false;

function showMenu(){
  if(menu==false){
    document.getElementById('navBar').style.display = "block";
  }else{
    document.getElementById('navBar').style.display = "none";
  }
  menu = !menu;
}

function reset(){
  document.getElementById('navBar').style.display = "block";
  var menu = true;
}
