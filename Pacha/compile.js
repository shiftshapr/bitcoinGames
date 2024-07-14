/*
{
  "p": "brc69",
  "op": "compile",
  "s": "pacha"
}
*/

//const collectionJsonUrl = '/content/1e671dcced26b5daa2d453703fc60a0e76cac5513d8a406618b0eb3d9c1b2ef0i0';
const collectionJsonUrl = '/content/1e671dcced26b5daa2d453703fc60a0e76cac5513d8a406618b0eb3d9c1b2ef0i0';
const imageRendering = 'pixelated';
const renderSize = { width: 400, height: 400 };

async function loadImage (url) {
    return new Promise((resolve, reject) => {
        const image = document.createElement('img');
        image.src = url;
        console.log(image.src);
        image.crossOrigin = 'anonymous';
        image.onload = () => {
            resolve(image)
        }
        image.onerror = () => {
            if (!image.src.startsWith('https://')) {
                image.src = 'https://ordinals.com' + url;
            } else if (image.src.startsWith('https://ordinals.com')) {
                image.src = 'https://ord-mirror.magiceden.dev' + url;
            } else {
                reject(new Error("Failed to load the image from all sources."));
            }
        }
    })
}

async function renderImage(imageEl, traitUrls) {
    const canvas = document.createElement('canvas');
    canvas.width = renderSize.width;
    canvas.height = renderSize.height;
    const ctx = canvas.getContext("2d");
    ctx.imageSmoothingEnabled = false;

    try {
        const modifiedBaseImage = await loadImage(baseTraitUrl);
        ctx.drawImage(modifiedBaseImage, 150, 80, 500, 500);
    } catch (e) {
        console.error("Error drawing the base image:", e);
    }

    const otherImages = await Promise.all(traitUrls.map(loadImage));
    otherImages.forEach(_ => ctx.drawImage(_, 0, 0, canvas.width, canvas.height));
    
    imageEl.src = canvas.toDataURL("image/png");
}

async function getAllTraits(traitsUrl, retry = false) {
    try {
        const collectionMetadataRes = await fetch(traitsUrl)
        const collectionMetadata = await collectionMetadataRes.json()
        return collectionMetadata.attributes.map(_ => `/content/${_}`)
    } catch (e) {
        if (!retry) {
            const timestamp = Math.floor(Date.now() / (60000 * 10))
            const newTraitsUrl = `${traitsUrl}?timestamp=${timestamp}`
            return getAllTraits(newTraitsUrl, true)
        }
        throw e
    }
}

function createInitialImage () {
    // Manipulate the <body> tag
    document.body.style.margin = '0px';
    document.body.style.padding = '0px';

    const img = document.createElement('img');
    img.id = 'img';
    img.style.height = '100%';
    img.style.width = '100%';
    img.style.objectFit = 'contain';
    img.style.imageRendering = imageRendering;

    return img
}

async function createInscriptionHtml() {
    const imageEl = createInitialImage();
    const selectedTraitIndexes = document.querySelector('script[t]').getAttribute('t').split(',');
    const traitIndexes = selectedTraitIndexes.slice(0);

    try {
        const allTraits = await getAllTraits(collectionJsonUrl);
        const traits = traitIndexes.map(_ => allTraits[+_]);
        
        await renderImage(imageEl, traits);

    } catch (e) {
        console.error(e);
    } finally {
        document.body.appendChild(imageEl);
    }
}

window.onload = function() {
    createInscriptionHtml();
}