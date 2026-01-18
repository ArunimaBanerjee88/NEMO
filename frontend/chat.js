const API_BASE = "http://127.0.0.1:8000";
const chatBox = document.getElementById("chatBox");
const input = document.getElementById("userInput");

// ✅ GET USER ID FROM GOOGLE CALLBACK
const params = new URLSearchParams(window.location.search);
const USER_ID = params.get("user_id");

if (!USER_ID) {
  alert("Not logged in. Redirecting...");
  window.location.href = "index.html";
}

addMessage("assistant", "Hi 😊 I’m NEMO. Ask me anything you want to learn.");

async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  input.value = "";

  addMessage("assistant", "Typing…");

  try {
    const res = await fetch(`${API_BASE}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: parseInt(USER_ID),
        message: message
      })
    });

    const data = await res.json();
    chatBox.lastChild.remove(); // remove "Typing…"
    addMessage("assistant", data.reply);

  } catch (err) {
    chatBox.lastChild.remove();
    addMessage("assistant", "⚠️ I had trouble responding.");
    console.error(err);
  }
}

function addMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `msg ${role}`;
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendMessage();
});
