// about menu
const aboutPop = document.getElementById('aboutPop');
const aboutClose = document.getElementById('aboutClose');
// contact menu
const contactPop = document.getElementById('contactPop');
const contactClose = document.getElementById('contactClose');
// listings
const listings = document.getElementById('listingsGoHere');
// loading buttons
const load10 = document.getElementById('load');
const load100 = document.getElementById('load100');
const load250 = document.getElementById('load250');
// select buttons
const selectButtons = document.getElementById('selectButtons');
const favorite = document.getElementById('favorite');
const share = document.getElementById('share');
const hide = document.getElementById('hide');
const clear = document.getElementById('clear');
// popup
const popup = document.getElementById('popup');
const popuptext = document.getElementById('popuptext');
// local variables
let selected = [];
let count = 0;

// "$("#daTable").trigger('addRows', [text, false, null]);" NEEDS TO BE USED INSTEAD OF "listing.innerHTML += text"
// DUE TO TABLESORTER JQUERY PLUGIN BEING DEPENDENT ON STATIC TABLES. THUS, WE NEED TO USE 'addRows' TABLESORTER METHOD
// AND TABLES W/ DATA ADDED USING VANILLA JS LOOPS ARE NOT SUPPORTED

// asyncronous on page load event listeners
window.addEventListener('load', async () => {
    // get listings json
    const entriesJSON = await fetch('/json/entries.json');
    const entries = await entriesJSON.json();

    // load 10 listings on page load
    for (let i = 0; i < 10; i++) {
        let text = `            <tr class="listings" name="${i}" id="listings">
                <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[i].name}</p></td>
                <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[i].address}</p></td>
                <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[i].neighborhood}</p></td>
                <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[i].beds}</p></td>
                <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[i].baths}</p></td>
                <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[i].area}</td>
                <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[i].price}</p></td>
                <td id="link" class="normal"><a class="listings" id="listings" name="linkToListing" href="${entries[i].link}">Link</a></td>
                <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input class="listings" name="listingSelector" type="checkbox" value="${i}"></div></td>
            </tr>`
        $("#daTable").trigger('addRows', [text, false, null]);
        count++;
    }

    // load 10 listings on button click
    load10.addEventListener('click', async () => {
        if ((entries.length - count) > 10) {
            const max = count + 10;
            for (let i = count; i < max; i++) {
                let text = `            <tr class="listings" name="${i}" id="listings">
                        <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].name}</p></td>
                        <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].address}</p></td>
                        <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].neighborhood}</p></td>
                        <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].beds}</p></td>
                        <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].baths}</p></td>
                        <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].area}</td>
                        <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].price}</p></td>
                        <td id="link" class="normal"><a class="listings" id="listings" name="linkToListing" href="${entries[count].link}">Link</a></td>
                        <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input value="${i}" class="listings" name="listingSelector" type="checkbox"></div></td>
                        </tr>`
                $("#daTable").trigger('addRows', [text, false, null]);
                count++;
            }
        }
        else {
            for (let i = count; i < entries.length; i++) {
                let text = `            <tr class="listings" name="${i}" id="listings">
                        <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].name}</p></td>
                        <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].address}</p></td>
                        <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].neighborhood}</p></td>
                        <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].beds}</p></td>
                        <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].baths}</p></td>
                        <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].area}</td>
                        <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].price}</p></td>
                        <td id="link" class="normal"><a class="listings" id="listings" name="listings" href="${entries[count].link}">Link</a></td>
                        <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input value="${i}" class="listings" name="listingSelector" type="checkbox"></div></td>
                        </tr>`
                $("#daTable").trigger('addRows', [text, false, null]);
                count++;
            }
        }
    });    

    // load 100 listings on button click
    load100.addEventListener('click', async () => {
        if ((entries.length - count) > 100) {
            const max = count + 100;
            for (let i = count; i < max; i++) {
                let text = `            <tr class="listings" name="${i}" id="listings">
                        <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].name}</p></td>
                        <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].address}</p></td>
                        <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].neighborhood}</p></td>
                        <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].beds}</p></td>
                        <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].baths}</p></td>
                        <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].area}</td>
                        <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].price}</p></td>
                        <td id="link" class="normal"><a class="listings" id="listings" name="linkToListing" href="${entries[count].link}">Link</a></td>
                        <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input value="${i}" class="listings" name="listingSelector" type="checkbox"></div></td>
                        </tr>`
                $("#daTable").trigger('addRows', [text, false, null]);
                count++;
            }
        }
        else {
            for (let i = count; i < entries.length; i++) {
                let text = `            <tr class="listings" name="${i}" id="listings">
                        <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].name}</p></td>
                        <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].address}</p></td>
                        <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].neighborhood}</p></td>
                        <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].beds}</p></td>
                        <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].baths}</p></td>
                        <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].area}</td>
                        <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].price}</p></td>
                        <td id="link" class="normal"><a class="listings" id="listings" name="listings" href="${entries[count].link}">Link</a></td>
                        <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input value="${i}" class="listings" name="listingSelector" type="checkbox"></div></td>
                        </tr>`
                $("#daTable").trigger('addRows', [text, false, null]);
                count++;
            }
        }
    });

    // load 250 listings on button click
    load250.addEventListener('click', async () => {
        if ((entries.length - count) > 250) {
            const max = count + 250;
            for (let i = count; i < max; i++) {
                let text = `            <tr class="listings" name="${i}" id="listings">
                        <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].name}</p></td>
                        <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].address}</p></td>
                        <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].neighborhood}</p></td>
                        <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].beds}</p></td>
                        <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].baths}</p></td>
                        <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].area}</td>
                        <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].price}</p></td>
                        <td id="link" class="normal"><a class="listings" id="listings" name="linkToListing" href="${entries[count].link}">Link</a></td>
                        <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input value="${i}" class="listings" name="listingSelector" type="checkbox"></div></td>
                        </tr>`
                $("#daTable").trigger('addRows', [text, false, null]);
                count++;
            }
        }
        else {
            for (let i = count; i < entries.length; i++) {
                let text = `            <tr class="listings" name="${i}" id="listings">
                        <td id="name" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].name}</p></td>
                        <td id="address" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].address}</p></td>
                        <td id="neighborhood" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].neighborhood}</p></td>
                        <td id="beds" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].beds}</p></td>
                        <td id="baths" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].baths}</p></td>
                        <td id="area" class="normal"><p class="listings" name ="listings" id="hide">${entries[count].area}</td>
                        <td id="price" class="normal"><p class="listings" name ="listings" id="listings">${entries[count].price}</p></td>
                        <td id="link" class="normal"><a class="listings" id="listings" name="listings" href="${entries[count].link}">Link</a></td>
                        <td id="select" class="normal"><div style="margin: auto; display: block; text-align: center; transform: translateY(40%);"><input value="${i}" class="listings" name="listingSelector" type="checkbox"></div></td>
                        </tr>`
                $("#daTable").trigger('addRows', [text, false, null]);
                count++;
            }
        }
    });
});

