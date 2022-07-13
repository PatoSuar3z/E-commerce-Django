

let url = "http://127.0.0.1:8000/api/Producto/"
$.get(url, function(respuesta){

    respuesta.forEach(function(item){
        console.log(item)
        let res = document.querySelector(`#block`);
        res.innerHTML +=`<div class="col-sm-6 col-md-4 col-lg-3 p-b-35 isotope-item women">

                        <div class="block2">
                        <div class="block2-pic hov-img0">
                            <img src="${item.imagen}" alt="IMG-PRODUCT">
                        </div>

                        <div class="block2-txt flex-w flex-t p-t-14">
                            <div class="block2-txt-child1 flex-col-l ">
                                <a class="" id="nombreplanta">
                                    ${item.nombre}
                                </a>

                                <span class="stext-105 cl3" id="s">
                                    $${item.precio}
                                    </div>
                            
                                    </div>
                                </div>
                            </div>
        `
    })
        
})




