// script.js / wqrcgs.js

document.addEventListener('DOMContentLoaded', function () {
    // Get DOM elements
    const networkNameInput = document.getElementById('networkName');
    const passwordInput = document.getElementById('password');
    const generateBtn = document.getElementById('generateBtn');
    const qrCodeContainer = document.getElementById('qrcode');
    const downloadBtn = document.getElementById('downloadBtn');

    let lastQRCodeCanvas = null; // Save reference to QR canvas for download

    function generateQRCode() {
        const networkName = networkNameInput.value.trim();
        const password = passwordInput.value.trim();

        if (!networkName) {
            alert("Please enter the Network Name.");
            return;
        }

        const wifiQRData = password 
            ? `WIFI:S:${networkName};T:WPA;P:${password};;`
            : `WIFI:S:${networkName};;`;

        // Clear previous QR code and message
        qrCodeContainer.innerHTML = '';
        lastQRCodeCanvas = null;

        // Generate QR code
        const qr = new QRCode(qrCodeContainer, {
            text: wifiQRData,
            width: 300,
            height: 300
        });

        // Delay to ensure QRCode is rendered in DOM
        setTimeout(() => {
            const canvas = qrCodeContainer.querySelector('canvas');
            if (canvas) lastQRCodeCanvas = canvas;

            const successMsg = document.createElement('p');
            successMsg.textContent = "QR Code generated successfully!";
            successMsg.style.color = "green";
            successMsg.style.marginTop = "10px";
            successMsg.style.fontWeight = "bold";
            qrCodeContainer.appendChild(successMsg);
        }, 200);

        // Reset form
        networkNameInput.value = '';
        passwordInput.value = '';
    }

    function downloadQRCodeAsJPEG() {
        if (!lastQRCodeCanvas) {
            alert("Please generate a QR Code first.");
            return;
        }

        const dataURL = lastQRCodeCanvas.toDataURL("image/jpeg");
        const link = document.createElement('a');
        link.href = dataURL;
        link.download = "wifi-qr-code.jpg";
        link.click();
    }

    generateBtn.addEventListener('click', generateQRCode);
    downloadBtn.addEventListener('click', downloadQRCodeAsJPEG);
});
