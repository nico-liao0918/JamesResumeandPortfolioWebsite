// script.js

// Elements
const networkNameInput = document.getElementById('networkName');
const passwordInput = document.getElementById('password');
const generateBtn = document.getElementById('generateBtn');
const qrCodeContainer = document.getElementById('qrcode');

// Function to generate the QR code
function generateQRCode() {
    const networkName = networkNameInput.value.trim();
    const password = passwordInput.value.trim();

    // Validate inputs
    if (!networkName || !password) {
        alert("Please fill in both fields.");
        return;
    }

    // WiFi format for QR code
    const wifiQRData = `WIFI:S:${networkName};T:WPA;P:${password};;`;

    // Clear any previous QR codes
    qrCodeContainer.innerHTML = '';

    // Generate the new QR code
    new QRCode(qrCodeContainer, {
        text: wifiQRData,
        width: 500,
        height: 500
    });

    // Optionally clear inputs after generation
    networkNameInput.value = '';
    passwordInput.value = '';

    // Provide feedback to the user
    alert("QR Code generated successfully!");
}

// Event listener for the button
generateBtn.addEventListener('click', generateQRCode);