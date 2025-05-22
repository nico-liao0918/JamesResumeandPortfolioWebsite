// script.js / wqrcgs.js

// Get DOM elements
const networkNameInput = document.getElementById('networkName');
const passwordInput = document.getElementById('password');
const generateBtn = document.getElementById('generateBtn');
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

    // Clear previous QR code and messages
    qrCodeContainer.innerHTML = '';

    // Create new QR code
    new QRCode(qrCodeContainer, {
        text: wifiQRData,
        width: 300,
        height: 300
    });

    // Create success message
    const successMsg = document.createElement('p');
    successMsg.textContent = "QR Code generated successfully!";
    successMsg.style.color = "green";
    successMsg.style.marginTop = "10px";
    successMsg.style.fontWeight = "bold";

    qrCodeContainer.appendChild(successMsg);

    // Optionally reset form
    networkNameInput.value = '';
    passwordInput.value = '';
}

// Attach event listener
generateBtn.addEventListener('click', generateQRCode);
