let isProcessing = false;

function sendMessage() {
    if(isProcessing) return;
    
    const input = document.getElementById('userInput');
    const chatWindow = document.getElementById('chatWindow');
    
    if(!input.value.trim()) return;

    isProcessing = true;
    const sendBtn = document.querySelector('.send-button');
    sendBtn.disabled = true;
    sendBtn.textContent = '...';

    const userDiv = document.createElement('div');
    userDiv.className = 'message user-message';
    userDiv.innerHTML = `<div class="message-bubble">${input.value}</div>`;
    chatWindow.appendChild(userDiv);

    fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: input.value})
    })
    .then(response => response.json())
    .then(data => {
        const aiDiv = document.createElement('div');
        aiDiv.className = 'message ai-message';
        aiDiv.innerHTML = `<div class="message-bubble" data-priority="${data.priority}">${data.message}</div>`;
        chatWindow.appendChild(aiDiv);
    })
    .catch(() => {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'message ai-message';
        errorDiv.innerHTML = '<div class="message-bubble" data-priority="critical">Connection error</div>';
        chatWindow.appendChild(errorDiv);
    })
    .finally(() => {
        input.value = '';
        isProcessing = false;
        sendBtn.disabled = false;
        sendBtn.textContent = 'Send';
        chatWindow.scrollTop = chatWindow.scrollHeight;
    });
}

document.getElementById('userInput').addEventListener('keydown', function(e) {
    if(e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});