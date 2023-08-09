var num = 0;
document.addEventListener("DOMContentLoaded", function(){
    document
        .querySelector("#list")
        .addEventListener("click", function(e){
            if (document.querySelector(".nav").classList.contains("on")){
                //메뉴 slide
                document.querySelector(".nav").classList.remove("on");
            } else {
                //메뉴 slidein
                document.querySelector(".nav").classList.add("on");
            }
        });
});

/*const navbar = () => {
    if (num%2==0){
        document.getElementById("list").style.display = "none";
        document.getElementById("nav").style.display = "block";
        document.getElementById("darkside").style.display = "block";
    }
    else {
        document.getElementById("list").style.display = "block";
        document.getElementById("nav").style.display = "none";
        document.getElementById("darkside").style.display = "none";
    }
    num += 1;
}*/
