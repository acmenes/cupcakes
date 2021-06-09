alert("JAVASCRIPT IS BACK")

$('.delete-cupcake').click(function(){
    alert("YOU CLICKED")
})

const BASE_URL = "http://localhost:5000"

const body = document.body

/// Generate HTML for cupcake data ///

function cupcakeHTML() {
    const cupcakeData = document.createElement("div")
    cupcakeData.setAttribute("id", "placeholder")
    cupcakeData.append("<p>Do I remember javascript?</p>")
    body.append(cupcakeData)
    return cupcakeData
}
  
async function showCupcakes(){
    const res = await axios.get(`${BASE_URL}/json/cupcakes`)
    console.log (res)
}

