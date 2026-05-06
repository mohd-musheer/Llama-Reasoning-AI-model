const chatList = document.getElementById("chatList");
const chatForm = document.getElementById("chatForm");
const promptInput = document.getElementById("promptInput");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearBtn");

let isGenerating = false;

const welcomeText =
  "Hello. Ask me anything and I will reason it out step by step.";

function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function formatMarkdownLike(text) {
  if (!text) {
    return "";
  }

  const escaped = escapeHtml(text);
  const segments = escaped.split(/```/);
  let html = "";

  segments.forEach((segment, index) => {
    if (index % 2 === 1) {
      const cleaned = segment.replace(/^\n/, "").replace(/\n$/, "");
      html += `<pre><code>${cleaned}</code></pre>`;
      return;
    }

    let part = segment
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\*(.+?)\*/g, "<em>$1</em>")
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\n/g, "<br>");

    html += part;
  });

  return html;
}

function autoScroll(smooth) {
  chatList.scrollTo({
    top: chatList.scrollHeight,
    behavior: smooth ? "smooth" : "auto",
  });
}

function createMessage(role) {
  const message = document.createElement("div");
  message.className = `message ${role}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";

  message.appendChild(bubble);
  chatList.appendChild(message);
  autoScroll(true);

  return { message, bubble };
}

function addUserMessage(text) {
  const { bubble } = createMessage("user");
  bubble.innerHTML = formatMarkdownLike(text);
}

function addAssistantMessage(text) {
  const { bubble } = createMessage("assistant");
  bubble.innerHTML = formatMarkdownLike(text);
}

function addTypingIndicator() {
  const { bubble } = createMessage("assistant");
  bubble.classList.add("typing");
  bubble.innerHTML =
    '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
  return bubble;
}

function setLoadingState(loading) {
  isGenerating = loading;
  sendBtn.disabled = loading;
  promptInput.disabled = loading;
  chatForm.classList.toggle("loading", loading);
}

function resizeInput() {
  promptInput.style.height = "auto";
  promptInput.style.height = `${Math.min(promptInput.scrollHeight, 160)}px`;
}

function typeText(bubble, text) {
  return new Promise((resolve) => {
    const stream = document.createElement("span");
    stream.className = "stream";
    bubble.appendChild(stream);

    const tokens = text.split(/(\s+)/);
    let index = 0;
    const step = Math.max(1, Math.floor(tokens.length / 3000));

    const timer = setInterval(() => {
      stream.textContent += tokens.slice(index, index + step).join("");
      index += step;
      autoScroll(true);

      if (index >= tokens.length) {
        clearInterval(timer);
        resolve();
      }
    }, 14);
  });
}

async function handleSubmit(event) {
  event.preventDefault();
  if (isGenerating) {
    return;
  }

  const prompt = promptInput.value.trim();
  if (!prompt) {
    return;
  }

  addUserMessage(prompt);
  promptInput.value = "";
  resizeInput();
  setLoadingState(true);

  const typingBubble = addTypingIndicator();

  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt }),
    });

    if (!response.ok) {
      throw new Error(`Request failed (${response.status})`);
    }

    const data = await response.json();
    const output = data.response || "";

    typingBubble.classList.remove("typing");
    typingBubble.innerHTML = "";

    await typeText(typingBubble, output);
    typingBubble.innerHTML = formatMarkdownLike(output) || "";
  } catch (error) {
    typingBubble.classList.remove("typing");
    typingBubble.innerHTML =
      "Sorry, I could not reach the model server. Please try again.";
  } finally {
    setLoadingState(false);
    promptInput.focus();
  }
}

function handleKeyDown(event) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    chatForm.requestSubmit();
  }
}

function resetChat() {
  chatList.innerHTML = "";
  addAssistantMessage(welcomeText);
}

promptInput.addEventListener("input", resizeInput);
promptInput.addEventListener("keydown", handleKeyDown);
chatForm.addEventListener("submit", handleSubmit);
clearBtn.addEventListener("click", resetChat);

resetChat();
