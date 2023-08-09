var num=0;
const navbar = () => {
    if (num%2==0){
        document.getElementById("list").style.display = "none";
        document.getElementById("list2").style.display = "block";
        document.getElementById("nav").style.display = "block";
        document.getElementById("darkside").style.display = "block";
    }
    else {
        document.getElementById("list").style.display = "block";
        document.getElementById("list2").style.display = "none";
        document.getElementById("nav").style.display = "none";
        document.getElementById("darkside").style.display = "none";
    }
    num += 1;
}
