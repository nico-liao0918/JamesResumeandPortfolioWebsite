// script.js / wqrcgs.js

// Elements
const networkNameInput = document.getElementById('networkName');
const passwordInput = document.getElementById('password');
const generateBtn = document.getElementById('generateBtn');
const qrCodeContainer = document.getElementById('qrcode');

function generateQRCode() {
    const networkName = networkNameInput.value.trim();
    const password = passwordInput.value.trim();

    if (!networkName) {
        alert("Please enter the Network Name.");
        return;
    }

    // Allow password to be optional
    const wifiQRData = password 
        ? `WIFI:S:${networkName};T:WPA;P:${password};;`
        : `WIFI:S:${networkName};;`;

    // Clear previous QR code
    qrCodeContainer.innerHTML = '';

    // Generate new QR code
    new QRCode(qrCodeContainer, {
        text: wifiQRData,
        width: 300,  // smaller and more responsive size
        height: 300
    });

    // Provide feedback - better user experience without alert
    const successMsg = document.createElement('p');
    successMsg.textContent = "QR Code generated successfully!";
    successMsg.style.color = "green";

    // Remove previous message if any
    const oldMsg = qrCodeContainer.querySelector('p');
    if (oldMsg) oldMsg.remove();

    qrCodeContainer.appendChild(successMsg);

    // Optionally clear inputs
    networkNameInput.value = '';
    passwordInput.value = '';
}

generateBtn.addEventListener('click', generateQRCode);
