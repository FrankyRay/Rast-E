async function getProducts() {
    return fetch("json/").then((res) => res.json())
}
function addProduct() {
    form = new FormData(document.querySelector('#productForm'));
    console.log(form)

    fetch("create-product-ajax", {
        method: "POST",
        body: form,
    })
    .then(_ => refreshProducts());

    document.getElementById("productForm").reset();
    document.querySelector('[data-bs-dismiss="modal"]').click();
    return false;
}

async function refreshProducts() {
    const productList = document.getElementById("products");
    const products = await getProducts();

    if (products.length == 0) {
        productList.innerHTML = `<div class="card text-center">
            <div class="card-header">Oh no</div>
            <div class="card-body">
                <img
                    src="image/pib_sad.webp"
                    class="card-img-top w-25"
                    alt="Puss In Cat: Sad Image"
                />
                <p class="card-text">
                    Tidak ada produk. Tambahkan untuk menampilkan produk disini
                </p>
                <a href="create-product" class="btn btn-primary">
                    Produk baru
                </a>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createProduct">
                    Produk baru (AJAX)
                </button>
            </div>
        </div>`;
    } else {
        inner = `<div class="card"> <div class="card-header">Hello world </div> <div class="card-body">`;
        products.forEach(product => {
            inner += `
                    <div class="card" style="width: 18rem">
                        <!-- <img src="..." class="card-img-top" alt="..." /> -->
                        <div class="card-body">
                            <h3 class="card-title">${ product.fields.name }</h3>
                            <hl />
                            <p class="card-text">
                                ${ product.fields.description }
                                <br />
                                <span>$${ product.fields.price } | ${ product.fields.rating }/5</span>
                            </p>
                            <p></p>
                            <div class="d-flex flex-row-reverse gap-2">
                                <a
                                    href="edit-product/${product.pk}"
                                    class="btn btn-outline-primary"
                                    >Edit</a
                                >
                                <a
                                    href="delete-product/${product.pk}"
                                    class="btn btn-outline-danger"
                                    >Delete</a
                                >
                            </div>
                        </div>
                    </div>`
        });
        inner += `</div>
            <div class="p-2">
                <a href="create-product" class="btn btn-primary">
                    Produk baru
                </a>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createProduct">
                    Produk baru (AJAX)
                </button>
            </div>
        </div>`

        productList.innerHTML = inner;

        console.log(productList.innerHTML);
    }
}

document.getElementById("productForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProduct();
})

refreshProducts();