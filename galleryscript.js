const imageGallery = [
    "images/image.webp",
    "images/image2.webp",
    "images/image3.webp"
]
const imageElement = document.getElementById("GI");
const prevButton = document.getElementById("PrevBut");
const nextButton = document.getElementById("NextBut");
let currentImgIndex = 0;
function updateImage() {
    imageElement.src = imageGallery[currentImgIndex];
};
nextButton.addEventListener("click", function(){
    currentImgIndex = (currentImgIndex +1) % imageGallery.length
    updateImage()
});
prevButton.addEventListener("click", function(){
    currentImgIndex = (currentImgIndex -1) % imageGallery.length
    updateImage()
});
updateImage();
