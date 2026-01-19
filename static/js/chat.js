document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('send-btn').addEventListener('click', sendMessage);

    // Send message when Enter is pressed, but not when Shift+Enter is pressed
    document.getElementById('chat-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent the default action to avoid a line break or form submit
            sendMessage();
        }
    });

    function sendMessage() {
        var input = document.getElementById('chat-input');
        var message = input.value.trim();
        if (message) {
            addMessage(message, 'sent');

            // Send the message to the Flask backend
            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: message}),
            })
            .then(response => response.json())
            .then(data => {
                // Display the response from Flask/OpenAI
                addMessage(data.response, 'received');
                scrollToBottom();
            })
            .catch((error) => {
                console.error('Error:', error);
                addMessage("Error getting response.", 'received');
            });

            input.value = '';
        }
    }

    function addMessage(text, type) {
        var chatMessages = document.getElementById('chat-messages');
        var messageDiv = document.createElement('div');
        messageDiv.classList.add('message', type);
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        scrollToBottom(); // Ensure the newest message is always in view
    }

    function scrollToBottom() {
        var chatMessages = document.getElementById('chat-messages');
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Existing code for showing/hiding the chat interface
    const chatIcon = document.getElementById('chat-icon');
    const chatContainer = document.getElementById('chat-container');
    const closeButton = document.getElementById('close-btn');

    chatIcon.addEventListener('click', function() {
        chatContainer.style.display = 'block';
        chatIcon.style.display = 'none';
    });

    closeButton.addEventListener('click', function() {
        chatContainer.style.display = 'none';
        chatIcon.style.display = 'block';
    });
});
