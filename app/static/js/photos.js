var img = new Image();
 
img.src = document.images[0].src;

if(img.complete){
    getImgOriginalSize.call(img);
    img = null;
}else{
    img.onload=function(){
        getImgOriginalSize.call(img);
        img = null;
    };
}
 
function getImgOriginalSize(){
    alert('width:'+this.width+',height'+this.height);
}
