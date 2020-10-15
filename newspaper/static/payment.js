let paymentBtn = document.getElementById('successPayment');
if(paymentBtn) {
    paymentBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/premiumNewsSuccess/")
    .then((result) => {
        window.location.href = '/premium';
    });
  });
}