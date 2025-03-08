const imageGallery = [
    "https://static.wikia.nocookie.net/fisch/images/d/df/7557_kg_nessie.png/revision/latest/scale-to-width-down/1000?cb=20241103044458",
    "https://static.wikia.nocookie.net/fisch/images/2/20/Aurora_Ancient_Kraken_V1.png/revision/latest/scale-to-width-down/185?cb=20250220090124",
    "https://static.wikia.nocookie.net/fisch/images/d/d1/Aurora_Northstar_Serpent.png/revision/latest?cb=20241215091636",
]
const imageElement = document.getElementById("GalleryImage");
const prevButton = document.getElementById("PrevBut");
const nextButton = document.getElementById("NextBut")
let currentImgIndex = 0;