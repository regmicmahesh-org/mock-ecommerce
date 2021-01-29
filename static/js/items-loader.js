const ITEM_LIST_API = "http://localhost:9001/all"

const section = document.querySelector(".section")

function insertInDom(el){

        const div = document.createElement("div")
        div.classList.add("item")

        const img = document.createElement("img")
        img.width = 300
        img.height = 300
        img.src = `/static/${el.image}`

        const headingOne = document.createElement("h2")
        headingOne.textContent = el.item_name

        const headingTwo = document.createElement("h3")
        headingTwo.textContent = `Price: ${el.price}`

        const linkToDetails = document.createElement("a")
        linkToDetails.href = `/item.html#${el.id}`
        linkToDetails.textContent = "Buy"


        div.appendChild(img)
        div.appendChild(headingOne)
        div.appendChild(headingTwo)
        div.appendChild(linkToDetails)

        section.appendChild(div)

}


async function loadItems(count){


    try{

    const data = await fetch(ITEM_LIST_API)
    const jsonData = await data.json()
    section.innerHTML = ""

    for(const el of jsonData){

        insertInDom(el)

    }

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