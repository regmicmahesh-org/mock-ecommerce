const section = document.querySelector(".section")
let element = {}
async function loadItems(count){


    try{

        const hashName = window.location.hash
        const itemId = hashName.slice(1, hashName.length)

    const data = await fetch(`http://localhost:9001/details/${itemId}/`)
    const jsonData = await data.json()
    element = jsonData
    const img = document.getElementById("itemThumbnail")
    img.src = `/static/${element.image}`
    

    }catch(e){
        count--;
        if(count < 0){
            section.textContent = "Failed to Load..."
            return
        }else{
        setTimeout(loadItems, 1000, count)
        }
    }
}


loadItems(5)