const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-message');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', async () => {
    const message = userInput.value.trim();
    if (message) {
        // Display user message
        appendMessage(message, 'user');
        userInput.value = ''; // Clear input field

        // Send message to backend for processing (dummy response for now)
        

        // Display chatbot response
        appendMessage(response, 'bot');
    }
});

function appendMessage(message, type) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message');
    messageElement.innerHTML = `<span class="${type}-message">${message}</span>`;
    chatHistory.appendChild(messageElement);
    chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to bottom after new message
}
