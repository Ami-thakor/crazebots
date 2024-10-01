// Function to initialize PayPal buttons
function initPayPalButtons() {
  const paypalButtonContainer = document.getElementById("paypal-button");
  const Continuebtn = document.getElementById("Continue-btn");
  const user_ID = document.getElementById("userid").value;
  const planName = document.getElementById("plan-name").innerText;
  

  paypal
    .Buttons({
      onClick() {
        const user_ID = document.getElementById("userid").value;

        if (user_ID.length < 3) {
          alert("Please fill all the details");
          return false;
        } else {
        }
      },
      createOrder: function (data, actions) {
        const amountElement = document.getElementById("data-amount");
        const amount_ = parseFloat(amountElement.dataset.amount);
        console.log(amount_);
        console.log(data);
        return actions.order.create({
          purchase_units: [
            {
              amount: {
                value: `${amount_}`,
              },
            },
          ],
          application_context: { shipping_preference: "NO_SHIPPING" },
        });
      },
      onApprove: function (data, actions) {
        // Capture the funds from the transaction
        return actions.order.capture().then(function (details) {
          var Transaction_ID =
            details.purchase_units[0].payments.captures[0].id;

          window.location.href = `/success/${Transaction_ID + "$" + user_ID + "$" + planName}`;
         
        });
      },
      onError: function (err) {
        // Handle errors or failed payment
        console.error("An error occurred:", err);
        alert("An error occurred. Please try again.");
      },
    })
    .render(paypalButtonContainer);

  Continuebtn.style.display = "none";
}

const checkOut = (planId) => {
  window.location.href = `/payment?plan=${planId}`;
};