// general document click listener (EVENTS IN BLOCKING ORDER)
document.onclick = event => {
    // selected checkboxes move into array
    if (event.target.getAttribute('name') === "listingSelector") {
        const selection = document.querySelector(`tr[name="${event.target.getAttribute('value')}"]`);
        if (selected.includes(selection)) {
            selected.splice(selected.indexOf(selection),1);
        }
        else {
            selected.push(selection);
        }
    }

    // if selected > 0 show selectButtons
    if (selected.length > 0) {
        selectButtons.style.display = "block";
    }
    else {
        selectButtons.style.display = "none";
    }
}

// about/contact buttons
// // about toggle
aboutPop.addEventListener('click', () => {
    switch (document.getElementById("aboutInfo").style.display) {
        case "none":
        case "":
            document.getElementById("aboutInfo").style.display = "block";
            document.getElementById("contactInfo").style.display = "none";
            break;
        case "block":
            document.getElementById("aboutInfo").style.display = "none";
            break;
    }
});
aboutClose.addEventListener('click', () => { 
    document.getElementById("aboutInfo").style.display = "none"; 
    document.getElementById("contactInfo").style.display = "none";
});
// // contact toggle
contactPop.addEventListener('click', () => {
    switch (document.getElementById("contactInfo").style.display) {
        case "none":
        case "":
            document.getElementById("contactInfo").style.display = "block";
            document.getElementById("aboutInfo").style.display = "none";
            break;
        case "block":
            document.getElementById("contactInfo").style.display = "none";
            break;
    }
});
contactClose.addEventListener('click', () => { 
    document.getElementById("aboutInfo").style.display = "none"; 
    document.getElementById("contactInfo").style.display = "none"; 
});

// selected listings' buttons listeners
// // favorite listings
favorite.addEventListener('click', () => {

});
// // share listings
share.addEventListener('click', () => {
    let text = "Check out these listings on https://www.homeyhopping.com:";
    selected.forEach(listing => {
        text += "\n• " + listing.querySelector('a[name="linkToListing"]').href;
    });
    navigator.clipboard.writeText(text);
    showNotif(`<strong>ALERT!<br><br>Copied Selection(s) To Clipboard!</strong>`);
});
// // hide listings
hide.addEventListener('click', () => {
    selected.forEach(listing => {
        listing.remove();
        $("#daTable").trigger('update', [false, null]);
    });
    selected = [];
    showNotif(`<strong>ALERT!<br><br>Selection(s) Hidden!</strong>`);
});
// // clear selections
clear.addEventListener('click', () => {
    const selections = document.querySelectorAll('input:checked');
    selections.forEach(selection => {
        selection.checked = false;
    });
    selected = [];
    showNotif(`<strong>ALERT!<br><br>Cleared Selection(s)!</strong>`);
});

// notification
const showNotif = async (message) => {
    popuptext.innerHTML = message;
    popup.classList.toggle('fade');
    setTimeout(() => {
        popup.classList.toggle('fade');
    }, 2000);
}