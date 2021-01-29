const ORDER_URL = "http://localhost:9000/order";
let counter = 0;

async function buttonHandler() {
  const name = element.item_name
  const price = element.price
  const number = document.getElementById("number").value;
  const time = Date.now().toLocaleString();
  const elem = document.getElementById("status");

  try {
    const resp = await fetch(ORDER_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "text/plain",
      },
      body: JSON.stringify({ item: name, price, contact: number, time }),
    });
    if (resp.status != 200) {
      throw Error;
    } else {
      elem.textContent = "Success!";
      elem.style.color = "green";
    }
  } catch (e) {
    counter++;

    if (counter < 6) {
      elem.textContent = `Retrying ${counter}.`;
      elem.style.color = "pink";
      console.log(` Retrying ${counter} times.`);
      setTimeout(buttonHandler, 1000 * counter);
    } else {
      elem.textContent = "Service Down!";
      elem.style.color = "red";
    }
  }
}

const button = document.getElementById("orderButton");
if (button) button.addEventListener("click", buttonHandler);


