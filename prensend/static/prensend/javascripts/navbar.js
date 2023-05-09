var num = 0;
const navbar = () => {
    
    if (num%2==0){
        document.getElementById("nav").style.display = "block";
    }
    else {
        document.getElementById("nav").style.display = "none";
    }
    num += 1;
}
