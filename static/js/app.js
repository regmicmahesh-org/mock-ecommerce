const URL = "http://localhost:8000/order"
let counter = 0

async function buttonHandler(){

    const name = document.getElementById("name").value
    const price = parseInt(document.getElementById("price").value)
    const number = document.getElementById('number').value
    const time = Date.now().toLocaleString()
    const elem = document.getElementById("status")
    


        try{
        const resp = await fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept' : 'text/plain'
              },
              body: JSON.stringify({item: name, price, contact: number,time}),
        })
        if(resp.status != 200){
            throw Error

        }else{
            
            elem.textContent = "Success!"
            elem.style.color = "green"

        }

        }catch(e){

            counter++
           
            if(counter < 4){
                elem.textContent = `Retrying ${counter+1}.`
                elem.style.color = "pink"
                console.log(` Retrying ${counter+1} times.`)
                setTimeout(buttonHandler, 1000 * counter)
            }else{
                elem.textContent = "Service Down!"
                elem.style.color = "red"
            }

        }

    }

const button = document.getElementById("orderButton")
button.addEventListener("click", buttonHandler)
