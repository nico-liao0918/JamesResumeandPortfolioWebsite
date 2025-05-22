// script.js / wqrcgs.js

// Get DOM elements
const networkNameInput = document.getElementById('networkName');
const passwordInput = document.getElementById('password');
const generateBtn = document.getElementById('generateBtn');
const downloadBtn = document.getElementById('downloadBtn');
const qrCodeContainer = document.getElementById('qrcode');

// Function to generate the WiFi QR Code
function generateQRCode() {
    const networkName = networkNameInput.value.trim();
    const password = passwordInput.value.trim();

    // Ensure network name is provided
    if (!networkName) {
        alert("Please enter the Network Name.");
        return;
    }

    // Construct QR code string in WiFi format
    const wifiQRData = password 
        ? `WIFI:S:${networkName};T:WPA;P:${password};;`
        : `WIFI:S:${networkName};;`;

    // Clear previous QR code
    qrCodeContainer.innerHTML = '';

    // Create new QR code as an image
    new QRCode(qrCodeContainer, {
        text: wifiQRData,
        width: 300,
        height: 300,
        useSVG: false
    });

    // Optionally reset form
    networkNameInput.value = '';
    passwordInput.value = '';
}

// Function to download the QR Code as JPEG
function downloadQRCode() {
    const img = qrCodeContainer.querySelector('img');
    if (!img) {
        alert("Please generate the QR code first!");
        return;
    }

    const a = document.createElement('a');
    a.href = img.src;
    a.download = 'wifi-qr-code.jpg';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Attach event listeners
generateBtn.addEventListener('click', generateQRCode);
downloadBtn.addEventListener('click', downloadQRCode);